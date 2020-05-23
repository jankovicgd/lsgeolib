from .point import Point
from .measurement import Measurement
from typing import Type, Dict


class HeightDifference(Measurement):
    def __init__(
        self, point_from: Type[Point], point_to: Type[Point], measured: float,
    ):
        super().__init__(point_from, point_to, measured)

    @property
    def measured(self):
        return self._measured

    @measured.setter
    def measured(self, value):
        self._measured = float(value)

    def calculate_approximate(self, *args, **kwargs) -> float:
        self.approximate = self.point_to.z - self.point_from.z
        return self.approximate

    def calculate_adjusted(self) -> float:
        pass

    def calculate_coefficients(self) -> Dict[str, float]:
        a_from_to = -1
        a_to_from = 1

        self.coefficients = {
            f"a_{self.point_from.id}_{self.point_to.id}": a_from_to,
            f"a_{self.point_to.id}_{self.point_from.id}": a_to_from,
        }

    def calculate_free_value(self) -> float:
        self.free_value = self.approximate - self.measured
        return self.free_value
