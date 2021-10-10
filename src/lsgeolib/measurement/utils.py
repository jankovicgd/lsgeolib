"""
utils.py
=========

Contains useful utility classes and methods

"""

import math
from typing import List

from .point import TwoDimensionalPoint


class OrientationAngles:
    def __init__(self) -> None:
        self.orientation_angles: List[float] = []

    def add_orientation_angle(self, orientation_angle: float) -> None:
        self.orientation_angles.append(orientation_angle)

    @property
    def average_orientation_angle(self) -> float:
        return sum(self.orientation_angles) / len(self.orientation_angles)


class Azimuth:
    def __init__(self, point_from: TwoDimensionalPoint, point_to: TwoDimensionalPoint):
        self.point_from = point_from
        self.point_to = point_to

    def __repr__(self) -> str:
        return f"Azimuth_{self.point_from.identifier}_{self.point_to.identifier}({self.azimuth})"

    @property
    def azimuth(self) -> float:
        dx = self.point_to.x - self.point_from.x
        dy = self.point_to.y - self.point_from.y

        if dx > 0 > dy:
            azimuth = math.degrees(math.atan(dx / dy)) + 180
        elif dx < 0 > dy:
            azimuth = math.degrees(math.atan(dx / dy)) + 180
        elif dx < 0 < dy:
            azimuth = math.degrees(math.atan(dx / dy)) + 360
        elif dy == 0 < dx:
            azimuth = 90
        elif dy == 0 > dx:
            azimuth = 270
        elif dx == 0 > dy:
            azimuth = 180
        elif dx == 0 < dy:
            azimuth = 0
        elif dx > 0 < dy:
            azimuth = math.degrees(math.atan(dx / dy))

        return azimuth
