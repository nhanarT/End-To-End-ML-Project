import os
from dotenv import load_dotenv

from ml_project.constants import *
from ml_project.utils import read_yaml, create_dirs
from ml_project.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    TrainingModelConfig,
    ModelEvaluationConfig,
)


class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH,
        schema_filepath=SCHEMA_FILE_PATH,
    ) -> None:
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_dirs([self.config.artifact_root])
        load_dotenv('.env', override=True)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        data_ingestion_config = DataIngestionConfig(
            stage_dir=config.stage_dir,
            source=config.source,
            dest=config.dest,
            unzip_dir=config.unzip_dir,
        )

        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.columns

        data_validation_config = DataValidationConfig(
            stage_dir=config.stage_dir,
            data_dir=config.data_dir,
            validation_result_file=config.validation_result_file,
            data_schema=schema,
        )

        return data_validation_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        params = self.params.DATA_TRANSFORMATION
        target = self.schema.target.name

        data_transformation_config = DataTransformationConfig(
            stage_dir=config.stage_dir,
            data_dir=config.data_dir,
            test_size=params.TEST_SIZE,
            stratify=params.STRATIFY,
            target=target
        )

        return data_transformation_config

    def get_training_model_config(self) -> TrainingModelConfig:
        config = self.config.training_model
        params = self.params.TRAINING_MODEL
        schema = self.schema

        training_model_config = TrainingModelConfig(
            stage_dir=config.stage_dir,
            data_dir=config.data_dir,
            output_dir=config.output_dir,
            schema=schema,
            SEED=params.SEED,
            N_NEIGHBORS=params.N_NEIGHBORS,
            N_ESTIMATORS=params.N_ESTIMATORS,
            DEBUG=DEBUG,
        )

        return training_model_config

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.TRAINING_MODEL
        schema = self.schema

        model_evaluation_config = ModelEvaluationConfig(
            stage_dir = config.stage_dir,
            data_dir = config.data_dir,
            model_dir = config.model_dir,
            model_params = params,
            metric_file_name = config.metric_file_name,
            schema = schema,
            mlflow_uri = os.environ["MLFLOW_TRACKING_URI"],
        )

        return model_evaluation_config
