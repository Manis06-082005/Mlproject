import sys
from data_science_project.exception import CustomException
from data_science_project.logger import logging
from data_science_project.components.data_ingestion import DataIngestion, DataIngestionConfig
from data_science_project.components.data_transformation import DataTransformation, DataTransformationConfig

if __name__ == "__main__":
    try:
        logging.info("Starting the ML project application.")

        # Initialize and start data ingestion
        data_ingestion = DataIngestion()
        train_path, test_path = data_ingestion.initiate_data_ingestion()
        # Initialize and start data transformation
        #data_transformation_config = DataTransformationConfig()
        #data_transformation = DataTransformation()
        #ata_transformation.initiate_data_transformation()
        data_transformation=DataTransformation()
        data_transformation.initiate_data_transformation(
            train_path=train_path,
            test_path=test_path


        )

        logging.info("ML project application has finished execution.")
    
    except Exception as e:
        logging.error("An error occurred in the ML project application.")
        raise CustomException(e, sys)