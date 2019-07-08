"""Module Docstring"""
import yaml
import pandas as pd

from lsgeonetadj.model.functional import direction_eq, \
    angle_eq, oriented_angle_eq, distance_eq, height_dif_eq
from lsgeonetadj.network.utils import check_directions

class GeodeticNetwork():
    """docstring for GeodeticNetwork."""
    points = {}
    measurements = {}

    def __init__(self, yml_path):
        super(GeodeticNetwork, self).__init__()
        self.__read_yml(yml_path)
        columns, index = self.__set_headers()
        self.A = pd.DataFrame(columns=columns, index=index)
        self.f = pd.Series(name='f')

    def __set_headers(self):
        """Sets the headers to unknown params and index
        to measurements"""
        columns = []
        for point in self.points:
            if self.points[point]['state'] == 'approximate':
                for coord in self.points[point]:
                    if coord == 'state':
                        continue
                    columns.append('{}.d{}'.format(point, coord))
        index = []
        for measurement_type in self.measurements:
            for measurement in self.measurements[measurement_type]:
                index_str = '{}.{}_{}'.format(
                    measurement,
                    self.measurements[measurement_type][measurement]['from'],
                    self.measurements[measurement_type][measurement]['to'])
                index.append(index_str)
        columns = check_directions(columns, self.points, self.measurements)
        return columns, index

    def __read_yml(self, yml_path):
        """Docstring"""
        with open(yml_path) as f:
            data = yaml.safe_load(f)
        for element in data:
            setattr(self, element, data[element])

    def init_functional(self):
        # TODO
        # if self.measurements['directions']:
        #     direction_eq()
        # if self.measurements['angles']:
        #     angle_eq()
        # if self.measurements['oriented_angles']:
        #     oriented_angle_eq()
        if self.measurements['distances']:
            for distance in self.measurements['distances']:
                a_ij, b_ij, a_ji, b_ji, f = distance_eq()
                self.A.update({distance: [a_ij, b_ij, a_ji, b_ji]})
        # if self.measurements['height_difs']:
        #     height_dif_eq()
        pass

    def init_stochastic(self):
        pass