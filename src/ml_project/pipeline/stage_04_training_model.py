from ml_project.config import ConfigurationManager
from ml_project.components import TrainingModel

import logging

logger = logging.getLogger("ml_project.pipeline.training_model")

STAGE_NAME = "Training Model"


class TrainingModelPipeline:
    def __init__(self) -> None:
        pass

    def execute(self) -> None:
        conf_manager = ConfigurationManager()
        training_model_conf = conf_manager.get_training_model_config()
        training_model = TrainingModel(config=training_model_conf)
        training_model.execute()


if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME} started >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        pipeline = TrainingModelPipeline()
        pipeline.execute()
        logger.info(f"{STAGE_NAME} finished <<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    except BaseException as e:
        logger.error(f"Encountered error during {STAGE_NAME}")
        logger.exception(e)
        raise e
