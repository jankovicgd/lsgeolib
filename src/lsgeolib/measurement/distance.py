import math
from .point import Point, ApproximatePoint, FixedPoint
from .measurement import Measurement

from typing import Type, Dict


class Distance(Measurement):
    """Distance class that represents a measurement of length between two points.

    Attributes:
        point_from (Point): Point from which the measurement is taken.
        point_to (Point): Point to which the measurement is taken.
        measured (float): Measured distance
    """

    def __init__(
        self, point_from: Type[Point], point_to: Type[Point], measured: float,
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

    def calculate_approximate(self, *args, **kwargs) -> float:
        self.approximate = math.sqrt(self.dx ** 2 + self.dy ** 2)
        return self.approximate

    def calculate_adjusted(self) -> float:
        pass

    def calculate_free_value(self) -> float:
        self.free_value = self.approximate - self.measured
        return self.free_value

    def calculate_coefficients(self) -> Dict[str, float]:
        a_from_to = -(self.point_to.x - self.point_from.x) / self.approximate
        a_to_from = -a_from_to
        b_from_to = -(self.point_to.y - self.point_from.y) / self.approximate
        b_to_from = -b_from_to

        self.coefficients = {
            f"a_{self.point_from.id}": a_from_to,
            f"b_{self.point_from.id}": b_from_to,
            f"a_{self.point_to.id}": a_to_from,
            f"b_{self.point_to.id}": b_to_from,
        }

        self.pop_coefficients()

        return self.coefficients
