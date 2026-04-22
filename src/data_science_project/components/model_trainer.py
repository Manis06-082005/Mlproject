from dataclasses import dataclass
import os
import sys

from data_science_project.exception import CustomException
from data_science_project.logger import logging

from sklearn.metrics import classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from catboost import CatBoostClassifier
from xgboost import XGBClassifier

from data_science_project.utils import evaluate_models


@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = os.path.join('artifacts', 'model.pkl')


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Splitting training and testing data")

            X_train, y_train = train_array[:, :-1], train_array[:, -1]
            X_test, y_test = test_array[:, :-1], test_array[:, -1]

            models = {
                "Logistic Regression": LogisticRegression(),
                "Random Forest": RandomForestClassifier(),
                "SVM": SVC(),
                "KNN": KNeighborsClassifier(),
                "Decision Tree": DecisionTreeClassifier(),
                "Gradient Boosting": GradientBoostingClassifier(),
                "AdaBoost": AdaBoostClassifier(),
                "CatBoost": CatBoostClassifier(verbose=0),
                "XGBoost": XGBClassifier()
            }

            parameters = {
                "Logistic Regression": {},
                "Random Forest": {"n_estimators": [100], "max_depth": [10]},
                "SVM": {"C": [1.0], "kernel": ["rbf"]},
                "KNN": {"n_neighbors": [5]},
                "Decision Tree": {"max_depth": [10]},
                "Gradient Boosting": {"n_estimators": [100], "learning_rate": [0.1]},
                "AdaBoost": {"n_estimators": [100]},
                "CatBoost": {"iterations": [100], "learning_rate": [0.1]},
                "XGBoost": {"n_estimators": [100], "learning_rate": [0.1]}
            }

            # 🔥 Use only evaluate_models (no duplicate training)
            model_report = evaluate_models(
                X_train,
                y_train,
                X_test,
                y_test,
                models,
                parameters,
                model_save_path=self.model_trainer_config.trained_model_file_path
            )

            best_model_score = max(model_report.values())
            best_model_name = max(model_report, key=model_report.get)
            best_model = models[best_model_name]

            logging.info(f"Best model: {best_model_name} with score: {best_model_score}")

            # Predictions
            predicted = best_model.fit(X_train, y_train).predict(X_test)

            logging.info(f"\nClassification Report:\n{classification_report(y_test, predicted)}")
            logging.info(f"\nConfusion Matrix:\n{confusion_matrix(y_test, predicted)}")

            return best_model_name, best_model_score

        except Exception as e:
            raise CustomException(e, sys)