from dataclasses import dataclass
from pathlib import Path

from pandas._libs.tslibs import ints_to_pydatetime
from ml_project.utils.common import OmegaConfOutput

StrOrPath = str | Path


@dataclass(frozen=True)
class DataIngestionConfig:
    stage_dir: StrOrPath
    source: StrOrPath
    dest: StrOrPath
    unzip_dir: StrOrPath


@dataclass(frozen=True)
class DataValidationConfig:
    stage_dir: StrOrPath
    data_dir: StrOrPath
    validation_result_file: StrOrPath
    data_schema: OmegaConfOutput


@dataclass(frozen=True)
class DataTransformationConfig:
    stage_dir: StrOrPath
    data_dir: StrOrPath
    test_size: float
    stratify: bool
    target: str


@dataclass(frozen=True)
class TrainingModelConfig:
    stage_dir: StrOrPath
    data_dir: StrOrPath
    output_dir: StrOrPath
    schema: OmegaConfOutput
    SEED: int
    N_NEIGHBORS: int
    N_ESTIMATORS: int
    DEBUG: bool


@dataclass(frozen=True)
class ModelEvaluationConfig:
    stage_dir: StrOrPath
    data_dir: StrOrPath
    model_dir: StrOrPath
    model_params: OmegaConfOutput
    metric_file_name: StrOrPath
    schema: OmegaConfOutput
    mlflow_uri: str
