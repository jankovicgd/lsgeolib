"""
measurement.py
===============

Provides abstract interface for measurements to extend
"""


from abc import abstractmethod, ABC
from typing import Dict, Tuple

from lsgeolib.measurement.point import Point


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
