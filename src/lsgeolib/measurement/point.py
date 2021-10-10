"""
point.py
=========

Module that contains the Point classes

"""

from abc import ABC
from enum import Enum, auto


class PointType(Enum):
    APPROXIMATE = auto()
    FIXED = auto()


class Point(ABC):
    def __init__(self, identifier: str, point_type: PointType):
        self.identifier = identifier
        self.point_type = point_type

    def __repr__(self) -> str:
        return f"{self.point_type.name}_Point_{self.identifier}"


class OneDimensionalPoint(Point):
    def __init__(self, identifier: str, point_type: PointType, z: float):
        super().__init__(identifier, point_type)
        self.z = z

    def __repr__(self) -> str:
        sub = super().__repr__()
        return f"{sub}(z: {self.z})"


class TwoDimensionalPoint(Point):
    def __init__(self, identifier: str, point_type: PointType, x: float, y: float):
        super().__init__(identifier, point_type)
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        sub = super().__repr__()
        return f"{sub}(x: {self.x}, y: {self.y})"
