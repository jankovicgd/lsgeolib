from typing import List

from .abc import AbstractGeodeticNetwork
from ..measurement import Measurement, Point


class GeodeticNetwork(AbstractGeodeticNetwork):
    def __init__(self, measurements: List[Measurement], points: List[Point]):
        self.measurements = measurements
        self.points = points

    @classmethod
    def from_yaml(cls, yaml: str) -> "GeodeticNetwork":
        pass


class TwoDimensionalGeodeticNetwork(GeodeticNetwork):
    pass


class OneDimensionalGeodeticNetwork(GeodeticNetwork):
    pass
