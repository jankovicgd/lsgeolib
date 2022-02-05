"""Module Docstring"""

from abc import ABC, abstractmethod


class AbstractGeodeticNetwork(ABC):
    @abstractmethod
    def adjust(self) -> None:
        ...
