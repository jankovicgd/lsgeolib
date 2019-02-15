"""Module docstring"""

class Point():
    """Point class that represents a 0 dimensional entity with 3 spatial coordinates

    Attributes:
        id (str): id of the point.
        x (double): x coordinate of point.
        y (double): y coordinate of point.
        z (double, optional): z coordinate of point, also height of point.
    """
    def __init__(self, p_id, x, y, z=None):
        super(Point, self).__init__()
        self.p_id = p_id
        self.x = float(x)
        self.y = float(y)
        if z:
            self.z = float(z)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            if hasattr(self, 'z') and hasattr(other, 'z'):
                if self.z == other.z:
                    return True
                return False
            return True
        return False

    def print_point(self):
        """Docstring"""
        print("X: " + str(self.x) + ", Y: " + str(self.y) + ", Z: " + str(self.z))
