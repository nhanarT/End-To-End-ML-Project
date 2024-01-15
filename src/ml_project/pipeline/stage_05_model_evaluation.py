from ml_project.config import ConfigurationManager
from ml_project.components import ModelEvaluation

import logging

logger = logging.getLogger("ml_project.pipeline.model_evaluation")

STAGE_NAME = "Model Evaluation"


class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass

    def execute(self) -> None:
        conf_manager = ConfigurationManager()
        model_evaluation_conf = conf_manager.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_conf)
        model_evaluation.execute()


if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME} started >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        pipeline = ModelEvaluationPipeline()
        pipeline.execute()
        logger.info(f"{STAGE_NAME} finished <<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    except BaseException as e:
        logger.error(f"Encountered error during {STAGE_NAME}")
        logger.exception(e)
        raise e
