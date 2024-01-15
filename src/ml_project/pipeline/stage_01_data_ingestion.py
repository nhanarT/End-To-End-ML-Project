from ml_project.config import ConfigurationManager
from ml_project.components import DataIngestion

import logging
logger = logging.getLogger("ml_project.pipeline.data_ingestion")

STAGE_NAME = "Data Ingestion"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def execute(self):
        conf_manager = ConfigurationManager()
        data_ingestion_conf = conf_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_conf)
        data_ingestion.execute()

if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME} started >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        pipeline = DataIngestionPipeline()
        pipeline.execute()
        logger.info(f"{STAGE_NAME} finished <<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    except BaseException as e:
        logger.error(f"Encountered error during {STAGE_NAME}")
        logger.exception(e)
        raise e
