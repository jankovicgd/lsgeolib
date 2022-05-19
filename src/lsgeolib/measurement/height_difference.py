"""

height_difference.py
=====================
"""

from typing import Any, Dict, Tuple
from dataclasses import dataclass

from .abc import Measurement, Standard, NullStandard, Point
from .point import OneDimensionalPoint
from ..globals import PointType


@dataclass
class HeightDifference(Measurement):
    """Measurement where the difference in height is measured between two points

    Attributes:
        point_from (OneDimensionalPoint): Point from which the measurement is taken.
        point_to (OneDimensionalPoint): Point to which the measurement is taken.
        measured (float): Measured height difference
    """

    def __init__(
        self,
        point_from: OneDimensionalPoint,
        point_to: OneDimensionalPoint,
        measured: float,
        standard: Standard = NullStandard("1.0"),
        *args: Any,
        **kwargs: Any,
    ) -> None:
        self.point_from = point_from
        self.point_to = point_to

        super().__init__(measured, standard)

    @property
    def approximate(self) -> float:
        return self.point_to.z - self.point_from.z

    @property
    def adjusted(self) -> float:
        pass

    @property
    def coefficients(self) -> Dict[Tuple[str, Point], float]:
        a_from_to = -1.0
        a_to_from = 1.0

        coefficients: Dict[Tuple[str, Point], float] = {}

        if self.point_from.point_type == PointType.APPROXIMATE:
            coefficients[("a", self.point_from)] = a_from_to

        if self.point_to.point_type == PointType.APPROXIMATE:
            coefficients[("a", self.point_to)] = a_to_from

        return coefficients

    @property
    def free_value(self) -> float:
        return self.approximate - self.measured


class HeightDifferenceStandard(Standard):
    def compute_weight_p(self, measurement: Measurement) -> float:
        return float(1 / float(self.value))
