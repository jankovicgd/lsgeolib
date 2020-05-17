from .point import Point
from abc import abstractmethod, abstractproperty, ABCMeta


class Measurement(object):
    __metaclass__ = ABCMeta

    def __init__(
        self,
        point_from: Point,
        point_to: Point,
        measured: float,
        point_base: Point = None,
    ):
        self.point_from = point_from
        self.point_to = point_to
        self.measured = measured
        self.point_base = point_base
        self.approximate = None
        self.adjusted = None
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
    def calculate_approximate(self):
        raise NotImplementedError

    @abstractmethod
    def calculate_adjusted(self):
        raise NotImplementedError

    # def __eq__(self, other: Point) -> bool:
    #     return self.x == other.x and self.y == other.y and self.z == other.z
