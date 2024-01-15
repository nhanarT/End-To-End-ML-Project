import joblib


class PredictionPipeline:
    def __init__(self) -> None:
        self.model = joblib.load('artifacts/training_model/models/model.joblib')

    def predict(self, data):
        prediction = self.model.predict(data)

        return prediction
