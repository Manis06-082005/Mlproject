import os
import sys
import pandas as pd
import pickle

from sqlalchemy import create_engine
from dotenv import load_dotenv
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

from data_science_project.exception import CustomException
from data_science_project.logger import logging


# Load environment variables
load_dotenv()

host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')


def read_sql_data():
    logging.info("Reading data from SQL database using SQLAlchemy")

    try:
        engine = create_engine(
            f"mysql+pymysql://{user}:{password}@{host}/{database}"
        )

        query = "SELECT * FROM churn_modelling"
        df = pd.read_sql(query, engine)

        logging.info(f"Data successfully read. Shape: {df.shape}")
        print(df.head())

        return df

    except Exception as e:
        logging.error("Error occurred while reading data from SQL database")
        raise CustomException(e, sys)


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)

        logging.info(f"Object successfully saved to {file_path}")

    except Exception as e:
        logging.error(f"Error occurred while saving object to {file_path}")
        raise CustomException(e, sys)


def evaluate_models(X_train, y_train, X_test, y_test, models, parameters, model_save_path):
    try:
        model_report: dict = {}

        for model_name, model in models.items():
            param = parameters[model_name]

            gs = GridSearchCV(model, param, cv=3)
            gs.fit(X_train, y_train)

            y_test_pred = gs.predict(X_test)
            acc_score = accuracy_score(y_test, y_test_pred)

            model_report[model_name] = acc_score

        # Find best model
        best_model_score = max(model_report.values())
        best_model_name = max(model_report, key=model_report.get)

        logging.info(
            f"Best model: {best_model_name} with accuracy score: {best_model_score}"
        )

        # Save best model
        if best_model_score >= 0.6:
            best_model = models[best_model_name]

            save_object(
                file_path=model_save_path,
                obj=best_model
            )
        else:
            logging.warning("No model found with accuracy score above 0.6")

        return model_report

    except Exception as e:
        logging.error("Error occurred during model evaluation")
        raise CustomException(e, sys)