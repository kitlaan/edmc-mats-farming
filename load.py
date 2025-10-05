from __future__ import annotations

import logging
import os
import pathlib
import time
import tkinter as tk
from typing import Any, Dict, List, Optional, TypedDict

from config import appname, config  # pyright: ignore[reportMissingImports]
from theme import theme  # pyright: ignore[reportMissingImports]

from assets import (
    EMISSIONS,
    MATERIALS,
    LOCATIONS,
    EmissionInfo,
    LocationInfo,
    Material,
    MaterialType,
)

EXPIRY_SECS = 1.5 * 60

plugin_name = os.path.basename(os.path.dirname(__file__))
logger = logging.getLogger(f"{appname}.{plugin_name}")


class TrackedMaterial(TypedDict):
    ui_text: tk.StringVar
    labels: list[tk.Label]
    max_qty: int
    expiry: Optional[float]


class EmissionState(TypedDict):
    system: str
    state: List[EmissionInfo]


LOCALISED_NAMES: Dict[Material, str] = {}


class This:
    """Holds module globals."""

    def __init__(self):
        self.parent: tk.Tk

        self.ui: tk.Frame
        self.ui_mats: tk.Frame
        self.ui_state: tk.StringVar = tk.StringVar(value="")
        self.ui_tracked_mats: Dict[Material, TrackedMaterial] = {}

        self.tracked_location: Optional[LocationInfo] = None
        self.tracked_emission: Optional[EmissionState] = None

        self.system_allegiance: Optional[str] = None
        self.system_faction_state: Optional[str] = None
        self.system_population: int = 0
        self.saw_uss_hge: bool = False


this = This()


def plugin_start3(plugin_dir: str) -> str:
    """
    Start the plugin.

    :param plugin_dir: Name of directory this was loaded from.
    :return: Identifier string for this plugin.
    """
    # In prod, don't include DEBUG logging
    if not get_local_file(".git"):
        logger.setLevel(logging.INFO)

    return plugin_name


def plugin_app(parent: tk.Tk) -> Optional[tk.Frame]:
    """
    Construct this plugin's main UI, if any.

    :param parent: The tk parent to place our widgets into.
    :return: See PLUGINS.md#display
    """
    this.parent = parent

    this.ui = tk.Frame(parent)
    ui_row = this.ui.grid_size()[1]

    tk.Label(this.ui, text="Material Farm:").grid(row=ui_row, column=0, sticky=tk.W)
    tk.Label(this.ui, textvariable=this.ui_state, anchor=tk.W).grid(
        row=ui_row, column=1, sticky=tk.E
    )
    ui_row += 1

    this.ui_mats = tk.Frame(this.ui)
    this.ui_mats.grid(row=ui_row, columnspan=2, sticky=tk.NSEW)
    ui_row += 1

    def ui_poll():
        if not config.shutting_down:
            expire_mats()
            this.ui.after(1000, ui_poll)

    ui_poll()

    return this.ui


def journal_entry(
    cmdr: str,
    is_beta: bool,
    system: str,
    station: str,
    entry: Dict[str, Any],
    state: Dict[str, Any],
) -> Optional[str]:
    """
    Handle a new Journal event.

    :param cmdr: Name of Commander.
    :param is_beta: Whether game beta was detected.
    :param system: Name of current tracked system.
    :param station: Name of current tracked station location.
    :param entry: The journal event.
    :param state: `monitor.state`
    :return: None if no error, else an error string.
    """
    force_reload = False
    event = entry["event"]
    body = state["Body"]

    if event in ["ShutDown", "Shutdown"]:
        this.tracked_location = None
        this.tracked_emission = None
        clear_status()
        clear_mats()
        return None

    # Fill in cache of localised names
    if event == "MaterialCollected":
        add_mat_name(
            Material(entry["Category"], entry["Name"]), entry.get("Name_Localised")
        )
    elif event == "Materials":
        for category in ["Raw", "Manufactured", "Encoded"]:
            materials = entry.get(category, [])
            for mat in materials:
                cat: MaterialType = category  # type: ignore
                add_mat_name(Material(cat, mat["Name"]), mat.get("Name_Localised"))

    # Cache the current system state
    if event in ["Location", "FSDJump"]:
        this.system_allegiance = entry.get("SystemAllegiance")
        system_faction = entry.get("SystemFaction", {})
        this.system_faction_state = system_faction.get("FactionState")
        this.system_population = entry.get("Population", 0)
        this.saw_uss_hge = False
        logger.debug(
            f"System: allegiance={this.system_allegiance}, state={this.system_faction_state}, population={this.system_population}"
        )
    elif event == "FSSSignalDiscovered":
        if entry.get("USSType") == "$USS_Type_VeryValuableSalvage;":
            this.saw_uss_hge = True
            if not this.tracked_location:
                this.ui_state.set("HGE")

    # Figure out if what we're currently tracking is no longer valid
    if this.tracked_location:
        if (
            this.tracked_location["system"] != system
            or this.tracked_location["body"] != body
        ):
            logger.debug(
                f"Clearing tracked location: {this.tracked_location['system']} != {system} / {this.tracked_location['body']} != {body}"
            )
            this.tracked_location = None
            clear_status()
            clear_mats()
    elif this.tracked_emission:
        if this.tracked_emission["system"] != system or body != None:
            logger.debug(
                f"Clearing tracked emission: {this.tracked_emission['system']} != {system} / {body}"
            )
            this.tracked_emission = None
            clear_status()
            clear_mats()

    # Figure out what we're tracking
    if not this.tracked_location and not this.tracked_emission:
        location = get_location_state(entry, state)
        emissions = get_emission_state(entry, state)
        if location:
            logger.debug(f"Tracking new location: {location}")
            this.tracked_location = location
            setup_status(location["name"])
            setup_mats(location["materials"])
            force_reload = True
        elif emissions or this.saw_uss_hge:
            logger.debug(f"Tracking new emission: {emissions}")
            this.tracked_emission = {
                "system": system,
                "state": emissions,
            }
            setup_status("HGE" if this.saw_uss_hge else "HGE?")
            for emission in emissions:
                setup_mats(emission["materials"])
            force_reload = True

    # If we collected something, temporarily track it
    if event == "MaterialCollected":
        add_temp_mat(Material(entry["Category"], entry["Name"]))

    # Keep the counts of what we're tracking up to date
    if entry["event"] in ["MaterialCollected", "Materials"] or force_reload:
        for mat, item in this.ui_tracked_mats.items():
            state_materials = state.get(mat.type)
            if state_materials is not None:
                if mat.key in state_materials:
                    count = min(item["max_qty"], state_materials[mat.key])
                    item["ui_text"].set(f"{count}")
                else:
                    item["ui_text"].set("0")

    # TODO: show useful info about site:
    #  * coords
    #  * click-to-copy for trader system

    return None


def clear_status():
    this.ui_state.set("")


def setup_status(str):
    this.ui_state.set(str)


def clear_mats() -> None:
    this.ui_tracked_mats.clear()

    for widget in this.ui_mats.winfo_children():
        widget.destroy()
    this.ui_mats.grid_remove()


def setup_mats(materials: list[Material]):
    for mat in materials:
        add_mat(mat, None)

    if this.ui_mats.grid_size()[1] > 0:
        this.ui_mats.grid()
    theme.update(this.ui_mats)


def add_mat_name(mat: Material, localised: Optional[str]) -> None:
    if localised:
        LOCALISED_NAMES[mat] = localised


def add_mat(mat: Material, expiry: Optional[float]) -> bool:
    if mat in this.ui_tracked_mats:
        if this.ui_tracked_mats[mat]["expiry"] is not None:
            this.ui_tracked_mats[mat]["expiry"] = expiry
        return False

    material = MATERIALS.get(mat)
    if not material:
        return False

    mat_name = LOCALISED_NAMES[mat] if mat in LOCALISED_NAMES else material["name"]
    mat_grade = material["grade"]
    max_qty = grade_to_max(material["grade"])

    if mat_grade == 0:
        mat_grade = "?"

    ui_text = tk.StringVar(value="")

    row = this.ui_mats.grid_size()[1]

    labels = [
        tk.Label(
            this.ui_mats,
            textvariable=ui_text,
            pady=0,
            borderwidth=0,
            highlightthickness=0,
        ),
        tk.Label(
            this.ui_mats,
            text=f"/{max_qty}",
            pady=0,
            borderwidth=0,
            highlightthickness=0,
        ),
        tk.Label(
            this.ui_mats,
            text=f"G{mat_grade} {mat_name}",
            pady=0,
            borderwidth=0,
            highlightthickness=0,
        ),
    ]
    labels[0].grid(row=row, column=0, sticky=tk.E)
    labels[1].grid(row=row, column=1, sticky=tk.E)
    labels[2].grid(row=row, column=2, sticky=tk.W)

    this.ui_tracked_mats[mat] = {
        "ui_text": ui_text,
        "labels": labels,
        "max_qty": max_qty,
        "expiry": expiry,
    }
    return True


def add_temp_mat(mat: Material):
    if add_mat(mat, time.time() + EXPIRY_SECS):
        this.ui_mats.grid()
        theme.update(this.ui_mats)


def expire_mats():
    to_delete = []
    for mat, item in this.ui_tracked_mats.items():
        if item["expiry"] is not None and item["expiry"] < time.time():
            to_delete.append(mat)
    for mat in to_delete:
        item = this.ui_tracked_mats[mat]
        for widget in item["labels"]:
            widget.destroy()
        del this.ui_tracked_mats[mat]

    if to_delete and this.ui_mats.grid_size()[1] == 0:
        this.ui_mats.grid_remove()


def get_location_state(
    entry: Dict[str, Any], state: Dict[str, Any]
) -> Optional[LocationInfo]:
    system: Optional[str] = state["SystemName"]
    if system and system in LOCATIONS:
        for location in LOCATIONS[system]:
            if location["body"] == state["Body"]:
                return location
    return None


def get_emission_state(
    entry: Dict[str, Any], state: Dict[str, Any]
) -> List[EmissionInfo]:
    emissions = []
    for emission in EMISSIONS:
        if (
            "allegiance" in emission
            and emission["allegiance"] != this.system_allegiance
        ):
            continue
        if (
            "factionState" in emission
            and emission["factionState"] != this.system_faction_state
        ):
            continue
            pass
        if (
            this.system_population < 10_000_000
        ):  # folks say 1M, but let's use 10M to be less spammy
            continue
        emissions.append(emission)

    return emissions


def grade_to_max(grade: int) -> int:
    """
    Convert a material grade to its maximum quantity.

    :param grade: The material grade.
    :return: The maximum quantity for the given grade.
    """
    match grade:
        case 1:
            return 300
        case 2:
            return 250
        case 3:
            return 200
        case 4:
            return 150
        case 5:
            return 100
        case _:
            return 100


def get_local_file(filename: str) -> Optional[pathlib.Path]:
    plugin_dir = pathlib.Path(__file__).parent
    filepath = plugin_dir / filename
    return filepath if filepath.is_file() else None
