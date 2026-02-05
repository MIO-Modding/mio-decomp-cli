from enum import StrEnum, auto
from typing import Annotated

from pydantic import BaseModel, Field

from mio_decomp.src.libraries.decompiler.constants import MAX_UINT64

u8 = Annotated[int, Field(ge=0, le=255)]
u32 = Annotated[int, Field(ge=0, le=4294967295)]
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
