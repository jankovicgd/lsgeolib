import math
from typing import Tuple, Dict

from .abc import Measurement
from .point import Point, TwoDimensionalPoint, PointType
from .utils import Azimuth
from .distance import Distance


class Angle(Measurement):
    def __init__(
        self,
        point_from: TwoDimensionalPoint,
        point_to: TwoDimensionalPoint,
        point_base: TwoDimensionalPoint,
        measured: float,
    ):
        self.point_from = point_from
        self.point_to = point_to
        self.point_base = point_base
        self.azimuth_base_from = Azimuth(point_base, point_from)
        self.azimuth_base_to = Azimuth(point_base, point_to)
        super().__init__(measured)

    @property
    def measured(self) -> float:
        return self._measured

    @measured.setter
    def measured(self, value: float) -> None:
        if value < 0:
            raise ValueError(f"Angle measured: {value}, cannot be negative")
        self._measured = value

    @property
    def approximate(self) -> float:
        return self.azimuth_base_to.azimuth - self.azimuth_base_from.azimuth

    @property
    def adjusted(self) -> float:
        pass

    @property
    def coefficients(self) -> Dict[Tuple[str, Point], float]:
        distance_base_from = Distance(self.point_base, self.point_from, 0).approximate
        distance_base_to = Distance(self.point_base, self.point_to, 0).approximate

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

        coefficients: Dict[Tuple[str, Point], float] = {}

        if self.point_from.point_type == PointType.APPROXIMATE:
            coefficients[("a", self.point_from)] = -a_from_base
            coefficients[("b", self.point_from)] = -b_from_base
        if self.point_to.point_type == PointType.APPROXIMATE:
            coefficients[("a", self.point_to)] = a_to_base
            coefficients[("b", self.point_to)] = b_to_base
        if self.point_base.point_type == PointType.APPROXIMATE:
            coefficients[("a", self.point_base)] = a_base_to - a_base_from
            coefficients[("b", self.point_base)] = b_base_to - b_base_from

        return coefficients

    @property
    def free_value(self) -> float:
        return self.approximate - self.measured
