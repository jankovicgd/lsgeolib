"""
measurement.py
===============

Provides abstract interface for measurements and standards to extend
"""


from abc import abstractmethod, ABC
from typing import Any, Dict, Tuple

from ..globals import PointType


class Point(ABC):
    coords: int

    def __init__(self, identifier: str, point_type: PointType):
        self.identifier = identifier
        self.point_type = point_type

    def __repr__(self) -> str:
        return f"{self.point_type.name}_Point_{self.identifier}"


class Standard(ABC):
    def __init__(self, value: str):
        self.value = value

    @abstractmethod
    def compute_weight_p(self, measurement: "Measurement") -> float:
        ...


class NullStandard(Standard):
    def compute_weight_p(self, measurement: "Measurement") -> float:
        return float(self.value)


class Measurement(ABC):
    """Abstract class for measurements

    Args:
        ABC ([type]): [description]
    """

    def __init__(
        self, measured: float, standard: Standard, *args: Any, **kwargs: Any
    ) -> None:
        self.measured = measured
        self.standard = standard

    @property
    def measured(self) -> float:
        return self._measured

    @measured.setter
    def measured(self, value: float) -> None:
        self._measured = value

    @property
    @abstractmethod
    def approximate(self) -> float:
        ...

    @property
    @abstractmethod
    def adjusted(self) -> float:
        ...

    @property
    @abstractmethod
    def free_value(self) -> float:
        ...

    @property
    @abstractmethod
    def coefficients(self) -> Dict[Tuple[str, Point], float]:
        ...
