import os
import sys
from data_science_project.exception import CustomException
from data_science_project.logger import logging
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')

def read_sql_data():
    logging.info("Reading data from SQL database using SQLAlchemy")

    try:
        # create engine
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