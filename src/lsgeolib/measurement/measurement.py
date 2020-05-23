from .point import Point
from abc import abstractmethod, abstractproperty, ABCMeta
from typing import Type, Dict


class Measurement(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(
        self,
        point_from: Type[Point],
        point_to: Type[Point],
        measured: float,
        point_base: Type[Point] = None,
    ):
        # Known values
        self.point_from = point_from
        self.point_to = point_to
        self.measured = measured
        self.point_base = point_base

        # Computed values
        self.approximate: float = None
        self.adjusted: float = None
        self.free_value: float = None
        self.coefficients = dict()

        if not point_base:
            self.dx = point_to.x - point_from.x
            self.dy = point_to.y - point_from.y

    def __repr__(self) -> str:
        """Representation function for measurements"""
        if not self.point_base:
            return f"{type(self).__name__}_{self.point_from.id}-{self.point_to.id}({self.measured})"

        return f"{type(self).__name__}_{self.point_from.id}-{self.point_base.id}-{self.point_to.id}({self.measured})"

    @abstractproperty
    def measured(self):
        raise NotImplementedError

    @abstractmethod
    def calculate_approximate(self, *args, **kwargs) -> float:
        raise NotImplementedError

    @abstractmethod
    def calculate_adjusted(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def calculate_free_value(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def calculate_coefficients(self) -> Dict[str, float]:
        raise NotImplementedError

    # def __eq__(self, other: Point) -> bool:
    #     return self.x == other.x and self.y == other.y and self.z == other.z
