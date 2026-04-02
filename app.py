
import sys
from data_science_project.exception import CustomException
from data_science_project.logger import logging

if __name__ == "__main__":
    logging.info("Starting the ML project application.")
    logging.info("ML project application has finished execution.")
try:
    a = 1 / 0
except Exception as e:
    logging.error("An error occurred in the ML project application.")
    raise CustomException(e, sys)   
