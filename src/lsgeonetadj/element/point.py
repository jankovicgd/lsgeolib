"""Module that contains the Point class and its relevant methods"""


class Point():
    """Point class that represents a 0 dimensional entity with 3 spatial coordinates

    Attributes:
        p_id (str): id of the point.
        state ['fixed'|'approximate']: state of point.
        x (double): x coordinate of point.
        y (double): y coordinate of point.
        z (double, optional): z coordinate of point, also height of point.
    """
    states = ['fixed', 'approximate']

    def __init__(self, p_id: str, state: str, x: float = 0.0, y: float = 0.0, z: float = 0):
        super(Point, self).__init__()
        self.p_id = p_id
        if state not in self.states:
            raise TypeError('Point state must be "fixed" or "approximate"')
        self.state = state
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __eq__(self, other) -> bool:
        return self.x == other.x and \
            self.y == other.y and \
            self.z == other.z

    def __str__(self) -> str:
        """Representation function"""
        return 'Point_{}({}, {}, {}, {})'.format(self.p_id, self.x, self.y, self.z, self.state)
