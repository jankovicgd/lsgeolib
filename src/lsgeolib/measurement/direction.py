import math
from .point import Point
from .measurement import Measurement


class Direction(Measurement):
    def __init__(self, point_from: Point, point_to: Point, measured: float):
        super().__init__(point_from, point_to, measured)
        self.orientation_angle = None
        self.approximate_azimuth = None

    @property
    def measured(self):
        return self._measured

    @measured.setter
    def measured(self, value):
        if value < 0:
            raise ValueError("Direction measurements cannot be negative")

        self._measured = float(value)

    def calculate_approximate(self, **kwargs) -> float:
        """Computes the approximate direction using the average orientation
        and approximate azimuth"""
        average_orientation = kwargs["average_orientation"]
        self.approximate = self.calculate_approximate_azimuth() + average_orientation
        return self.approximate

    def calculate_adjusted(self) -> float:
        pass

    def calculate_free_value(self) -> float:
        self.free_value = self.approximate - self.measured

    def calculate_approximate_azimuth(self) -> float:
        if self.dx > 0 > self.dy:
            self.approximate_azimuth = math.degrees(math.atan(self.dx / self.dy)) + 180
        if self.dx < 0 > self.dy:
            self.approximate_azimuth = math.degrees(math.atan(self.dx / self.dy)) + 180
        if self.dx < 0 < self.dy:
            self.approximate_azimuth = math.degrees(math.atan(self.dx / self.dy)) + 360
        if self.dy == 0 < self.dx:
            self.approximate_azimuth = 90
        if self.dy == 0 > self.dx:
            self.approximate_azimuth = 270
        if self.dx == 0 > self.dy:
            self.approximate_azimuth = 180
        if self.dx == 0 < self.dy:
            self.approximate_azimuth = 0
        if self.dx > 0 < self.dy:
            self.approximate_azimuth = math.degrees(math.atan(self.dx / self.dy))
        return self.approximate_azimuth

    def calculate_approximate_orientation(self) -> float:
        orientation_angle = self.measured - self.calculate_approximate_azimuth()

        if orientation_angle < 0:
            self.orientation_angle = orientation_angle + 360
            return self.orientation_angle

        self.orientation_angle = orientation_angle
        return self.orientation_angle

    def calculate_derrivative_coefficients(self):
        pass
