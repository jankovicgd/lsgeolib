from typing import Type, Dict

from .measurement import Measurement
from .point import Point


class Angle(Measurement):
    def __init__(
        self,
        point_from: Type[Point],
        point_to: Type[Point],
        point_base: Type[Point],
        measured: float,
    ):
        super(Angle).__init__(point_from, point_to, measured, point_base)

    @property
    def measured(self):
        return self._measured

    @measured.setter
    def measured(self, value):
        # TODO add possibility for converting DMS to float
        if value < 0:
            raise ValueError("Angle measurements cannot be negative")

        self._measured = float(value)

    def calculate_approximate(self, *args, **kwargs) -> float:
        pass

    def calculate_adjusted(self) -> float:
        pass

    def calculate_coefficients(self) -> Dict[str, float]:
        pass

    def calculate_free_parameter(self) -> float:
        pass

    # def calculate_approximate_angle_from_direction(self):
    #     """Docstring"""
    #     assert self.l2.m_dir > self.l1.m_dir
    #     return self.l2.m_dir - self.l1.m_dir

    # def calculate_approximate_angle_from_azimuth(self):
    #     """Docstring"""
    #     assert (
    #         self.l2.calculate_approximate_azimuth()
    #         > self.l1.calculate_approximate_azimuth()
    #     )
    #     return (
    #         self.l2.calculate_approximate_azimuth()
    #         - self.l1.calculate_approximate_azimuth()
    #     )
