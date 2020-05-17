from .point import Point
from .measurement import Measurement


class HeightDifference(Measurement):
    def __init__(
        self, point_from: Point, point_to: Point, measured: float = 0.0,
    ):
        super().__init__(point_from, point_to, measured)

    def calculate_approximate(self) -> float:
        self.adjusted = self.point_to.z - self.point_from.z
        return self.adjusted

    def calculate_adjusted(self) -> float:
        pass

    @property
    def measured(self):
        return self._measured

    @measured.setter
    def measured(self, value):
        self._measured = float(value)
