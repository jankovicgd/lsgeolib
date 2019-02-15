"""Module docstring"""

class Point():
    """Point class that represents a 0 dimensional entity with 3 spatial coordinates

    Attributes:
        id (str): id of the point.
        x (double): x coordinate of point.
        y (double): y coordinate of point.
        z (double, optional): z coordinate of point, also height of point.
    """
    def __init__(self, p_id, x=0, y=0, z=0):
        super(Point, self).__init__()
        self.p_id = p_id
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __eq__(self, other):
        return self.x == other.x and \
            self.y == other.y and \
            self.z == other.z

    def __str__(self):
        """Representation function"""
        return 'Point_{}({}, {}, {})'.format(self.p_id, self.x, self.y, self.z)
