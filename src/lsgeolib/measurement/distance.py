import math
from .point import Point
from .measurement import Measurement


class Distance(Measurement):
    def __init__(
        self, point_from: Point, point_to: Point, measured: float,
    ):
        super().__init__(point_from, point_to, measured)

    @property
    def measured(self):
        return self._measured

    @measured.setter
    def measured(self, value):
        if value < 0:
            raise ValueError("Distance measurements cannot be negative")

        self._measured = float(value)

    def calculate_approximate(self) -> float:
        self.approximate = math.sqrt(self.dx ** 2 + self.dy ** 2)
        return self.approximate

    def calculate_adjusted(self) -> float:
        pass

    def calculate_free_value(self) -> float:
        self.free_value = self.approximate - self.measured
        return self.free_value

    def calculate_derivative_coefficients(self) -> dict:
        a_from_to = -(self.point_from.x - self.point_to.x) / self.approximate
        a_to_from = -a_from_to
        b_from_to = -(self.point_from.y - self.point_to.y) / self.approximate
        b_to_from = -b_from_to

        self.derivative_coefficients = {
            f"a_{self.point_from.id}_{self.point_to.id}": a_from_to,
            f"a_{self.point_to.id}_{self.point_from.id}": a_to_from,
            f"b_{self.point_from.id}_{self.point_to.id}": b_from_to,
            f"b_{self.point_to.id}_{self.point_from.id}": b_to_from,
        }

        return self.derivative_coefficients
