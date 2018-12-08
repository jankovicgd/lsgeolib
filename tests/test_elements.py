"""This is the docstring for test_element"""

# -*- coding: utf-8 -*-

import math
import pytest
from lsgeonetadj.skeleton import fib
from lsgeonetadj.element.point import Point
from lsgeonetadj.element.line import Line
from lsgeonetadj.element.angle import Angle


__author__ = "jankovic_gd"
__copyright__ = "jankovic_gd"
__license__ = "mit"


def test_fib():
    """Docstring"""
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)

def test_calculate_approximate_distance():
    """Docstring"""
    p1 = Point(p_id=1, x=10.0, y=20.0)
    p2 = Point(p_id=2, x=20.0, y=10.0)
    l1 = Line(p1, p2)
    assert l1.calculate_approximate_distance() == 10 * math.sqrt(2)

def test_calculate_approximate_angle():
    """Docstring"""
    p1 = Point(p_id=1, x=10.0, y=20.0)
    p2 = Point(p_id=2, x=20.0, y=10.0)
    p3 = Point(p_id=3, x=30.0, y=30.0)
    l1 = Line(p1, p2, m_dir=60)
    l2 = Line(p2, p3, m_dir=80)
    a1 = Angle(l1, l2)
    assert a1.calculate_approximate_angle_direction() == 20

def test_calculate_approximate_azimuth():
    """Docstring"""
    p1 = Point(p_id=1, x=10.0, y=10.0)
    p2 = Point(p_id=2, x=20.0, y=20.0)
    p3 = Point(p_id=3, x=30.0, y=10.0)
    l1 = Line(p1, p2)
    l2 = Line(p2, p3)
    l3 = Line(p2, p1)
    l4 = Line(p3, p2)
    assert l1.calculate_approximate_azimuth() == 45.0
    assert l2.calculate_approximate_azimuth() == 135.0
    assert l3.calculate_approximate_azimuth() == 225.0
    assert l4.calculate_approximate_azimuth() == 315.0

def test_points_equal():
    """Docstring"""
    p1 = Point(p_id=1, x=10.0, y=10.0)
    p2 = Point(p_id=2, x=10.0, y=10.0)
    p3 = Point(p_id=3, x=20.0, y=10.0)
    assert p1.__eq__(p2)
    assert not p1.__eq__(p3)

def test_calculate_approximate_angle_azimuth():
    """Docstring"""
    p1 = Point(p_id=1, x=20.0, y=20.0)
    p2 = Point(p_id=2, x=10.0, y=10.0)
    p3 = Point(p_id=3, x=20.0, y=10.0)
    l1 = Line(p2, p1)
    l2 = Line(p2, p3)
    a1 = Angle(l1, l2)
    assert a1.calculate_approximate_angle_azimuth() == 45
