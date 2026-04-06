import sys
from data_science_project.exception import CustomException
from data_science_project.logger import logging
from data_science_project.components.data_ingestion import DataIngestion, DataIngestionConfig

if __name__ == "__main__":
    try:
        logging.info("Starting the ML project application.")

        # Initialize and start data ingestion
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

        logging.info("ML project application has finished execution.")
    
    except Exception as e:
        logging.error("An error occurred in the ML project application.")
        raise CustomException(e, sys)