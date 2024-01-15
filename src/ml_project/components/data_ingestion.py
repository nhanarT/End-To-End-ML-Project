import os
import shutil
import zipfile

from ml_project.entity.config_entity import DataIngestionConfig
from ml_project.utils import create_dirs
import logging


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        self.logger = logging.getLogger('ml_project.component.DataIngestion')

        create_dirs([self.config.stage_dir, self.config.unzip_dir])

    def _ingest_data(self):
        if not os.path.exists(self.config.dest):
            shutil.copy2(self.config.source, self.config.dest)
            self.logger.info(f"Ingested data from {self.config.source}")
        else:
            self.logger.error(f"Cannot ingest data. {self.config.dest} already exists")
            raise RuntimeError(f"{self.config.dest} already exists")

    def _unzip_file(self):
        try:
            with zipfile.ZipFile(self.config.dest, "r") as zip_file_instance:
                zip_file_instance.extractall(self.config.unzip_dir)
        except BaseException as e:
            self.logger.error(f"Failed to unzip {self.config.dest}")
            self.logger.exception(e)
            raise RuntimeError(
                f"Something happened during extracting {self.config.dest}"
            )

    def _format_data(self):
        try:
            with open(
                os.path.join(self.config.unzip_dir, "card_transdata.csv"), "r"
            ) as f:
                data = f.read()

            with open(
                os.path.join(self.config.unzip_dir, "card_transdata.csv"), "w"
            ) as f:
                for line in data.split("\n"):
                    f.write(line + "\n")
            self.logger.info("Formated data")
        except BaseException as e:
            self.logger.error("Failed to format data")
            raise e

    def execute(self):
        self._ingest_data()
        self._unzip_file()
        self._format_data()
