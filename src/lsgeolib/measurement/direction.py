"""
direction.py
============

Contains class for the direction measurement
"""

import math
from typing import Any, Tuple, Dict

from .point import TwoDimensionalPoint
from .abc import Point, Measurement, Standard, NullStandard
from .distance import Distance
from .utils import Azimuth
from ..globals import PointType


class Direction(Measurement):
    """Direction class that represents a measurement of a direction read while measuring
    a point.

    Attributes:
        point_from (Point): Point from which the measurement is taken.
        point_to (Point): Point to which the measurement is taken.
        measured (float): Measured direction
    """

    def __init__(
        self,
        point_from: TwoDimensionalPoint,
        point_to: TwoDimensionalPoint,
        measured: float,
        standard: Standard = NullStandard("1.0"),
        *args: Any,
        **kwargs: Any,
    ):
        self.point_from = point_from
        self.point_to = point_to
        self.azimuth: Azimuth = Azimuth(point_from, point_to)
        super().__init__(measured, standard)

    @property
    def measured(self) -> float:
        return self._measured

    @measured.setter
    def measured(self, value: float) -> None:
        if value < 0:
            raise ValueError(f"Direction measured: {value}, cannot be negative")

        value %= 360

        self._measured = value

    @property
    def average_orientation_angle(self) -> float:
        return self._average_orientation_angle

    @average_orientation_angle.setter
    def average_orientation_angle(self, value: float) -> None:
        self._average_orientation_angle = value

    @property
    def approximate(self) -> float:
        return self.azimuth.azimuth + self.average_orientation_angle

    @property
    def adjusted(self) -> float:
        pass

    @property
    def free_value(self) -> float:
        return self.approximate - self.measured

    @property
    def approximate_orientation_angle(self) -> float:
        approximate_orientation_angle = self.measured - self.azimuth.azimuth

        if approximate_orientation_angle < 0:
            approximate_orientation_angle += 360

        return approximate_orientation_angle

    @property
    def coefficients(self) -> Dict[Tuple[str, Point], float]:

        distance = Distance(self.point_from, self.point_to, 0).approximate

        a_from_to = 206264.806 * (
            math.sin(math.radians(self.azimuth.azimuth)) / distance
        )
        a_to_from = -a_from_to
        b_from_to = -206264.806 * (
            math.cos(math.radians(self.azimuth.azimuth)) / distance
        )
        b_to_from = -b_from_to
        z_coef = 1

        coefficients: Dict[Tuple[str, Point], float] = {}

        if self.point_from.point_type == PointType.APPROXIMATE:
            coefficients[("a", self.point_from)] = a_from_to
            coefficients[("b", self.point_from)] = b_from_to
            coefficients[("z", self.point_from)] = z_coef

        if self.point_to.point_type == PointType.APPROXIMATE:
            coefficients[("a", self.point_to)] = a_to_from
            coefficients[("b", self.point_to)] = b_to_from
            coefficients[("z", self.point_to)] = z_coef

        return coefficients


class AngularSecondsStandard(Standard):
    def compute_weight_p(self, measurement: "Measurement") -> float:
        return 1.0
