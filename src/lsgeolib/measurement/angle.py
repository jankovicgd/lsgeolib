import math
from typing import Type, Dict

from .measurement import Measurement
from .point import Point, ApproximatePoint, FixedPoint
from .utils import Azimuth
from .distance import Distance


class Angle(Measurement):
    def __init__(
        self,
        point_from: Type[Point],
        point_to: Type[Point],
        point_base: Type[Point],
        measured: float,
    ):
        super(Angle).__init__(point_from, point_to, measured, point_base)
        self.azimuth_base_from = Azimuth(point_base, point_from)
        self.azimuth_base_to = Azimuth(point_base, point_to)

    @property
    def measured(self):
        return self._measured

    @measured.setter
    def measured(self, value):
        # TODO add possibility for converting DMS to float
        if value < 0:
            raise ValueError("Angle measurements cannot be negative")

        self._measured = float(value)

    def calculate_approximate(self, *args, **kwargs) -> float:
        self.approximate = self.azimuth_to.azimuth - self.azimuth_from.azimuth
        return self.approximate

    def calculate_adjusted(self) -> float:
        pass

    def calculate_coefficients(self) -> Dict[str, float]:
        distance_base_from = Distance(
            self.point_base, self.point_from, 0
        ).calculate_approximate()
        distance_base_to = Distance(
            self.point_base, self.point_to, 0
        ).calculate_approximate()

        a_base_from = 206264.806 * (
            math.sin(math.radians(self.azimuth_base_from.azimuth)) / distance_base_from
        )
        a_from_base = -a_base_from
        a_base_to = 206264.806 * (
            math.sin(math.radians(self.azimuth_base_to.azimuth)) / distance_base_to
        )
        a_to_base = -a_base_to

        b_base_from = -206264.806 * (
            math.cos(math.radians(self.azimuth_base_from.azimuth)) / distance_base_from
        )
        b_from_base = -b_base_from
        b_base_to = -206264.806 * (
            math.cos(math.radians(self.azimuth_base_to.azimuth)) / distance_base_to
        )
        b_to_base = -b_base_to

        self.coefficients = {
            f"a_({self.point_base.id}": a_base_to - a_base_from,
            f"b_({self.point_base.id}": b_base_to - b_base_from,
            f"a_{self.point_to.id}": a_to_base,
            f"b_{self.point_to.id}": b_to_base,
            f"a_{self.point_from.id}": -a_from_base,
            f"b_{self.point_from.id}": -b_from_base,
        }

        self.pop_coefficients()

        return self.coefficients

    def calculate_free_value(self) -> float:
        self.free_value = self.approximate - self.measured
