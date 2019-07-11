"""This is the docstring for test_element"""

# -*- coding: utf-8 -*-

import math
from lsgeonetadj.element.point import Point
from lsgeonetadj.element.line import Line
from lsgeonetadj.element.angle import Angle


__author__ = "jankovic_gd"
__copyright__ = "jankovic_gd"
__license__ = "mit"


p1 = Point(p_id=1, state='approximate', x=10.0, y=20.0)
p2 = Point(p_id=2, state='approximate', x=20.0, y=10.0)
p3 = Point(p_id=3, state='approximate', x=30.0, y=30.0)
p4 = Point(p_id=4, state='approximate', x=10.0, y=10.0, z=10.0)
p5 = Point(p_id=5, state='approximate', x=10.0, y=10.0)
p6 = Point(p_id=6, state='approximate', x=20.0, y=20.0)
l1 = Line(p1, p2, m_dir=60)
l2 = Line(p2, p3, m_dir=80)
l3_1 = Line(p5, p3)
l3_2 = Line(p3, p5)
l4 = Line(p5, p6)
l5 = Line(p5, p2)
a1 = Angle(l1, l2)
a2 = Angle(l4, l5)


def test_calculate_approximate_distance():
    """Test function for Line.calculate_approximate_distance()"""

    test_approximate_distance = l1.calculate_approximate_distance()
    assert test_approximate_distance == 10 * math.sqrt(2)
    # error when impossible to calculate distance
    # with pytest.raises(AssertionError):
    #     l1.calculateDistance()


def test_calculate_approximate_angle():
    """Test function for Angle.calculate_approximate_angle()"""

    test_approximate_angle = a1.calculate_approximate_angle_direction()
    assert test_approximate_angle == 20


def test_calculate_approximate_azimuth():
    """Test function for Line.calculate_approximate_azimuth()"""

    test1_approximate_azimuth = l3_1.calculate_approximate_azimuth()
    test2_approximate_azimuth = l3_2.calculate_approximate_azimuth()
    assert test1_approximate_azimuth == 45.0
    assert test2_approximate_azimuth == 225.0
    # TODO add more cases here


def test_points_equal():
    """Test function for Point.__eq__()"""

    assert p1 == p1
    assert p1 != p3
    assert p4 == p4


def test_calculate_approximate_angle_azimuth():
    """Test function for Angle().calculate_approximate_angle_azimuth"""

    test_approximate_angle_azimuth = a2.calculate_approximate_angle_azimuth()
    assert test_approximate_angle_azimuth == 45
    # TODO add more cases
