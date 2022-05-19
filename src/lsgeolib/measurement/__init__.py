from typing import Dict, List, Type

from .abc import Measurement, Point, Standard
from .point import OneDimensionalPoint, TwoDimensionalPoint
from .distance import Distance, FixedVariableStandard
from .direction import Direction, AngularSecondsStandard
from .height_difference import HeightDifference, HeightDifferenceStandard
from .angle import Angle
from .utils import OrientationAngles, Azimuth
from ..globals import MeasurementType, StandardType
from ..config import MeasurementModel, PointModel, StandardModel

MEASUREMENT_MAP: Dict[MeasurementType, Type[Measurement]] = {
    MeasurementType.ANGLE: Angle,
    MeasurementType.DIRECTION: Direction,
    MeasurementType.DISTANCE: Distance,
    MeasurementType.HEIGHT_DIFFERENCE: HeightDifference,
}

STANDARD_MAP: Dict[StandardType, Type[Standard]] = {
    StandardType.FIXED_VARIABLE_DISTANCE: FixedVariableStandard,
    StandardType.ANGULAR_SECONDS: AngularSecondsStandard,
    StandardType.HEIGHT_DIFFERENCE: HeightDifferenceStandard,
}


def standard_config_factory(standard_cfg: StandardModel) -> Standard:
    StandardClass = STANDARD_MAP[standard_cfg.type]
    return StandardClass(standard_cfg.value)


def measurement_config_factory(
    measurement_cfg: MeasurementModel, points: List[Point]
) -> Measurement:
    standard = standard_config_factory(measurement_cfg.standard)
    point_from = next((p for p in points if p.identifier == measurement_cfg.point_from))
    point_to = next((p for p in points if p.identifier == measurement_cfg.point_to))
    point_base = None
    if measurement_cfg.point_base:
        point_base = next(
            (p for p in points if p.identifier == measurement_cfg.point_base)
        )

    MeasurementClass = MEASUREMENT_MAP[measurement_cfg.type]

    return MeasurementClass(
        point_from=point_from,
        point_to=point_to,
        point_base=point_base,
        standard=standard,
        measured=measurement_cfg.measured,
    )


def point_config_factory(point_cfg: PointModel) -> Point:
    if point_cfg.x is not None and point_cfg.y is not None:
        return TwoDimensionalPoint(
            identifier=point_cfg.identifier,
            type=point_cfg.type,
            x=point_cfg.x,
            y=point_cfg.y,
        )

    if point_cfg.z is not None:
        return OneDimensionalPoint(
            identifier=point_cfg.identifier, type=point_cfg.type, z=point_cfg.z
        )

    raise ValueError("Cannot resolve point")


__all__ = [
    "Measurement",
    "Point",
    "OneDimensionalPoint",
    "TwoDimensionalPoint",
    "Distance",
    "Direction",
    "HeightDifference",
    "Angle",
    "OrientationAngles",
    "Azimuth",
]
