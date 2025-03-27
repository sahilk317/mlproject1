import pymongo
from src.constant.env_variable import MONGO_DB_KEY
from src.constant.database import DATABASE_NAME , COLLECTION_NAME
from src.logger import logging
from dotenv import load_dotenv
import os

print('reading dotenv file')

load_dotenv()

logging.info('complete reading dotenv file')

class mongo_db_connectionn:
    client = None

    def __init__(self,database_name):
        database_name = DATABASE_NAME

        try:
            if mongo_db_connectionn.client is None:
                mongo_db_url = os.getenv(MONGO_DB_KEY)
                logging.info(f'retriving mongodb url {mongo_db_url}')
                mongo_client = pymongo.MongoClient(mongo_db_url)
                print("MongoDB connection established successfully!")

            self.client = mongo_client
            self.database = self.client[database_name]
            self.database_name = database_name

        except Exception as e:

                print(f"Error connecting to MongoDB: {e}")
                logging.error(f'error {e}')
                mongo_client = None  # Set to None if connection fails



