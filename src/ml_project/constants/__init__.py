from pathlib import Path
from ml_project import logger

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")
SCHEMA_FILE_PATH = Path("schema.yaml")
DEBUG = True
if DEBUG:
    logger.warning("You are running in DEBUG mode")
