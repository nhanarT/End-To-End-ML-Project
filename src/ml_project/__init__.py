from beartype.claw import beartype_this_package
beartype_this_package()

import os
import sys
import logging

log_str: str = "[%(asctime)s - %(levelname)s - %(name)s]: %(message)s"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "executing_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=log_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout),
    ],
)

logger = logging.getLogger("ml_project")
