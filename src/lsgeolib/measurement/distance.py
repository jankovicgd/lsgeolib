import math
from .point import Point
from .measurement import Measurement


class Distance(Measurement):
    def __init__(
        self, point_from: Point, point_to: Point, measured: float,
    ):
        super().__init__(point_from, point_to, measured)

    def calculate_approximate(self) -> float:
        self.approximate = math.sqrt(self.dx ** 2 + self.dy ** 2)
        return self.approximate

    def calculate_adjusted(self) -> float:
        pass

    @property
    def measured(self):
        return self._measured

    @measured.setter
    def measured(self, value):
        if value < 0:
            raise ValueError("Distance measurements cannot be negative")

        self._measured = float(value)
