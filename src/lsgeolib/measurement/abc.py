"""
measurement.py
===============

Provides abstract interface for measurements to extend
"""


from abc import abstractmethod, ABC
from typing import Dict, Tuple
from enum import Enum, auto


class PointType(Enum):
    APPROXIMATE = auto()
    FIXED = auto()


class Point(ABC):
    def __init__(self, identifier: str, point_type: PointType):
        self.identifier = identifier
        self.point_type = point_type

    def __repr__(self) -> str:
        return f"{self.point_type.name}_Point_{self.identifier}"


class Measurement(ABC):
    """Abstract class for measurements

    Args:
        ABC ([type]): [description]
    """

    def __init__(self, measured: float) -> None:
        self.measured = measured

    @property
    def measured(self) -> float:
        return self._measured

    @measured.setter
    def measured(self, value: float) -> None:
        self._measured = value

    @property
    @abstractmethod
    def approximate(self) -> float:
        """raise NotImplementedError"""

    @property
    @abstractmethod
    def adjusted(self) -> float:
        """raise NotImplementedError"""

    @property
    @abstractmethod
    def free_value(self) -> float:
        """raise NotImplementedError"""

    @property
    @abstractmethod
    def coefficients(self) -> Dict[Tuple[str, Point], float]:
        """raise NotImplementedError"""
