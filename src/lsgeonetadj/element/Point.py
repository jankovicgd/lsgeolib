class Point(object):
    """Point class that represents a 0 dimensional entity with 3 spatial coordinates

    Attributes:
        id (str): id of the point.
        x (double): x coordinate of point.
        y (double): y coordinate of point.
        z (double, optional): z coordinate of point.
    """
    def __init__(self, id, x, y, z=None):
        super(Point, self).__init__()
        self.id = id
        self.x = x
        self.y = y
        self.z = z

    def printPoint(self):
        print("X: " + str(self.x) + ", Y: " + str(self.y) + ", Z: " + str(self.z))
