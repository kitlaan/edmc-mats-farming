from __future__ import annotations

import logging
import os
import tkinter as tk
from typing import Any, Dict, Optional

from config import appname  # pyright: ignore[reportMissingImports]
from theme import theme  # pyright: ignore[reportMissingImports]

from assets import MATERIALS, LOCATIONS, LocationInfo, Material


plugin_name = os.path.basename(os.path.dirname(__file__))
logger = logging.getLogger(f"{appname}.{plugin_name}")


class This:
    """Holds module globals."""

    def __init__(self):
        self.parent: tk.Tk

        self.ui: tk.Frame
        self.ui_mats: tk.Frame
        self.ui_location: tk.StringVar = tk.StringVar(value="")
        self.ui_tracked_mats: Dict[Material, tk.StringVar] = {}

        self.tracked_location: Optional[LocationInfo] = None


this = This()


def plugin_start3(plugin_dir: str) -> str:
    """
    Start the plugin.

    :param plugin_dir: Name of directory this was loaded from.
    :return: Identifier string for this plugin.
    """
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
    tk.Label(this.ui, textvariable=this.ui_location, anchor=tk.W).grid(
        row=ui_row, column=1, sticky=tk.E
    )
    ui_row += 1

    this.ui_mats = tk.Frame(this.ui)
    this.ui_mats.grid(row=ui_row, columnspan=2, sticky=tk.NSEW)
    ui_row += 1

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

    if entry["event"] in ["ShutDown", "Shutdown"]:
        clear_mats()
    elif this.tracked_location:
        if (
            this.tracked_location["system"] != system
            or this.tracked_location["body"] != state["Body"]
        ):
            clear_mats()
    elif system in LOCATIONS:
        for location in LOCATIONS[system]:
            if location["body"] == state["Body"]:
                setup_mats(location)
                force_reload = True
                break

    if not this.tracked_location:
        # No tracked location, so nothing to do.
        return None

    if (
        entry["event"] in ["MaterialTrade", "MaterialCollected", "Materials"]
        or force_reload
    ):
        for mat, ui_text in this.ui_tracked_mats.items():
            state_materials = state.get(mat.type)
            if state_materials is not None:
                if mat.key in state_materials:
                    max_qty = grade_to_max(MATERIALS[mat]["grade"])
                    count = min(max_qty, state_materials[mat.key])
                    ui_text.set(f"{count}")
                else:
                    ui_text.set("0")

    return None


def clear_mats() -> None:
    """
    Clear the tracked location.
    """
    this.tracked_location = None

    this.ui_location.set("")
    this.ui_tracked_mats.clear()

    for widget in this.ui_mats.winfo_children():
        widget.destroy()
    this.ui_mats.grid_remove()


def setup_mats(location: LocationInfo) -> None:
    """
    Setup the materials UI for the given location.

    :param location: The location dictionary.
    """
    this.tracked_location = location
    this.ui_location.set(location["name"])

    row = this.ui_mats.grid_size()[1]
    for mat in location["materials"]:
        material = MATERIALS.get(mat)
        if not material:
            continue

        mat_name = material["name"]
        mat_grade = material["grade"]
        max_qty = grade_to_max(material["grade"])

        ui_text = tk.StringVar(value="")
        this.ui_tracked_mats[mat] = ui_text

        tk.Label(this.ui_mats, textvariable=ui_text).grid(
            row=row, column=0, sticky=tk.E
        )
        tk.Label(this.ui_mats, text=f"/{max_qty}").grid(row=row, column=1, sticky=tk.E)
        tk.Label(this.ui_mats, text=f"G{mat_grade} {mat_name}").grid(
            row=row, column=2, sticky=tk.W
        )
        row += 1

    if row > 0:
        this.ui_mats.grid()
    theme.update(this.ui_mats)


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
            return 0
