"""
distance.py
============

Contains class for distance measurement
"""

import math
from typing import Any, Tuple, Dict

from .point import TwoDimensionalPoint
from .abc import Measurement, Point, Standard, NullStandard
from ..globals import PointType


class Distance(Measurement):
    """Distance class that represents a measurement of length between two points.

    Attributes:
        point_from (TwoDimensionalPoint): Point from which the measurement is taken.
        point_to (TwoDimensionalPoint): Point to which the measurement is taken.
        measured (float): Measured distance
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

        super().__init__(measured, standard)

    @property
    def measured(self) -> float:
        return self._measured

    @measured.setter
    def measured(self, value: float) -> None:
        if value < 0:
            raise ValueError(f"Distance measured: {value}, cannot be negative")

        self._measured = value

    @property
    def approximate(self) -> float:
        dx = self.point_to.x - self.point_from.x
        dy = self.point_to.y - self.point_from.y
        return math.sqrt(dx ** 2 + dy ** 2)

    @property
    def adjusted(self) -> float:
        pass

    @property
    def free_value(self) -> float:
        return self.approximate - self.measured

    @property
    def coefficients(self) -> Dict[Tuple[str, Point], float]:
        a_from_to = -(self.point_to.x - self.point_from.x) / self.approximate
        a_to_from = -a_from_to
        b_from_to = -(self.point_to.y - self.point_from.y) / self.approximate
        b_to_from = -b_from_to

        coefficients: Dict[Tuple[str, Point], float] = {}
        if self.point_from.point_type == PointType.APPROXIMATE:
            coefficients[("a", self.point_from)] = a_from_to
            coefficients[("b", self.point_from)] = b_from_to
        if self.point_to.point_type == PointType.APPROXIMATE:
            coefficients[("a", self.point_to)] = a_to_from
            coefficients[("b", self.point_to)] = b_to_from

        return coefficients


class FixedVariableStandard(Standard):
    def compute_weight_p(self, measurement: "Measurement") -> float:
        values = self.value.split("+")
        fixed_part = float(values[0])
        variable_part = float(values[1])

        return 1 / float(fixed_part + variable_part * measurement.measured / 1000)
