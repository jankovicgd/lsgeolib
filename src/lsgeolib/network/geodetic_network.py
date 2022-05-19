from typing import List, Tuple

import numpy as np

from lsgeolib.globals import PointType

from .abc import AbstractGeodeticNetwork
from ..measurement import (
    Measurement,
    Point,
    Direction,
    point_config_factory,
    measurement_config_factory,
)
from ..config import load_config


class GeodeticNetwork(AbstractGeodeticNetwork):
    def __init__(self, measurements: List[Measurement], points: List[Point]) -> None:
        self.measurements = measurements
        self.points = points

        self.f = None
        self.A = None
        self.P = None

    @classmethod
    def from_yaml(cls, yaml_path: str) -> "GeodeticNetwork":
        config = load_config(yaml_path)

        points = [point_config_factory(point) for point in config.points]
        measurements = [
            measurement_config_factory(measurement, points)
            for measurement in config.measurements
        ]

        return cls(measurements, points)

    def add_measurement(self, measurement: Measurement) -> None:
        self.measurements.append(measurement)

    def add_point(self, point: Point) -> None:
        self.points.append(point)

    def shape(self) -> Tuple[int, int]:
        rows = len(self.measurements)
        cols = sum(
            [p.coords for p in self.points if p.point_type == PointType.APPROXIMATE]
        )

        if any(
            [False if isinstance(m, Direction) else True for m in self.measurements]
        ):
            cols += 1

        return (rows, cols)

    def arrange_A(self) -> None:
        pass

    def arrange_f(self) -> None:
        shape = (1, len(self.measurements))
        self.f = np.zeros(shape)

        for i, measurement in enumerate(self.measurements):
            self.f[i] = measurement.free_value


class TwoDimensionalGeodeticNetwork(GeodeticNetwork):
    def adjust(self) -> None:
        pass


class OneDimensionalGeodeticNetwork(GeodeticNetwork):
    pass
