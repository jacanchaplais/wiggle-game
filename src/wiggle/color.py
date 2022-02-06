from typing import Tuple
from colour import Color


def rgb_255(rgb_floats: Tuple[float, float, float]) -> Tuple[int, int, int]:
    return tuple(map(lambda v: int(v * 255), rgb_floats))  # type: ignore


def color_tuple(rep: str) -> Tuple[int, int, int]:
    color = Color(rep)
    rgb_floats = color.rgb
    rgb_ints = rgb_255(rgb_floats)
    return rgb_ints
