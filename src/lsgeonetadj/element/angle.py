"""Module docstring"""

import math
from lsgeonetadj.element.line import Line

class Angle():
    """docstring for Angle."""
    def __init__(self, l1, l2, m_ang=None):
        super(Angle, self).__init__()
        assert isinstance(l1, Line)
        assert isinstance(l2, Line)
        self.l1 = l1
        self.l2 = l2
        if m_ang:
            self.m_ang = m_ang

    def calculate_approximate_angle_direction(self):
        """Docstring"""
        assert self.l2.m_dir > self.l1.m_dir
        return self.l2.m_dir - self.l1.m_dir

    def calculate_approximate_angle_azimuth(self):
        """Docstring"""
        assert self.l2.calculate_approximate_azimuth() > self.l1.calculate_approximate_azimuth()
        return self.l2.calculate_approximate_azimuth() - self.l1.calculate_approximate_azimuth()
