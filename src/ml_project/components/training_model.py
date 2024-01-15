import os

import joblib
import numpy as np
import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from ml_project.entity.model_entity import HardVotingModel

from ml_project.entity.config_entity import TrainingModelConfig
from ml_project.utils import create_dirs

import logging

class TrainingModel:
    def __init__(self, config: TrainingModelConfig):
        self.config = config
        self.logger = logging.getLogger("ml_project.component.TrainingModel")

        create_dirs([self.config.stage_dir, self.config.output_dir])
        np.random.seed(self.config.SEED)

    def _train_and_save_model(self):
        # Read and split data for undersample
        train_data = pd.read_csv(os.path.join(self.config.data_dir, "train.csv"))
        target_col = self.config.schema.target.name
        fraud_data = train_data[train_data[target_col] == 1]
        no_fraud_data = train_data[train_data[target_col] == 0]

        # Undersample and train model
        if self.config.DEBUG:
            n_models = 1
        else:
            n_models = no_fraud_data.shape[0] // fraud_data.shape[0]
        knn_models = []
        rf_models = []
        self.logger.info(f"There are {n_models} models to train")
        for i in range(n_models):
            self.logger.info(f"Start training model {i}")
            undersampled_no_fraud_data = no_fraud_data.sample(n=fraud_data.shape[0])
            combined_data = pd.concat([undersampled_no_fraud_data, fraud_data])
            features = combined_data.drop([target_col], axis=1)
            target = combined_data[target_col]

            self.logger.info(f"Start training KNN_{i}")
            knn_model = KNeighborsClassifier(n_neighbors=3)
            knn_model.fit(features, target)
            knn_models.append(knn_model)
            self.logger.info(f"Trained KNN_{i}")

            self.logger.info(f"Start training RandomForest_{i}")
            rf_model = RandomForestClassifier(
                n_estimators=100, random_state=self.config.SEED + i
            )
            rf_model.fit(features, target)
            rf_models.append(rf_model)
            self.logger.info(f"Trained RandomForest_{i}")

        # Save model
        ensemble_model = HardVotingModel(knn_models + rf_models)
        ensemble_model.fit()
        save_path = os.path.join(self.config.output_dir, "model.joblib")
        joblib.dump(ensemble_model, save_path)
        self.logger.info(f"Saved model to {save_path}")

    def execute(self):
        self._train_and_save_model()
