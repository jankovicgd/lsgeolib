"""Module Docstring"""

import math
from lsgeonetadj.element import Point


class Line():
    """Line is defined as a 1D element and its measurements are defined as going from p1 to p2

    Measurements on a line for a 1D network are height difference, for a 2D network are distance,
    direction and azimuth.

    Attributes:
        p1 (Point): first point
        p2 (Point): second point
        m_dist (double, optional): distance measured, positive
        m_dir (double, optional): direction measured, positive
        m_dh (double, optional): height difference measured
        m_azi (double, optional): azimuth measured, positive
    """

    def __init__(self, p1: Point, p2: Point, m_dist: float = 0.0, m_dir: float = 0.0,
                 m_dh: float = 0.0, m_azi: float = 0.0):
        super(Line, self).__init__()
        assert isinstance(p1, Point)
        assert isinstance(p2, Point)
        self.p1 = p1
        self.p2 = p2
        self.m_dist = float(m_dist)
        self.m_dir = float(m_dir)
        self.m_dh = float(m_dh)
        self.m_azi = float(m_azi)
        self.dx = p2.x - p1.x
        self.dy = p2.y - p1.y

    def calculate_approximate_distance(self) -> float:
        """Docstring"""
        setattr(self, 'a_dist', math.sqrt(self.dx**2 + self.dy**2))
        return self.a_dist  # noqa pylint: disable=E1101

    def calculate_approximate_azimuth(self) -> float:
        """Docstring"""
        if self.dx > 0 > self.dy:
            setattr(self, 'a_azi', math.degrees(
                math.atan(self.dx/self.dy)) + 180)
        if self.dx < 0 > self.dy:
            setattr(self, 'a_azi', math.degrees(
                math.atan(self.dx/self.dy)) + 180)
        if self.dx < 0 < self.dy:
            setattr(self, 'a_azi', math.degrees(
                math.atan(self.dx/self.dy)) + 360)
        if self.dy == 0 < self.dx:
            setattr(self, 'a_azi', 90)
        if self.dy == 0 > self.dx:
            setattr(self, 'a_azi', 270)
        if self.dx == 0 > self.dy:
            setattr(self, 'a_azi', 180)
        if self.dx == 0 < self.dy:
            setattr(self, 'a_azi', 0)
        if self.dx > 0 < self.dy:
            setattr(self, 'a_azi', math.degrees(math.atan(self.dx/self.dy)))
        return self.a_azi  # noqa pylint: disable=E1101

    def calculate_approximate_height_difference(self) -> float:
        """Docstring"""
        setattr(self, 'a_dh', self.p2.z - self.p1.z)
        return self.a_dh  # noqa pylint: disable=E1101

    def calculate_approximate_orientation(self) -> float:
        """Docstring"""
        orientation = self.m_dir - self.calculate_approximate_azimuth()
        if orientation < 0:
            setattr(self, 'ori', orientation + 360)
            return self.ori  # noqa pylint: disable=E1101
        setattr(self, 'ori', orientation)
        return self.ori  # noqa pylint: disable=E1101

    def calculate_approximate_direction(self, avg_orientation: float) -> float:
        """Computes the approximate direction using the average orientation
        and approximate azimuth"""
        setattr(self, 'a_dir', self.calculate_approximate_azimuth() + avg_orientation)
        return self.a_dir  # noqa pylint: disable=E1101

    def __str__(self):
        """Representation function"""
        return 'Line_{}-{}'.format(self.p1.p_id, self.p2.p_id)
