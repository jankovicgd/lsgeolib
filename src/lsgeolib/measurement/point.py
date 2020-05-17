"""Module that contains the Point class and its relevant methods"""


class Point:
    """Point class that represents a 0 dimensional entity with 3 spatial coordinates.
    In least square terms each point can be:
     * fixed - coordinates of the point cannot change
     * approximate - coordinates of the point are an unknown and will be adjusted

    Attributes:
        p_id (str): id of the point.
        x (double): x coordinate of point.
        y (double): y coordinate of point.
        z (double, optional): z coordinate of point, also height of point.
    """

    def __init__(
        self, identifier: str, x: float = 0.0, y: float = 0.0, z: float = 0.0,
    ):
        self.id = str(identifier)
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __repr__(self):
        return f"Point_{self.id}(x: {self.x}, y: {self.y}, z: {self.z})"


class FixedPoint(Point):
    pass


class ApproximatePoint(Point):
    def calculate_adjusted_coordinates(self):
        pass
