from lsgeonetadj.element.Line import Line
import math

class Angle(object):
    """docstring for Angle."""
    def __init__(self, l1, l2, mAng=None):
        super(Angle, self).__init__()
        self.l1 = l1
        self.l2 = l2

    def calculateApproximateAngle(self):
        return self.l2.mDir - self.l1.mDir
