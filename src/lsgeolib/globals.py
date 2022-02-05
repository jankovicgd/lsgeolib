from enum import Enum, auto


class PointType(Enum):
    APPROXIMATE = auto()
    FIXED = auto()


class StandardType(Enum):
    ANGULAR_SECONDS = auto()
    FIXED_VARIABLE_DISTANCE = auto()
    HEIGHT_DIFFERENCE = auto()
