"""Module Docstring"""

import math
from lsgeonetadj.element.point import Point

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
    def __init__(self, p1, p2, m_dist=None, m_dir=None, m_dh=None, m_azi=None):
        super(Line, self).__init__()
        assert isinstance(p1, Point)
        assert isinstance(p2, Point)
        self.p1 = p1
        self.p2 = p2
        if m_dist:
            self.m_dist = float(m_dist)
        if m_dir:
            self.m_dir = float(m_dir)
        if m_dh:
            self.m_dh = float(m_dh)
        if m_azi:    
            self.m_azi = float(m_azi)
        self.dx = p2.x - p1.x
        self.dy = p2.y - p1.y

    def calculate_approximate_distance(self):
        """Docstring"""
        setattr(self, 'a_dist', math.sqrt(self.dx**2 + self.dy**2))
        return self.a_dist # noqa pylint: disable=E1101

    def calculate_approximate_azimuth(self):
        """Docstring"""
        if self.dx > 0 > self.dy:
            setattr(self, 'a_azi', math.degrees(math.atan(self.dx/self.dy)) + 180)
            return self.a_azi # noqa pylint: disable=E1101
        if self.dx < 0 > self.dy:
            setattr(self, 'a_azi', math.degrees(math.atan(self.dx/self.dy)) + 180)
            return self.a_azi # noqa pylint: disable=E1101
        if self.dx < 0 < self.dy:
            setattr(self, 'a_azi', math.degrees(math.atan(self.dx/self.dy)) + 360)
            return self.a_azi # noqa pylint: disable=E1101
        if self.dy == 0 < self.dx:
            setattr(self, 'a_azi', 90)
            return self.a_azi # noqa pylint: disable=E1101
        if self.dy == 0 > self.dx:
            setattr(self, 'a_azi', 270)
            return self.a_azi # noqa pylint: disable=E1101
        if self.dx == 0 > self.dy:
            setattr(self, 'a_azi', 180)
            return self.a_azi # noqa pylint: disable=E1101
        if self.dx == 0 < self.dy:
            setattr(self, 'a_azi', 0)
            return self.a_azi # noqa pylint: disable=E1101
        return math.degrees(math.atan(self.dx/self.dy))

    def calculate_approximate_height_difference(self):
        """Docstring"""
        setattr(self, 'a_dh', self.p2.z - self.p1.z)
        return self.a_dh # noqa pylint: disable=E1101

    def calculate_approximate_orientation(self):
        """Docstring"""
        orientation = self.m_dir - self.calculate_approximate_azimuth()
        if orientation < 0:
            setattr(self, 'ori', orientation + 360)
            return self.ori # noqa pylint: disable=E1101
        setattr(self, 'ori', orientation)
        return self.ori # noqa pylint: disable=E1101

    def calculate_approximate_direction(self, avg_orientation):
        """Docstring"""
        setattr(self, 'a_dir', self.calculate_approximate_azimuth() + avg_orientation)
        return self.a_dir # noqa pylint: disable=E1101
