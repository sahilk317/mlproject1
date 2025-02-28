import numpy as np
import pandas as pd
import json
from json import loads as json_loads
from src.config import mongo_client
from src.exception import SensorException
from src.logger import logging
import sys

def send_csv_to_mongo(file_path: str, database_name: str, collection_name: str):
    try:
        # Read CSV file dynamically
        df = pd.read_csv(file_path)
        
        # Reset index and drop the old one
        df.reset_index(drop=True, inplace=True)

        # Convert DataFrame to JSON records (list of dictionaries)
        data_json = json_loads(df.to_json(orient="records"))

        # Insert into MongoDB
        collection = mongo_client[database_name][collection_name]
        collection.insert_many(data_json)

        logging.info(f"Successfully inserted {len(data_json)} records into {database_name}.{collection_name}")

    except Exception as e:
        logging.error(f"Error while inserting data into MongoDB: {str(e)}")
        raise SensorException(e, sys)
