import sys

from data_science_project.exception import CustomException
from data_science_project.logger import logging
from data_science_project.components.data_ingestion import DataIngestion
from data_science_project.components.data_transformation import DataTransformation
from data_science_project.components.model_trainer import ModelTrainer


if __name__ == "__main__":
    try:
        logging.info("Starting the ML project application.")

        # 🔹 Step 1: Data Ingestion
        data_ingestion = DataIngestion()
        train_path, test_path = data_ingestion.initiate_data_ingestion()

        # 🔹 Step 2: Data Transformation
        data_transformation = DataTransformation()
        train_array, test_array,_ = data_transformation.initiate_data_transformation(
            train_path=train_path,
            test_path=test_path
        )

        # 🔹 Step 3: Model Training
        model_trainer = ModelTrainer()
        best_model_name, best_model_score = model_trainer.initiate_model_trainer(
            train_array,
            test_array
        )

        print(f"Best Model: {best_model_name}")
        print(f"Best Score: {best_model_score}")

        logging.info("ML project application finished successfully.")

    except Exception as e:
        logging.error("An error occurred in the ML project application.")
        raise CustomException(e, sys)