import sys
import os

sys.path.append(os.path.abspath("src"))

from src.mlProject.logger import logger

if __name__ == "__main__":
    logger.info("Starting the ML project application.")
    logger.info("ML project application has finished execution.")