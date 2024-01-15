from ml_project.config import ConfigurationManager
from ml_project.components import DataTransformation

import logging

logger = logging.getLogger("ml_project.pipeline.data_transformation")

STAGE_NAME = "Data Transformation"


class DataTransformationPipeline:
    def __init__(self) -> None:
        pass

    def execute(self) -> None:
        conf_manager = ConfigurationManager()
        data_transformation_conf = conf_manager.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_conf)
        data_transformation.execute()


if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME} started >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        pipeline = DataTransformationPipeline()
        pipeline.execute()
        logger.info(f"{STAGE_NAME} finished <<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    except BaseException as e:
        logger.error(f"Encountered error during {STAGE_NAME}")
        logger.exception(e)
        raise e
