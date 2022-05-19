from dataclasses import dataclass
from typing import List, Optional, cast

from omegaconf import OmegaConf

from .globals import PointType, MeasurementType, StandardType


@dataclass
class StandardModel:
    type: StandardType
    value: str


@dataclass
class PointModel:
    identifier: str
    type: PointType
    x: Optional[float] = None
    y: Optional[float] = None
    z: Optional[float] = None


@dataclass
class MeasurementModel:
    point_from: str
    point_to: str
    measured: float
    standard: StandardModel
    type: MeasurementType
    point_base: Optional[str] = None


@dataclass
class ConfigurationModel:
    points: List[PointModel]
    measurements: List[MeasurementModel]


def load_config(configuration_path: str) -> ConfigurationModel:
    """Load the configuration as a structured config

    Args:
        configuration_path (str): File path to configuration

    Returns:
        PreprocessorConfig: Structured configuration
    """

    return cast(
        ConfigurationModel,
        OmegaConf.merge(
            OmegaConf.structured(ConfigurationModel), OmegaConf.load(configuration_path)
        ),
    )
