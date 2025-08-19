from typing import Literal, Mapping, NamedTuple, Optional, TypedDict

MaterialType = Literal["Raw", "Manufactured", "Encoded"]


class Material(NamedTuple):
    type: MaterialType
    key: str


class MaterialInfo(TypedDict):
    name: str
    grade: int


class StationInfo(TypedDict):
    system: str
    station: str


class LocationInfo(TypedDict):
    name: str
    system: str
    body: str
    materials: list[Material]
    trader: Optional[StationInfo]


ENC_ADAPTIVEENCRYPTORS = Material("Encoded", "adaptiveencryptors")
ENC_CONSUMERFIRMWARE = Material("Encoded", "consumerfirmware")
ENC_ENCRYPTIONARCHIVES = Material("Encoded", "encryptionarchives")
ENC_INDUSTRIALFIRMWARE = Material("Encoded", "industrialfirmware")

MFG_CHEMICALMANIPULATORS = Material("Manufactured", "chemicalmanipulators")
MFG_COMPOUNDSHIELDING = Material("Manufactured", "compoundshielding")
MFG_CONDUCTIVEPOLYMERS = Material("Manufactured", "conductivepolymers")
MFG_CONFIGURABLECOMPONENTS = Material("Manufactured", "configurablecomponents")
MFG_HEATVANES = Material("Manufactured", "heatvanes")
MFG_POLYMERCAPACITORS = Material("Manufactured", "polymercapacitors")
MFG_REFINEDFOCUSCRYSTALS = Material("Manufactured", "refinedfocuscrystals")

RAW_ANTIMONY = Material("Raw", "antimony")
RAW_CADMIUM = Material("Raw", "cadmium")
RAW_MERCURY = Material("Raw", "mercury")
RAW_MOLYBDENUM = Material("Raw", "molybdenum")
RAW_NIOBIUM = Material("Raw", "niobium")
RAW_POLONIUM = Material("Raw", "polonium")
RAW_RUTHENIUM = Material("Raw", "ruthenium")
RAW_SELENIUM = Material("Raw", "selenium")
RAW_TECHNETIUM = Material("Raw", "technetium")
RAW_TELLURIUM = Material("Raw", "tellurium")
RAW_TIN = Material("Raw", "tin")
RAW_TUNGSTEN = Material("Raw", "tungsten")
RAW_YTTRIUM = Material("Raw", "yttrium")
RAW_ZIRCONIUM = Material("Raw", "zirconium")

MATERIALS: Mapping[Material, MaterialInfo] = {
    # Encoded: Emission Data:
    #   Exceptional Scrambled Emission Data 1
    #   Irregular Emission Data 2
    #   Unexpected Emission Data 3
    #   Decoded Emission Data 4
    #   Abnormal Compact Emissions Data 5
    # Encoded: Wake Scans:
    #   Atypical Disrupted Wake Echoes 1
    #   Anomalous FSD Telemetry 2
    #   Strange Wake Solutions 3
    #   Eccentric Hyperspace Trajectories 4
    #   Datamined Wake Exceptions 5
    # Encoded: Shield Data:
    #   Distorted Shield Cycle Recordings 1
    #   Inconsistent Shield Soak Analysis 2
    #   Untypical Shield Scans 3
    #   Aberrant Shield Pattern Analysis 4
    #   Peculiar Shield Frequency Data 5
    # Encoded: Encryption Files:
    #   Unusual Encrypted Files 1
    #   Tagged Encryption Codes 2
    #   Open Symmetric Keys 3
    ENC_ENCRYPTIONARCHIVES: {
        "name": "Atypical Encryption Archives",
        "grade": 4,
    },
    ENC_ADAPTIVEENCRYPTORS: {
        "name": "Adaptive Encryptors Capture",
        "grade": 5,
    },
    # Encoded: Data Archives:
    #   Anomalous Bulk Scan Data 1
    #   Unidentified Scan Archives 2
    #   Classified Scan Databanks 3
    #   Divergent Scan Data 4
    #   Classified Scan Fragment 5
    # Encoded: Encoded Firmware:
    #   Specialised Legacy Firmware 1
    ENC_CONSUMERFIRMWARE: {
        "name": "Modified Consumer Firmware",
        "grade": 2,
    },
    ENC_INDUSTRIALFIRMWARE: {
        "name": "Cracked Industrial Firmware",
        "grade": 3,
    },
    #   Security Firmware Patch 4
    #   Modified Embedded Firmware 5
    #
    #######################################################
    #
    # Raw: Category 1:
    #   Carbon 1
    #   Vanadium 2
    RAW_NIOBIUM: {
        "name": "Niobium",
        "grade": 3,
    },
    RAW_YTTRIUM: {
        "name": "Yttrium",
        "grade": 4,
    },
    # Raw: Category 2:
    #   Phosphorus 1
    #   Chromium 2
    RAW_MOLYBDENUM: {
        "name": "Molybdenum",
        "grade": 3,
    },
    RAW_TECHNETIUM: {
        "name": "Technetium",
        "grade": 4,
    },
    # Raw: Category 3:
    #   Sulphur 1
    #   Manganese 2
    RAW_CADMIUM: {
        "name": "Cadmium",
        "grade": 3,
    },
    RAW_RUTHENIUM: {
        "name": "Ruthenium",
        "grade": 4,
    },
    # Raw: Category 4:
    #   Iron 1
    #   Zinc 2
    RAW_TIN: {
        "name": "Tin",
        "grade": 3,
    },
    RAW_SELENIUM: {
        "name": "Selenium",
        "grade": 4,
    },
    # Raw: Category 5:
    #   Nickel 1
    #   Germanium 2
    RAW_TUNGSTEN: {
        "name": "Tungsten",
        "grade": 3,
    },
    RAW_TELLURIUM: {
        "name": "Tellurium",
        "grade": 4,
    },
    # Raw: Category 6:
    #   Rhenium 1
    #   Arsenic 2
    RAW_MERCURY: {
        "name": "Mercury",
        "grade": 3,
    },
    RAW_POLONIUM: {
        "name": "Polonium",
        "grade": 4,
    },
    # Raw: Category 7:
    #   Lead 1
    RAW_ZIRCONIUM: {
        "name": "Zirconium",
        "grade": 2,
    },
    #   Boron 3
    RAW_ANTIMONY: {
        "name": "Antimony",
        "grade": 4,
    },
    #
    #######################################################
    #
    # Manufactured: Chemical:
    #   Chemical Storage Units 1
    #   Chemical Processors 2
    #   Chemical Distillery 3
    MFG_CHEMICALMANIPULATORS: {
        "name": "Chemical Manipulators",
        "grade": 4,
    },
    #   Pharmaceutical Isolators 5
    # Manufactured: Thermic:
    #   Tempered Alloys 1
    #   Heat Resistant Ceramics 2
    #   Precipitated Alloys 3
    #   Thermic Alloys 4
    #   Military Grade Alloys 5
    # Manufactured: Heat:
    #   Heat Conduction Wiring 1
    #   Heat Dispersion Plate 2
    #   Heat Exchangers 3
    MFG_HEATVANES: {
        "name": "Heat Vanes",
        "grade": 4,
    },
    #   Proto Heat Radiators 5
    # Manufactured: Conductive:
    #   Basic Conductors 1
    #   Conductive Components 2
    #   Conductive Ceramics 3
    MFG_CONDUCTIVEPOLYMERS: {
        "name": "Conductive Polymers",
        "grade": 4,
    },
    #   Biotech Conductors 5
    # Manufactured: Mechanical Components:
    #   Mechanical Scrap 1
    #   Mechanical Equipment 2
    #   Mechanical Components 3
    MFG_CONFIGURABLECOMPONENTS: {
        "name": "Configurable Components",
        "grade": 4,
    },
    #   Improvised Components 5
    # Manufactured: Capacitors:
    #   Grid Resistors 1
    #   Hybrid Capacitors 2
    #   Electrochemical Arrays 3
    MFG_POLYMERCAPACITORS: {
        "name": "Polymer Capacitors",
        "grade": 4,
    },
    #   Military Supercapacitors 5
    # Manufactured: Shielding:
    #   Worn Shield Emitters 1
    #   Shield Emitters 2
    #   Shielding Sensors 3
    MFG_COMPOUNDSHIELDING: {
        "name": "Compound Shielding",
        "grade": 4,
    },
    #   Imperial Shielding 5
    # Manufactured: Composite:
    #   Compact Composites 1
    #   Filament Composites 2
    #   High Density Composites 3
    #   Proprietary Composites 4
    #   Core Dynamics Composites 5
    # Manufactured: Crystals:
    #   Crystal Shards 1
    #   Flawed Focus Crystals 2
    #   Focus Crystals 3
    MFG_REFINEDFOCUSCRYSTALS: {
        "name": "Refined Focus Crystals",
        "grade": 4,
    },
    #   Exquisite Focus Crystals 5
    # Manufactured: Alloys:
    #   Salvaged Alloys 1
    #   Galvanising Alloys 2
    #   Phase Alloys 3
    #   Proto Light Alloys 4
    #   Proto Radiolic Alloys 5
}

# Map system to a location, for faster lookup
# Note: try to keep to 7 items or just G4/G5...
LOCATIONS: Mapping[str, list[LocationInfo]] = {
    "HIP 12099": [
        # https://canonn.science/codex/cmdr-john-jameson-crashed-cobra-mkiii/
        # https://redshiftlogistics.online/2020/02/15/data-farm-1.html
        {
            "name": "Jameson Crash Site",
            "system": "HIP 12099",
            "body": "HIP 12099 1 b",
            "materials": [
                ENC_ADAPTIVEENCRYPTORS,
                ENC_ENCRYPTIONARCHIVES,
                ENC_INDUSTRIALFIRMWARE,
                ENC_CONSUMERFIRMWARE,
            ],
            "trader": {"system": "Diaguandri", "station": "Ray Gateway"},
        },
    ],
    "Hyades Sector DR-V c2-23": [
        # https://canonn.science/codex/davs-hope/
        # https://redshiftlogistics.online/2020/04/25/manufactured-material-farm-1.html
        {
            "name": "Dav's Hope",
            "system": "Hyades Sector DR-V c2-23",
            "body": "Hyades Sector DR-V c2-23 a 5",
            "materials": [
                MFG_CHEMICALMANIPULATORS,
                MFG_COMPOUNDSHIELDING,
                MFG_CONDUCTIVEPOLYMERS,
                MFG_CONFIGURABLECOMPONENTS,
                MFG_HEATVANES,
                MFG_POLYMERCAPACITORS,
                MFG_REFINEDFOCUSCRYSTALS,
            ],
            "trader": {"system": "HIP 12067", "station": "Vaucanson Gateway"},
        }
    ],
    "Koli Discii": [
        # https://canonn.science/codex/koli-discii-crashed-ship/
        {
            "name": "Crashed Anaconda",
            "system": "Koli Discii",
            "body": "Koli Discii C 6 a",
            "materials": [
                RAW_ANTIMONY,
                RAW_RUTHENIUM,
                RAW_TELLURIUM,
                RAW_TUNGSTEN,
                RAW_ZIRCONIUM,
            ],
            "trader": None,
        }
    ],
    "Orrere": [
        # https://canonn.science/codex/orrere-crashed-ship/
        {
            "name": "Crashed Anaconda",
            "system": "Orrere",
            "body": "Orrere 2 b",
            "materials": [
                RAW_ANTIMONY,
                RAW_RUTHENIUM,
                RAW_TELLURIUM,
                RAW_TUNGSTEN,
                RAW_ZIRCONIUM,
            ],
            "trader": None,
        }
    ],
    "35 G. Carinae": [
        # https://www.reddit.com/r/EliteDangerous/comments/1j7otmi/update_41_raw_materials_collection_no_relog/
        {
            "name": "Brain Tree",
            "system": "35 G. Carinae",
            "body": "35 G. Carinae 1 e",
            "materials": [
                RAW_ANTIMONY,
                RAW_CADMIUM,
                RAW_MOLYBDENUM,
            ],
            "trader": None,
        },
        # https://www.reddit.com/r/EliteDangerous/comments/1j7otmi/update_41_raw_materials_collection_no_relog/
        {
            "name": "Brain Tree",
            "system": "35 G. Carinae",
            "body": "35 G. Carinae 2 a",
            "materials": [
                RAW_TECHNETIUM,
                RAW_NIOBIUM,
                RAW_TIN,
            ],
            "trader": None,
        },
        # https://www.reddit.com/r/EliteDangerous/comments/1j7otmi/update_41_raw_materials_collection_no_relog/
        {
            "name": "Brain Tree",
            "system": "35 G. Carinae",
            "body": "35 G. Carinae 2 c",
            "materials": [
                RAW_RUTHENIUM,
                RAW_MOLYBDENUM,
                RAW_TUNGSTEN,
            ],
            "trader": None,
        },
        # https://www.reddit.com/r/EliteDangerous/comments/1j7otmi/update_41_raw_materials_collection_no_relog/
        {
            "name": "Brain Tree",
            "system": "35 G. Carinae",
            "body": "35 G. Carinae 2 d",
            "materials": [
                RAW_YTTRIUM,
                RAW_NIOBIUM,
                RAW_TUNGSTEN,
            ],
            "trader": None,
        },
    ],
    "HR 3230": [
        # https://www.reddit.com/r/EliteDangerous/comments/1j7otmi/update_41_raw_materials_collection_no_relog/
        {
            "name": "Brain Tree",
            "system": "HR 3230",
            "body": "HR 3230 3 a a",
            "materials": [
                RAW_SELENIUM,
                RAW_TECHNETIUM,
                RAW_NIOBIUM,
                RAW_TIN,
            ],
            "trader": None,
        },
    ],
    "Synuefe SE-V b49-4": [
        # https://www.reddit.com/r/EliteDangerous/comments/1j7otmi/update_41_raw_materials_collection_no_relog/
        {
            "name": "Brain Tree",
            "system": "Synuefe SE-V b49-4",
            "body": "Synuefe SE-V b49-4 B 3 a",
            "materials": [
                RAW_SELENIUM,
                RAW_TECHNETIUM,
                RAW_NIOBIUM,
                RAW_MERCURY,
            ],
            "trader": None,
        },
    ],
    "Synuefe AA-P c22-7": [
        # https://www.reddit.com/r/EliteDangerous/comments/1j7otmi/update_41_raw_materials_collection_no_relog/
        {
            "name": "Brain Tree",
            "system": "Synuefe AA-P c22-7",
            "body": "Synuefe AA-P c22-7 5 c",
            "materials": [
                RAW_POLONIUM,
                RAW_MOLYBDENUM,
                RAW_TIN,
            ],
            "trader": None,
        },
    ],
}
