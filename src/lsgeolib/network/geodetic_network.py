"""Module Docstring"""
import yaml
import pandas as pd

from lsgeolib.model.functional import (
    direction_eq,
    angle_eq,
    oriented_angle_eq,
    distance_eq,
    height_dif_eq,
)
from lsgeolib.network.utils import check_directions


class GeodeticNetwork:
    """docstring for GeodeticNetwork."""

    def __init__(self):
        super(GeodeticNetwork, self).__init__()
        self.measurements = None
        self.covariances = None
