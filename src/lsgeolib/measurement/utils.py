import math
from typing import Type

from .point import Point


class OrientationAngle:
    def __init__(self):
        self._orientation_angles = []
        self.average_orientation_angle = 0.0

    def add_orientation_angle(self, orientation_angle):
        self._orientation_angles.append(orientation_angle)
        self.average_orientation_angle = sum(self._orientation_angles) / len(
            self._orientation_angles
        )


class Azimuth:
    def __init__(self, point_from, point_to):
        self.point_from: Type[Point] = point_from
        self.point_to: Type[Point] = point_to
        self.azimuth: float = 0

        self.dx = point_to.x - point_from.x
        self.dy = point_to.y - point_from.y
        self.calculate_azimuth()

    def calculate_azimuth(self) -> float:
        if self.dx > 0 > self.dy:
            self.azimuth = math.degrees(math.atan(self.dx / self.dy)) + 180
        elif self.dx < 0 > self.dy:
            self.azimuth = math.degrees(math.atan(self.dx / self.dy)) + 180
        elif self.dx < 0 < self.dy:
            self.azimuth = math.degrees(math.atan(self.dx / self.dy)) + 360
        elif self.dy == 0 < self.dx:
            self.azimuth = 90
        elif self.dy == 0 > self.dx:
            self.azimuth = 270
        elif self.dx == 0 > self.dy:
            self.azimuth = 180
        elif self.dx == 0 < self.dy:
            self.azimuth = 0
        elif self.dx > 0 < self.dy:
            self.azimuth = math.degrees(math.atan(self.dx / self.dy))
        return self.azimuth
