import os

import pandas as pd
import mlflow
import joblib

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

from ml_project.utils import create_dirs, save_json

class ModelEvaluation():
    def __init__(self, config):
        self.config = config
        
        create_dirs([self.config.stage_dir])

    def evaluate_metrics(self, y_true, y_pred):
        acc = accuracy_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred)
        recall = recall_score(y_true, y_pred)
        f1 = f1_score(y_true, y_pred)
        auc = roc_auc_score(y_true, y_pred)
        result = {
            "acc": acc,
            "precision": precision,
            "recall": recall,
            "f1": f1,
            "auc": auc,
        }
        return result

    def _model_evaluation(self):
        test_data = pd.read_csv(os.path.join(self.config.data_dir, 'test.csv'))
        target_col = self.config.schema.target.name
        features = test_data.drop(target_col, axis=1)
        target = test_data[target_col]

        mlflow.set_tracking_uri(self.config.mlflow_uri)
        mlflow_tracking_store_type = mlflow.get_tracking_uri().split(":")[0]
        
        mlflow.set_experiment("ml_project")
        
        with mlflow.start_run():
            
            mlflow.log_params(self.config.model_params)

            model = joblib.load(os.path.join(self.config.model_dir, 'model.joblib'))
            prediction = model.predict(features)
            metrics = self.evaluate_metrics(target, prediction)
            save_json(self.config.metric_file_name, metrics, overwrite=True)

            mlflow.log_metrics(metrics)
            
            if mlflow_tracking_store_type != 'file':
                mlflow.sklearn.log_model(model, "model", registered_model_name="Ensemble_KNN_RandomForest")
            else:
                mlflow.sklearn.log_model(model, "model")

    def execute(self):
        self._model_evaluation()
