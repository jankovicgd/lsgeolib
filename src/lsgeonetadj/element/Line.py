from lsgeonetadj.element.Point import Point
import math

class Line(object):
    """docstring for Line."""
    def __init__(self, p1, p2, mDist=None, mDir=None):
        super(Line, self).__init__()
        self.p1 = p1
        self.p2 = p2
        self.mDist = mDist
        self.mDir = mDir
        self.dy = p2.y - p1.y
        self.dx = p2.x - p1.x

    def calculateApproximate2DDistance(self):
        return math.sqrt(self.dx**2 + self.dy**2)

    def calculateApproximateAzimuth(self):
        if self.dx > 0 and self.dy < 0:
            return math.degrees(math.atan(self.dx/self.dy) + 180)
        elif self.dx < 0 and self.dy < 0:
            return math.degrees(math.atan(self.dx/self.dy) + 180)
        elif self.dx < 0 and self.dy > 0:
            return math.degrees(math.atan(self.dx/self.dy) + 360)
        else:
            return math.degrees(math.atan(self.dx/self.dy))
