"""Module Docstring"""

from abc import ABC, abstractmethod


class GeodeticNetwork(ABC):
    @abstractmethod
    def adjust(self):
        """"""


class TwoDimensionalGeodeticNetwork(GeodeticNetwork):
    pass


class OneDimensionalGeodeticNetwork(GeodeticNetwork):
    pass
