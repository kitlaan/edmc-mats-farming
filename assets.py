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
ENC_ANCIENTBIOLOGICALDATA = Material("Encoded", "ancientbiologicaldata")
ENC_ANCIENTCULTURALDATA = Material("Encoded", "ancientculturaldata")
ENC_ANCIENTHISTORICALDATA = Material("Encoded", "ancienthistoricaldata")
ENC_ANCIENTLANGUAGEDATA = Material("Encoded", "ancientlanguagedata")
ENC_ANCIENTTECHNOLOGICALDATA = Material("Encoded", "ancienttechnologicaldata")
ENC_ARCHIVEDEMISSIONDATA = Material("Encoded", "archivedemissiondata")
ENC_BULKSCANDATA = Material("Encoded", "bulkscandata")
ENC_CLASSIFIEDSCANDATA = Material("Encoded", "classifiedscandata")
ENC_COMPACTEMISSIONSDATA = Material("Encoded", "compactemissionsdata")
ENC_CONSUMERFIRMWARE = Material("Encoded", "consumerfirmware")
ENC_DATAMINEDWAKE = Material("Encoded", "dataminedwake")
ENC_DECODEDEMISSIONDATA = Material("Encoded", "decodedemissiondata")
ENC_DISRUPTEDWAKEECHOES = Material("Encoded", "disruptedwakeechoes")
ENC_EMBEDDEDFIRMWARE = Material("Encoded", "embeddedfirmware")
ENC_EMISSIONDATA = Material("Encoded", "emissiondata")
ENC_ENCODEDSCANDATA = Material("Encoded", "encodedscandata")
ENC_ENCRYPTEDFILES = Material("Encoded", "encryptedfiles")
ENC_ENCRYPTIONARCHIVES = Material("Encoded", "encryptionarchives")
ENC_ENCRYPTIONCODES = Material("Encoded", "encryptioncodes")
ENC_FSDTELEMETRY = Material("Encoded", "fsdtelemetry")
ENC_GUARDIAN_MODULEBLUEPRINT = Material("Encoded", "guardian_moduleblueprint")
ENC_HYPERSPACETRAJECTORIES = Material("Encoded", "hyperspacetrajectories")
ENC_INDUSTRIALFIRMWARE = Material("Encoded", "industrialfirmware")
ENC_LEGACYFIRMWARE = Material("Encoded", "legacyfirmware")
ENC_SCANARCHIVES = Material("Encoded", "scanarchives")
ENC_SCANDATABANKS = Material("Encoded", "scandatabanks")
ENC_SCRAMBLEDEMISSIONDATA = Material("Encoded", "scrambledemissiondata")
ENC_SECURITYFIRMWARE = Material("Encoded", "securityfirmware")
ENC_SHIELDCYCLERECORDINGS = Material("Encoded", "shieldcyclerecordings")
ENC_SHIELDDENSITYREPORTS = Material("Encoded", "shielddensityreports")
ENC_SHIELDFREQUENCYDATA = Material("Encoded", "shieldfrequencydata")
ENC_SHIELDPATTERNANALYSIS = Material("Encoded", "shieldpatternanalysis")
ENC_SHIELDSOAKANALYSIS = Material("Encoded", "shieldsoakanalysis")
ENC_SYMMETRICKEYS = Material("Encoded", "symmetrickeys")
ENC_TG_INTERDICTIONDATA = Material("Encoded", "tg_interdictiondata")
ENC_TG_SHIPFLIGHTDATA = Material("Encoded", "tg_shipflightdata")
ENC_TG_SHIPSYSTEMSDATA = Material("Encoded", "tg_shipsystemsdata")
ENC_TG_SHUTDOWNDATA = Material("Encoded", "tg_shutdowndata")
ENC_UNKNOWNSHIPSIGNATURE = Material("Encoded", "unknownshipsignature")
ENC_WAKESOLUTIONS = Material("Encoded", "wakesolutions")

MFG_BASICCONDUCTORS = Material("Manufactured", "basicconductors")
MFG_BIOTECHCONDUCTORS = Material("Manufactured", "biotechconductors")
MFG_CHEMICALDISTILLERY = Material("Manufactured", "chemicaldistillery")
MFG_CHEMICALMANIPULATORS = Material("Manufactured", "chemicalmanipulators")
MFG_CHEMICALPROCESSORS = Material("Manufactured", "chemicalprocessors")
MFG_CHEMICALSTORAGEUNITS = Material("Manufactured", "chemicalstorageunits")
MFG_COMPACTCOMPOSITES = Material("Manufactured", "compactcomposites")
MFG_COMPOUNDSHIELDING = Material("Manufactured", "compoundshielding")
MFG_CONDUCTIVECERAMICS = Material("Manufactured", "conductiveceramics")
MFG_CONDUCTIVECOMPONENTS = Material("Manufactured", "conductivecomponents")
MFG_CONDUCTIVEPOLYMERS = Material("Manufactured", "conductivepolymers")
MFG_CONFIGURABLECOMPONENTS = Material("Manufactured", "configurablecomponents")
MFG_CRYSTALSHARDS = Material("Manufactured", "crystalshards")
MFG_ELECTROCHEMICALARRAYS = Material("Manufactured", "electrochemicalarrays")
MFG_EXQUISITEFOCUSCRYSTALS = Material("Manufactured", "exquisitefocuscrystals")
MFG_FEDCORECOMPOSITES = Material("Manufactured", "fedcorecomposites")
MFG_FEDPROPRIETARYCOMPOSITES = Material("Manufactured", "fedproprietarycomposites")
MFG_FILAMENTCOMPOSITES = Material("Manufactured", "filamentcomposites")
MFG_FOCUSCRYSTALS = Material("Manufactured", "focuscrystals")
MFG_GALVANISINGALLOYS = Material("Manufactured", "galvanisingalloys")
MFG_GRIDRESISTORS = Material("Manufactured", "gridresistors")
MFG_GUARDIAN_POWERCELL = Material("Manufactured", "guardian_powercell")
MFG_GUARDIAN_POWERCONDUIT = Material("Manufactured", "guardian_powerconduit")
MFG_GUARDIAN_SENTINEL_WEAPONPARTS = Material(
    "Manufactured", "guardian_sentinel_weaponparts"
)
MFG_GUARDIAN_SENTINEL_WRECKAGECOMPONENTS = Material(
    "Manufactured", "guardian_sentinel_wreckagecomponents"
)
MFG_GUARDIAN_TECHCOMPONENT = Material("Manufactured", "guardian_techcomponent")
MFG_HEATCONDUCTIONWIRING = Material("Manufactured", "heatconductionwiring")
MFG_HEATDISPERSIONPLATE = Material("Manufactured", "heatdispersionplate")
MFG_HEATEXCHANGERS = Material("Manufactured", "heatexchangers")
MFG_HEATRESISTANTCERAMICS = Material("Manufactured", "heatresistantceramics")
MFG_HEATVANES = Material("Manufactured", "heatvanes")
MFG_HIGHDENSITYCOMPOSITES = Material("Manufactured", "highdensitycomposites")
MFG_HYBRIDCAPACITORS = Material("Manufactured", "hybridcapacitors")
MFG_IMPERIALSHIELDING = Material("Manufactured", "imperialshielding")
MFG_IMPROVISEDCOMPONENTS = Material("Manufactured", "improvisedcomponents")
MFG_MECHANICALCOMPONENTS = Material("Manufactured", "mechanicalcomponents")
MFG_MECHANICALEQUIPMENT = Material("Manufactured", "mechanicalequipment")
MFG_MECHANICALSCRAP = Material("Manufactured", "mechanicalscrap")
MFG_MILITARYGRADEALLOYS = Material("Manufactured", "militarygradealloys")
MFG_MILITARYSUPERCAPACITORS = Material("Manufactured", "militarysupercapacitors")
MFG_PHARMACEUTICALISOLATORS = Material("Manufactured", "pharmaceuticalisolators")
MFG_PHASEALLOYS = Material("Manufactured", "phasealloys")
MFG_POLYMERCAPACITORS = Material("Manufactured", "polymercapacitors")
MFG_PRECIPITATEDALLOYS = Material("Manufactured", "precipitatedalloys")
MFG_PROTOHEATRADIATORS = Material("Manufactured", "protoheatradiators")
MFG_PROTOLIGHTALLOYS = Material("Manufactured", "protolightalloys")
MFG_PROTORADIOLICALLOYS = Material("Manufactured", "protoradiolicalloys")
MFG_REFINEDFOCUSCRYSTALS = Material("Manufactured", "refinedfocuscrystals")
MFG_SALVAGEDALLOYS = Material("Manufactured", "salvagedalloys")
MFG_SHIELDEMITTERS = Material("Manufactured", "shieldemitters")
MFG_SHIELDINGSENSORS = Material("Manufactured", "shieldingsensors")
MFG_TEMPEREDALLOYS = Material("Manufactured", "temperedalloys")
MFG_TG_ABRASION01 = Material("Manufactured", "tg_abrasion01")
MFG_TG_ABRASION02 = Material("Manufactured", "tg_abrasion02")
MFG_TG_ABRASION03 = Material("Manufactured", "tg_abrasion03")
MFG_TG_BIOMECHANICALCONDUITS = Material("Manufactured", "tg_biomechanicalconduits")
MFG_TG_CAUSTICCRYSTAL = Material("Manufactured", "tg_causticcrystal")
MFG_TG_CAUSTICGENERATORPARTS = Material("Manufactured", "tg_causticgeneratorparts")
MFG_TG_CAUSTICSHARD = Material("Manufactured", "tg_causticshard")
MFG_TG_PROPULSIONELEMENT = Material("Manufactured", "tg_propulsionelement")
MFG_TG_WEAPONPARTS = Material("Manufactured", "tg_weaponparts")
MFG_TG_WRECKAGECOMPONENTS = Material("Manufactured", "tg_wreckagecomponents")
MFG_THERMICALLOYS = Material("Manufactured", "thermicalloys")
MFG_UNCUTFOCUSCRYSTALS = Material("Manufactured", "uncutfocuscrystals")
MFG_UNKNOWNCARAPACE = Material("Manufactured", "unknowncarapace")
MFG_UNKNOWNENERGYCELL = Material("Manufactured", "unknownenergycell")
MFG_UNKNOWNENERGYSOURCE = Material("Manufactured", "unknownenergysource")
MFG_UNKNOWNORGANICCIRCUITRY = Material("Manufactured", "unknownorganiccircuitry")
MFG_WORNSHIELDEMITTERS = Material("Manufactured", "wornshieldemitters")

RAW_ANTIMONY = Material("Raw", "antimony")
RAW_ARSENIC = Material("Raw", "arsenic")
RAW_BORON = Material("Raw", "boron")
RAW_CADMIUM = Material("Raw", "cadmium")
RAW_CARBON = Material("Raw", "carbon")
RAW_CHROMIUM = Material("Raw", "chromium")
RAW_GERMANIUM = Material("Raw", "germanium")
RAW_IRON = Material("Raw", "iron")
RAW_LEAD = Material("Raw", "lead")
RAW_MANGANESE = Material("Raw", "manganese")
RAW_MERCURY = Material("Raw", "mercury")
RAW_MOLYBDENUM = Material("Raw", "molybdenum")
RAW_NICKEL = Material("Raw", "nickel")
RAW_NIOBIUM = Material("Raw", "niobium")
RAW_PHOSPHORUS = Material("Raw", "phosphorus")
RAW_POLONIUM = Material("Raw", "polonium")
RAW_RHENIUM = Material("Raw", "rhenium")
RAW_RUTHENIUM = Material("Raw", "ruthenium")
RAW_SELENIUM = Material("Raw", "selenium")
RAW_SULPHUR = Material("Raw", "sulphur")
RAW_TECHNETIUM = Material("Raw", "technetium")
RAW_TELLURIUM = Material("Raw", "tellurium")
RAW_TIN = Material("Raw", "tin")
RAW_TUNGSTEN = Material("Raw", "tungsten")
RAW_VANADIUM = Material("Raw", "vanadium")
RAW_YTTRIUM = Material("Raw", "yttrium")
RAW_ZINC = Material("Raw", "zinc")
RAW_ZIRCONIUM = Material("Raw", "zirconium")

MATERIALS: Mapping[Material, MaterialInfo] = {
    # Encoded: Emission Data:
    ENC_SCRAMBLEDEMISSIONDATA: {
        "grade": 1,
        "name": "Exceptional Scrambled Emission Data",
    },
    ENC_ARCHIVEDEMISSIONDATA: {"grade": 2, "name": "Irregular Emission Data"},
    ENC_EMISSIONDATA: {"grade": 3, "name": "Unexpected Emission Data"},
    ENC_DECODEDEMISSIONDATA: {"grade": 4, "name": "Decoded Emission Data"},
    ENC_COMPACTEMISSIONSDATA: {"grade": 5, "name": "Abnormal Compact Emissions Data"},
    # Encoded: Wake Scans:
    ENC_DISRUPTEDWAKEECHOES: {"grade": 1, "name": "Atypical Disrupted Wake Echoes"},
    ENC_FSDTELEMETRY: {"grade": 2, "name": "Anomalous FSD Telemetry"},
    ENC_WAKESOLUTIONS: {"grade": 3, "name": "Strange Wake Solutions"},
    ENC_HYPERSPACETRAJECTORIES: {
        "grade": 4,
        "name": "Eccentric Hyperspace Trajectories",
    },
    ENC_DATAMINEDWAKE: {"grade": 5, "name": "Datamined Wake Exceptions"},
    # Encoded: Shield Data:
    ENC_SHIELDCYCLERECORDINGS: {
        "grade": 1,
        "name": "Distorted Shield Cycle Recordings",
    },
    ENC_SHIELDSOAKANALYSIS: {"grade": 2, "name": "Inconsistent Shield Soak Analysis"},
    ENC_SHIELDDENSITYREPORTS: {"grade": 3, "name": "Untypical Shield Scans"},
    ENC_SHIELDPATTERNANALYSIS: {"grade": 4, "name": "Aberrant Shield Pattern Analysis"},
    ENC_SHIELDFREQUENCYDATA: {"grade": 5, "name": "Peculiar Shield Frequency Data"},
    # Encoded: Encryption Files:
    ENC_ENCRYPTEDFILES: {"grade": 1, "name": "Unusual Encrypted Files"},
    ENC_ENCRYPTIONCODES: {"grade": 2, "name": "Tagged Encryption Codes"},
    ENC_SYMMETRICKEYS: {"grade": 3, "name": "Open Symmetric Keys"},
    ENC_ENCRYPTIONARCHIVES: {"grade": 4, "name": "Atypical Encryption Archives"},
    ENC_ADAPTIVEENCRYPTORS: {"grade": 5, "name": "Adaptive Encryptors Capture"},
    # Encoded: Data Archives:
    ENC_BULKSCANDATA: {"grade": 1, "name": "Anomalous Bulk Scan Data"},
    ENC_SCANARCHIVES: {"grade": 2, "name": "Unidentified Scan Archives"},
    ENC_SCANDATABANKS: {"grade": 3, "name": "Classified Scan Databanks"},
    ENC_ENCODEDSCANDATA: {"grade": 4, "name": "Divergent Scan Data"},
    ENC_CLASSIFIEDSCANDATA: {"grade": 5, "name": "Classified Scan Fragment"},
    # Encoded: Encoded Firmware:
    ENC_LEGACYFIRMWARE: {"grade": 1, "name": "Specialised Legacy Firmware"},
    ENC_CONSUMERFIRMWARE: {"grade": 2, "name": "Modified Consumer Firmware"},
    ENC_INDUSTRIALFIRMWARE: {"grade": 3, "name": "Cracked Industrial Firmware"},
    ENC_SECURITYFIRMWARE: {"grade": 4, "name": "Security Firmware Patch"},
    ENC_EMBEDDEDFIRMWARE: {"grade": 5, "name": "Modified Embedded Firmware"},
    # Encoded: Guardian Stuff:
    ENC_ANCIENTBIOLOGICALDATA: {"grade": 0, "name": "Pattern Alpha Obelisk Data"},
    ENC_ANCIENTCULTURALDATA: {"grade": 0, "name": "Pattern Beta Obelisk Data"},
    ENC_ANCIENTHISTORICALDATA: {"grade": 0, "name": "Pattern Gamma Obelisk Data"},
    ENC_ANCIENTLANGUAGEDATA: {"grade": 0, "name": "Pattern Delta Obelisk Data"},
    ENC_ANCIENTTECHNOLOGICALDATA: {"grade": 0, "name": "Pattern Epsilon Obelisk Data"},
    ENC_GUARDIAN_MODULEBLUEPRINT: {
        "grade": 0,
        "name": "Guardian Module Blueprint Fragment",
    },
    # Encoded: Thargoid Stuff:
    ENC_TG_INTERDICTIONDATA: {"grade": 0, "name": "Thargoid Interdiction Telemetry"},
    ENC_TG_SHIPFLIGHTDATA: {"grade": 0, "name": "Ship Flight Data"},
    ENC_TG_SHIPSYSTEMSDATA: {"grade": 0, "name": "Ship Systems Data"},
    ENC_TG_SHUTDOWNDATA: {"grade": 0, "name": "Massive Energy Surge Analytics"},
    ENC_UNKNOWNSHIPSIGNATURE: {"grade": 0, "name": "Thargoid Ship Signature"},
    #
    #######################################################
    #
    # Raw: Category 1:
    RAW_CARBON: {"grade": 1, "name": "carbon"},
    RAW_VANADIUM: {"grade": 2, "name": "vanadium"},
    RAW_NIOBIUM: {"grade": 3, "name": "Niobium"},
    RAW_YTTRIUM: {"grade": 4, "name": "Yttrium"},
    # Raw: Category 2:
    RAW_PHOSPHORUS: {"grade": 1, "name": "phosphorus"},
    RAW_CHROMIUM: {"grade": 2, "name": "chromium"},
    RAW_MOLYBDENUM: {"grade": 3, "name": "Molybdenum"},
    RAW_TECHNETIUM: {"grade": 4, "name": "Technetium"},
    # Raw: Category 3:
    RAW_SULPHUR: {"grade": 1, "name": "sulphur"},
    RAW_MANGANESE: {"grade": 2, "name": "manganese"},
    RAW_CADMIUM: {"grade": 3, "name": "Cadmium"},
    RAW_RUTHENIUM: {"grade": 4, "name": "Ruthenium"},
    # Raw: Category 4:
    RAW_IRON: {"grade": 1, "name": "iron"},
    RAW_ZINC: {"grade": 2, "name": "zinc"},
    RAW_TIN: {"grade": 3, "name": "Tin"},
    RAW_SELENIUM: {"grade": 4, "name": "Selenium"},
    # Raw: Category 5:
    RAW_NICKEL: {"grade": 1, "name": "nickel"},
    RAW_GERMANIUM: {"grade": 2, "name": "germanium"},
    RAW_TUNGSTEN: {"grade": 3, "name": "Tungsten"},
    RAW_TELLURIUM: {"grade": 4, "name": "Tellurium"},
    # Raw: Category 6:
    RAW_RHENIUM: {"grade": 1, "name": "rhenium"},
    RAW_ARSENIC: {"grade": 2, "name": "arsenic"},
    RAW_MERCURY: {"grade": 3, "name": "Mercury"},
    RAW_POLONIUM: {"grade": 4, "name": "Polonium"},
    # Raw: Category 7:
    RAW_LEAD: {"grade": 1, "name": "lead"},
    RAW_ZIRCONIUM: {"grade": 2, "name": "Zirconium"},
    RAW_BORON: {"grade": 3, "name": "Boron"},
    RAW_ANTIMONY: {"grade": 4, "name": "Antimony"},
    #
    #######################################################
    #
    # Manufactured: Chemical:
    MFG_CHEMICALSTORAGEUNITS: {"grade": 1, "name": "Chemical Storage Units"},
    MFG_CHEMICALPROCESSORS: {"grade": 2, "name": "Chemical Processors"},
    MFG_CHEMICALDISTILLERY: {"grade": 3, "name": "Chemical Distillery"},
    MFG_CHEMICALMANIPULATORS: {"grade": 4, "name": "Chemical Manipulators"},
    MFG_PHARMACEUTICALISOLATORS: {"grade": 5, "name": "Pharmaceutical Isolators"},
    # Manufactured: Thermic:
    MFG_TEMPEREDALLOYS: {"grade": 1, "name": "Tempered Alloys"},
    MFG_HEATRESISTANTCERAMICS: {"grade": 2, "name": "Heat Resistant Ceramics"},
    MFG_PRECIPITATEDALLOYS: {"grade": 3, "name": "Precipitated Alloys"},
    MFG_THERMICALLOYS: {"grade": 4, "name": "Thermic Alloys"},
    MFG_MILITARYGRADEALLOYS: {"grade": 5, "name": "Military Grade Alloys"},
    # Manufactured: Heat:
    MFG_HEATCONDUCTIONWIRING: {"grade": 1, "name": "Heat Conduction Wiring"},
    MFG_HEATDISPERSIONPLATE: {"grade": 2, "name": "Heat Dispersion Plate"},
    MFG_HEATEXCHANGERS: {"grade": 3, "name": "Heat Exchangers"},
    MFG_HEATVANES: {"grade": 4, "name": "Heat Vanes"},
    MFG_PROTOHEATRADIATORS: {"grade": 5, "name": "Proto Heat Radiators"},
    # Manufactured: Conductive:
    MFG_BASICCONDUCTORS: {"grade": 1, "name": "Basic Conductors"},
    MFG_CONDUCTIVECOMPONENTS: {"grade": 2, "name": "Conductive Components"},
    MFG_CONDUCTIVECERAMICS: {"grade": 3, "name": "Conductive Ceramics"},
    MFG_CONDUCTIVEPOLYMERS: {"grade": 4, "name": "Conductive Polymers"},
    MFG_BIOTECHCONDUCTORS: {"grade": 5, "name": "Biotech Conductors"},
    # Manufactured: Mechanical Components:
    MFG_MECHANICALSCRAP: {"grade": 1, "name": "Mechanical Scrap"},
    MFG_MECHANICALEQUIPMENT: {"grade": 2, "name": "Mechanical Equipment"},
    MFG_MECHANICALCOMPONENTS: {"grade": 3, "name": "Mechanical Components"},
    MFG_CONFIGURABLECOMPONENTS: {"grade": 4, "name": "Configurable Components"},
    MFG_IMPROVISEDCOMPONENTS: {"grade": 5, "name": "Improvised Components"},
    # Manufactured: Capacitors:
    MFG_GRIDRESISTORS: {"grade": 1, "name": "Grid Resistors"},
    MFG_HYBRIDCAPACITORS: {"grade": 2, "name": "Hybrid Capacitors"},
    MFG_ELECTROCHEMICALARRAYS: {"grade": 3, "name": "Electrochemical Arrays"},
    MFG_POLYMERCAPACITORS: {"grade": 4, "name": "Polymer Capacitors"},
    MFG_MILITARYSUPERCAPACITORS: {"grade": 5, "name": "Military Supercapacitors"},
    # Manufactured: Shielding:
    MFG_WORNSHIELDEMITTERS: {"grade": 1, "name": "Worn Shield Emitters"},
    MFG_SHIELDEMITTERS: {"grade": 2, "name": "Shield Emitters"},
    MFG_SHIELDINGSENSORS: {"grade": 3, "name": "Shielding Sensors"},
    MFG_COMPOUNDSHIELDING: {"grade": 4, "name": "Compound Shielding"},
    MFG_IMPERIALSHIELDING: {"grade": 5, "name": "Imperial Shielding"},
    # Manufactured: Composite:
    MFG_COMPACTCOMPOSITES: {"grade": 1, "name": "Compact Composites"},
    MFG_FILAMENTCOMPOSITES: {"grade": 2, "name": "Filament Composites"},
    MFG_HIGHDENSITYCOMPOSITES: {"grade": 3, "name": "High Density Composites"},
    MFG_FEDPROPRIETARYCOMPOSITES: {"grade": 4, "name": "Proprietary Composites"},
    MFG_FEDCORECOMPOSITES: {"grade": 5, "name": "Core Dynamics Composites"},
    # Manufactured: Crystals:
    MFG_CRYSTALSHARDS: {"grade": 1, "name": "Crystal Shards"},
    MFG_UNCUTFOCUSCRYSTALS: {"grade": 2, "name": "Flawed Focus Crystals"},
    MFG_FOCUSCRYSTALS: {"grade": 3, "name": "Focus Crystals"},
    MFG_REFINEDFOCUSCRYSTALS: {"grade": 4, "name": "Refined Focus Crystals"},
    MFG_EXQUISITEFOCUSCRYSTALS: {"grade": 5, "name": "Exquisite Focus Crystals"},
    # Manufactured: Alloys:
    MFG_SALVAGEDALLOYS: {"grade": 1, "name": "Salvaged Alloys"},
    MFG_GALVANISINGALLOYS: {"grade": 2, "name": "Galvanising Alloys"},
    MFG_PHASEALLOYS: {"grade": 3, "name": "Phase Alloys"},
    MFG_PROTOLIGHTALLOYS: {"grade": 4, "name": "Proto Light Alloys"},
    MFG_PROTORADIOLICALLOYS: {"grade": 5, "name": "Proto Radiolic Alloys"},
    # Manufactured: Guardian Stuff:
    MFG_GUARDIAN_POWERCELL: {"grade": 0, "name": "Guardian Power Cell"},
    MFG_GUARDIAN_POWERCONDUIT: {"grade": 0, "name": "Guardian Power Conduit"},
    MFG_GUARDIAN_SENTINEL_WEAPONPARTS: {
        "grade": 0,
        "name": "Guardian Sentinel Weapon Parts",
    },
    MFG_GUARDIAN_SENTINEL_WRECKAGECOMPONENTS: {
        "grade": 0,
        "name": "Guardian Wreckage Components",
    },
    MFG_GUARDIAN_TECHCOMPONENT: {"grade": 0, "name": "Guardian Technology Component"},
    # Manufactured: Thargoid Stuff:
    MFG_TG_ABRASION01: {"grade": 0, "name": "Heat Exposure Specimen"},
    MFG_TG_ABRASION02: {"grade": 0, "name": "Phasing Membrane Residue"},
    MFG_TG_ABRASION03: {"grade": 0, "name": "Hardened Surface Fragments"},
    MFG_TG_BIOMECHANICALCONDUITS: {"grade": 0, "name": "Bio-Mechanical Conduits"},
    MFG_TG_CAUSTICCRYSTAL: {"grade": 0, "name": "Caustic Crystal"},
    MFG_TG_CAUSTICGENERATORPARTS: {"grade": 0, "name": "Corrosive Mechanisms"},
    MFG_TG_CAUSTICSHARD: {"grade": 0, "name": "Caustic Shard"},
    MFG_TG_PROPULSIONELEMENT: {"grade": 0, "name": "Propulsion Elements"},
    MFG_TG_WEAPONPARTS: {"grade": 0, "name": "Weapon Parts"},
    MFG_TG_WRECKAGECOMPONENTS: {"grade": 0, "name": "Wreckage Components"},
    MFG_UNKNOWNCARAPACE: {"grade": 0, "name": "Thargoid Carapace"},
    MFG_UNKNOWNENERGYCELL: {"grade": 0, "name": "Thargoid Energy Cell"},
    MFG_UNKNOWNENERGYSOURCE: {"grade": 0, "name": "Sensor Fragment"},
    MFG_UNKNOWNORGANICCIRCUITRY: {"grade": 0, "name": "Thargoid Organic Circuitry"},
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
            "body": "Hyades Sector DR-V c2-23 A 5",
            "materials": [
                MFG_CHEMICALMANIPULATORS,
                MFG_COMPOUNDSHIELDING,
                MFG_CONDUCTIVEPOLYMERS,
                MFG_CONFIGURABLECOMPONENTS,
                MFG_HEATVANES,
                MFG_POLYMERCAPACITORS,
                MFG_REFINEDFOCUSCRYSTALS,
                # the above are all G4's, but G1-3's also spawn. For example,
                #   Chemical Distillery 3
                #   Conductive Ceramics 3
                #   Electrochemical Arrays 3
                #   Focus Crystals 3
                #   Heat Exchangers 3
                #   High Density Composites 3
                #   Mechanical Components 3
                #   Phase Alloys 3
                #   Shielding Sensors 3
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
