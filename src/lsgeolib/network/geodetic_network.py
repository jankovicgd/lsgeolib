"""Module Docstring"""

from abc import ABC, abstractmethod
from typing import List

from ..measurement.abc import Measurement
from ..measurement.point import Point


class GeodeticNetwork(ABC):
    def __init__(self, measurements: List[Measurement], points: List[Point]):
        self.measurements = measurements
        self.points = points

    @abstractmethod
    def adjust(self):
        ...


class TwoDimensionalGeodeticNetwork(GeodeticNetwork):
    pass


class OneDimensionalGeodeticNetwork(GeodeticNetwork):
    pass
