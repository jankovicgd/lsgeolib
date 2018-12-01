#!/home/nikola/miniconda3/envs/lsGeoNetAdj/bin/python
# -*- coding: utf-8 -*-

import pytest
from lsgeonetadj.skeleton import fib
from lsgeonetadj.element.Point import Point
from lsgeonetadj.element.Line import Line
from lsgeonetadj.element.Angle import Angle
import math

__author__ = "jankovic_gd"
__copyright__ = "jankovic_gd"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)

def test_calculateApproximate2DDistance():
    p1 = Point(id=1, x=10.0, y=20.0)
    p2 = Point(id=2, x=20.0, y=10.0)
    l1 = Line(p1, p2)
    assert l1.calculateApproximate2DDistance() == 10 * math.sqrt(2)
    # error when impossible to calculate distance
    # with pytest.raises(AssertionError):
    #     l1.calculateDistance()

def test_calculateApproximateAngle():
    p1 = Point(id=1, x=10.0, y=20.0)
    p2 = Point(id=2, x=20.0, y=10.0)
    p3 = Point(id=3, x=30.0, y=30.0)
    l1 = Line(p1, p2, mDir=60)
    l2 = Line(p2, p3, mDir=80)
    a1 = Angle(l1, l2)
    assert a1.calculateApproximateAngle() == 20

def test_calculateApproximateAzimuth():
    p1 = Point(1, 10.0, 10.0)
    p2 = Point(2, 20.0, 20.0)
    p3 = Point(3, 30.0, 10.0)
    l1 = Line(p1, p2)
    l2 = Line(p2, p3)
    l3 = Line(p2, p1)
    l4 = Line(p3, p2)
    assert l1.calculateApproximateAzimuth() == 45.0
    assert l2.calculateApproximateAzimuth() == 135.0
    assert l3.calculateApproximateAzimuth() == 225.0
    assert l4.calculateApproximateAzimuth() == 315.0
