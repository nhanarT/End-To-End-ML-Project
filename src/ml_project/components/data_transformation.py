import os

import pandas as pd
from sklearn.model_selection import train_test_split

from ml_project.entity.config_entity import DataTransformationConfig
from ml_project.utils.common import create_dirs

import logging

class DataTransformation:
    def __init__(self, config: DataTransformationConfig) -> None:
        self.config = config
        self.logger = logging.getLogger("ml_project.component.DataTransformation")

        create_dirs([self.config.stage_dir])

    def _transform_data(self):
        df = pd.read_csv(os.path.join(self.config.data_dir, "card_transdata.csv"))
        test_size = self.config.test_size
        target_col = self.config.target

        train_df, test_df = train_test_split(
            df, test_size=test_size, stratify=df[target_col]
        )

        train_df.to_csv(os.path.join(self.config.stage_dir, "train.csv"), index=False)
        test_df.to_csv(os.path.join(self.config.stage_dir, "test.csv"), index=False)

        self.logger.info("Transformed data")

    def execute(self):
        self._transform_data()
