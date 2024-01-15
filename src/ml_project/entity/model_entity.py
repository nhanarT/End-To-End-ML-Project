import numpy as np

from beartype.typing import List

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.base import BaseEstimator, ClassifierMixin



class HardVotingModel(BaseEstimator, ClassifierMixin):
    """
        A model that accept prefit classifiers
    """
    def __init__(
        self, estimators: List[KNeighborsClassifier | RandomForestClassifier]
    ) -> None:
        super().__init__()
        self.estimators = estimators

    def fit(self, X=None, y=None):
        return self

    def predict(self, X):
        predictions = np.asarray(
            [estimator.predict(X) for estimator in self.estimators]
        ).T
        predictions = predictions.astype(int)
        majority_vote = np.apply_along_axis(
            lambda x: np.argmax(np.bincount(x)), axis=1, arr=predictions
        )
        return majority_vote

