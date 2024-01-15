import os
import json

from pathlib import Path
from omegaconf import ListConfig, OmegaConf, DictConfig

from beartype import beartype
from beartype.typing import List, Any

import logging
logger = logging.getLogger("ml_project.utils")

OmegaConfOutput = DictConfig | ListConfig
StrOrPath = str | Path


@beartype
def read_yaml(file_path: StrOrPath) -> OmegaConfOutput:
    try:
        content = OmegaConf.load(file_path)
        logger.info(f"Loaded {file_path} successfully")
        if not content:
            logger.warning(f"{file_path} is empty")
        return content
    except BaseException as e:
        logger.error(f"Failed to load {file_path}")
        logger.exception(e)
        raise e


@beartype
def create_dirs(path_to_dir: List[StrOrPath], verbose: bool = True) -> None:
    for dir in path_to_dir:
        os.makedirs(dir, exist_ok=True)
        if verbose:
            if os.path.exists(dir):
                logger.info(f"Directory {dir} already exists")
            else:
                logger.info(f"Created directory {dir}")

@beartype
def save_json(file_path: StrOrPath, data: Any, overwrite: bool = False) -> None:
    if not overwrite and os.path.exists(file_path):
        raise FileExistsError(f"You call function with default value overwrite=False, {file_path} already exists")

    with open(file_path, 'w') as f:
        json.dump(data, f)
