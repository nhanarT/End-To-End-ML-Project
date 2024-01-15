from ml_project.config import ConfigurationManager
from ml_project.components import DataValidation

import logging

logger = logging.getLogger("ml_project.pipeline.data_validation")

STAGE_NAME = "Data Validation"


class DataValidationPipeline:
    def __init__(self) -> None:
        pass

    def execute(self) -> None:
        conf_manager = ConfigurationManager()
        data_validation_conf = conf_manager.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_conf)
        data_validation.execute()


if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME} started >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        pipeline = DataValidationPipeline()
        pipeline.execute()
        logger.info(f"{STAGE_NAME} finished <<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    except BaseException as e:
        logger.error(f"Encountered error during {STAGE_NAME}")
        logger.exception(e)
        raise e
