import math
from typing import Type, Dict
from .point import Point, ApproximatePoint, FixedPoint
from .measurement import Measurement
from .distance import Distance
from .utils import Azimuth, OrientationAngle


class Direction(Measurement):
    def __init__(self, point_from: Type[Point], point_to: Type[Point], measured: float):
        super().__init__(point_from, point_to, measured)
        self._orientation_angle: OrientationAngle = None
        self.approximate_orientation_angle: float = 0.0
        self.azimuth: Azimuth = Azimuth(point_from, point_to)

    @property
    def measured(self):
        return self._measured

    @measured.setter
    def measured(self, value):
        # TODO add possibility for converting DMS to float
        if value < 0:
            raise ValueError("Direction measurements cannot be negative")

        if value > 360:
            raise ValueError("Direction mesaurements cannot be higher than 360 degrees")

        self._measured = float(value)

    @property
    def orientation_angle(self):
        return self._orientation_angle

    @orientation_angle.setter
    def orientation_angle(self, value):
        self._orientation_angle = value

    def calculate_approximate(self, *args, **kwargs) -> float:
        """Computes the approximate direction using the average orientation
        and approximate azimuth"""

        self.approximate = (
            self.azimuth.azimuth + self._orientation_angle.average_orientation_angle
        )

        return self.approximate

    def calculate_adjusted(self) -> float:
        pass

    def calculate_free_value(self) -> float:
        self.free_value = self.approximate - self.measured

    def calculate_approximate_orientation_angle(self) -> float:
        approximate_orientation_angle = self.measured - self.azimuth.azimuth

        if approximate_orientation_angle < 0:
            approximate_orientation_angle += 360

        self.approximate_orientation_angle = approximate_orientation_angle
        return self.approximate_orientation_angle

    def calculate_coefficients(self) -> Dict["str", "float"]:

        distance = Distance(self.point_from, self.point_to, 0).calculate_approximate()

        a_from_to = 206264.806 * (
            math.sin(math.radians(self.azimuth.azimuth)) / distance
        )
        a_to_from = -a_from_to
        b_from_to = -206264.806 * (
            math.cos(math.radians(self.azimuth.azimuth)) / distance
        )
        b_to_from = -b_from_to
        z_coef = 1

        if isinstance(self.point_from, ApproximatePoint) and isinstance(
            self.point_to, ApproximatePoint
        ):
            self.coefficients = {
                f"a_{self.point_from.id}_{self.point_to.id}": a_from_to,
                f"a_{self.point_to.id}_{self.point_from.id}": a_to_from,
                f"b_{self.point_from.id}_{self.point_to.id}": b_from_to,
                f"b_{self.point_to.id}_{self.point_from.id}": b_to_from,
                f"z_{self.point_from.id}": z_coef,
            }

        if isinstance(self.point_from, ApproximatePoint) and isinstance(
            self.point_to, FixedPoint
        ):
            self.coefficients = {
                f"a_{self.point_from.id}_{self.point_to.id}": a_from_to,
                f"b_{self.point_from.id}_{self.point_to.id}": b_from_to,
                f"z_{self.point_from.id}": z_coef,
            }

        if isinstance(self.point_from, FixedPoint) and isinstance(
            self.point_to, ApproximatePoint
        ):
            self.coefficients = {
                f"a_{self.point_to.id}_{self.point_from.id}": a_to_from,
                f"b_{self.point_to.id}_{self.point_from.id}": b_to_from,
                f"z_{self.point_from.id}": z_coef,
            }

        if isinstance(self.point_from, FixedPoint) and isinstance(
            self.point_to, FixedPoint
        ):
            self.coefficients = {
                f"z_{self.point_from.id}": z_coef,
                f"z_{self.point_to.iz}": z_coef,
            }

        return self.coefficients
