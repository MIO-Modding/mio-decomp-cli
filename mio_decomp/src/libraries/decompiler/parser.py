from enum import StrEnum, auto
from pathlib import Path
from typing import Annotated

import typer
from pydantic import BaseModel, Field, conint
from rich import print  # noqa: F401

from .constants import MAX_UINT64

u32 = Annotated[int, conint(strict=True, ge=0, le=4294967295)]
u64 = Annotated[int, Field(ge=0, le=MAX_UINT64)]


class Flags(StrEnum):
    Acquired = auto()
    Equipped = auto()


class f32x2(BaseModel):
    x: float
    y: float

    def __init__(self, x: int | float, y: int | float, **kwargs) -> None:
        super(f32x2, self).__init__(x=x, y=y, **kwargs)


class f32x3(BaseModel):
    x: float
    y: float
    z: float

    def __init__(
        self, x: int | float, y: int | float, z: int | float, **kwargs
    ) -> None:
        super(f32x3, self).__init__(x=x, y=y, z=z, **kwargs)


class Trail(BaseModel):
    points: list = []


class Marker(BaseModel):
    pos: f32x2 = f32x2(0.000000, 0.000000)
    type: u32 = 0
    placed: bool = False


class Markers(BaseModel):
    markers: list[Marker] = [Marker() for _ in range(16)]


class MapManager(BaseModel):
    displayed: bool = False


class MIOParts(BaseModel):
    map_manager: MapManager = MapManager()


class Enum_single(StrEnum):
    Up = auto()
    Cuve = auto()
    Start = auto()
    Personal_assistant = auto()
    Unknown = auto()
    Intro = auto()
    First_encounter = auto()
    Rambling = auto()
    City = auto()


class HalynAlign(BaseModel):
    configuration_discrete: int = 2
    first_rotation_ever: bool = True
    state: Enum_single = Enum_single.Up


class Tomo(BaseModel):
    quest: Enum_single = Enum_single.Cuve


class FrailPuppet(BaseModel):
    quest: Enum_single = Enum_single.Start


class Capu(BaseModel):
    capu_name: Enum_single = Enum_single.Personal_assistant
    quest: Enum_single = Enum_single.Start


class Hacker(BaseModel):
    hacker_name: Enum_single = Enum_single.Unknown
    met_at_least_once: bool = False


class Philosopher(BaseModel):
    repaired_tuner: bool = False
    tuner_interacted: bool = False


class Shii(BaseModel):
    quest: Enum_single = Enum_single.Intro
    still_dead_when_hub_attacked: bool = False
    bridge_intro_done: bool = False


class Minions(BaseModel):
    sin: bool = False
    cos: bool = False
    tan: bool = False


class Mel(BaseModel):
    quest: Enum_single = Enum_single.Intro
    name: Enum_single = Enum_single.Unknown
    minions: Minions = Minions()
    met_in_shop_once: bool = False
    rambo_awoken: bool = False


class Cos(BaseModel):
    encountered: bool = False
    cos_keepers_spawned: bool = False
    cos_keepers_killed: bool = False


class Tan(BaseModel):
    fan_stopped: bool = False


class Rad(BaseModel):
    quest: Enum_single = Enum_single.First_encounter


class Estrogen(BaseModel):
    quest: Enum_single = Enum_single.Rambling
    has_refused_audience: bool = False


class MIOPlotPoints(BaseModel):
    death_after_hub: u32 = 0


class HalynPlotPoints(BaseModel):
    encountered: bool = False
    statue: Enum_single = Enum_single.City


class Goliath(BaseModel):
    in_observatory: bool = False
    room_entrance_triggers: list[str] = ["" for _ in range(12)]


class PlotPoints(BaseModel):
    tomo: Tomo = Tomo()
    frail_puppet: FrailPuppet = FrailPuppet()
    capu: Capu = Capu()
    hacker: Hacker = Hacker()
    philosopher: Philosopher = Philosopher()
    shii: Shii = Shii()
    mel: Mel = Mel()
    cos: Cos = Cos()
    tan: Tan = Tan()
    rad: Rad = Rad()
    estragon: Estrogen = Estrogen()
    mio: MIOPlotPoints = MIOPlotPoints()
    halyn: HalynPlotPoints = HalynPlotPoints()
    goliath: Goliath = Goliath()


class Factorio(BaseModel):
    selected_experiment: u32 = 4


class MapState(BaseModel):
    face_inside_bits: list[u32] = [0 for _ in range(1241)]
    edge_visited_bits: list[u32] = [0 for _ in range(1408)]


class Trinket(BaseModel):
    equip_order: u32 = 0


class Rebuild(BaseModel):
    scrap_investment: u32 = 0
    step: u32 = 1


class RebuildNPC(BaseModel):
    scrap_investment: u32 = 0


class DatapadFlags(StrEnum):
    UNIMPLEMENTED = auto()  # Not real, but i needed a flag to put here


class Datapad(BaseModel):
    status: DatapadFlags = DatapadFlags.UNIMPLEMENTED
    discovery_index: int = 0
    mark_as_read: bool = False


class PairValue(BaseModel):
    flags: list[Flags] = []
    count: int = 0
    trinket: Trinket | None = None
    rebuild: Rebuild | None = None
    rebuild_npc: RebuildNPC | None = None
    datapad: Datapad | None = None


class Pair(BaseModel):
    key: str = ""
    value: PairValue = PairValue()


class SavedEntries(BaseModel):
    pairs: list[Pair] = [Pair() for _ in range(1638)]


class Save(BaseModel):
    flags: list[Flags] = []
    version: u32 = 5
    id: u64 = 0
    checkpoint_id: str = Field(
        default="cp_FOCUS_dispatch_zone",
    )
    checkpoint_world_pos: f32x3 = f32x3(-1000.000000, 4426.000000, 0.000000)
    checkpoint_wrap_index: int = 0
    checkpoint_is_temporary: bool = False
    previous_checkpoint_id: str = ""
    previous_checkpoint_world_pos: f32x3 = f32x3(0.000000, 0.000000, 0.000000)
    previous_checkpoint_wrap_index: int = 0
    trail: Trail = Trail()
    markers: Markers = Markers()
    mio_parts: MIOParts = MIOParts()
    halyn_align: HalynAlign = HalynAlign()
    map_trace_flags: list[Flags] = []
    plotpoints: PlotPoints = PlotPoints()
    nextfest_demo_time_to_bad_ending: float = -1.0
    nextfest_demo_time_to_good_ending: float = -1.0
    orb_slash_slot: str = ""
    factorio: Factorio = Factorio()
    nacre_in_hub_basin: u32 = 0
    nacre_buffered_in_hub_basin: u32 = 0
    shield_decay_mask: u32 = 1
    mio_wrap_index: int = 0
    map_state: MapState = MapState()


class SavedVisibility2(BaseModel):
    pairs: list = []


class SavedNotImportant(BaseModel):
    playtime: float = 0.0
    last_save_time: float = 0.0
    liquid_nacres_count: u32 = 0
    solidify_nacre_count: int = 0


class MIOSave(BaseModel):
    save: Save = Save()
    saved_entries: SavedEntries = SavedEntries()
    saved_visibility2: SavedVisibility2 = SavedVisibility2()
    saved_not_important: SavedNotImportant = SavedNotImportant()


class SaveParser:
    def __init__(self):
        self.save: MIOSave = MIOSave()

    def __convert_value(self, value: str):
        if value.startswith("i32"):
            return int(value[4:-1])
        elif value.startswith("u32"):
            return int(value[4:-1])
        elif value.startswith("u64"):
            return int(value[4:-1])
        elif value.startswith("String"):
            return value[8:-2]
        elif value.startswith("bool"):
            return value[5] == "t"
        elif value.startswith("f32x3"):
            nums: list[float] = [float(n) for n in value[6:-1].split(", ")]
            return f32x3(*nums)
        elif value.startswith("f32x2"):
            nums: list[float] = [float(n) for n in value[6:-1].split(", ")]
            return f32x2(*nums)
        elif value.startswith("f32"):
            return float(value[4:-1])
        elif value.startswith("f64"):
            return float(value[4:-1])
        else:
            typer.Abort()
            return None

    def __safe_set_value_by_key(self, group: str, key: str, value: str) -> None:
        if value.startswith("Array"):
            return

        access_string: str = f"{group.lower()}.{key}"
        current_object = self.save
        parts = access_string.split(".")
        for part in parts[:-1]:
            if part.isdigit():
                current_object = current_object[int(part)]  # ty:ignore[not-subscriptable]
            else:
                if getattr(current_object, part) is None:
                    match part:
                        case "datapad":
                            setattr(current_object, "datapad", Datapad())
                        case "rebuild":
                            setattr(current_object, "rebuild", Rebuild())
                        case "rebuild_npc":
                            setattr(current_object, "rebuild_npc", RebuildNPC())
                        case "trinket":
                            setattr(current_object, "trinket", Trinket())
                        case _:
                            print(f"NONE FOUND! {part}")

                current_object = getattr(current_object, part)

        processed_value = self.__convert_value(value)
        if value is None:
            typer.Abort()

        if isinstance(current_object, list):
            current_object[int(parts[-1])] = processed_value
        else:
            setattr(current_object, parts[-1], processed_value)

    def parse_save(self, input_path: Path) -> str:
        """Parses a MIO save file into JSON.

        Args:
            input_path (Path): Path to the save_file.

        Returns:
            str: The JSON representing the save file.
        """
        lines: list[str] = [
            line.strip()
            for line in input_path.read_text(encoding="utf-8").splitlines()
            if not line == ""
        ]

        grouped_lines: dict[str, list[str]] = {}

        current_group: str | None = None

        for line in lines:
            line = line.strip()
            if current_group is None:
                if line.endswith("{"):
                    current_group = line[:-2]
                    grouped_lines[current_group] = []
                    continue
            else:
                if line == "}":
                    current_group = None
                    continue
                grouped_lines[current_group].append(line)

        for group, lines in grouped_lines.items():
            for line in lines:
                key, _, value = line.split(" ", 2)
                self.__safe_set_value_by_key(group, key, value)

        return self.save.model_dump_json(indent=4, exclude_none=True)


if __name__ == "__main__":
    parser: SaveParser = SaveParser()
    parser.__safe_set_value_by_key("", "", "")
