import sys
import os
import pandas as pd
import numpy as np
import json
from src.constant.database import DATABASE_NAME,COLLECTION_NAME
from src.configuration.mongo_db_connection import mongo_db_connectionn
from src.exception import SensorException
from json import loads as json_loads
from src.logger import logging



# class sensorData :

#     def __init__(self):
#         try:
#             self.mongo_client = mongo_db_connectionn.client
#         except Exception as e:
#             SensorException(e,sys)

            

#     def send_csv_to_mongo(self,file_path: str, database_name: str, collection_name: str):
#         try:
#             # Read CSV file dynamically
#             df = pd.read_csv(file_path)
        
#             # Reset index and drop the old one
#             df.reset_index(drop=True, inplace=True)

#             # Convert DataFrame to JSON records (list of dictionaries)
#             data_json = json_loads(df.to_json(orient="records"))

#             # Insert into MongoDB
#             collection = self.mongo_client[database_name][collection_name]
#             collection.insert_many(data_json)

#             logging.info(f"Successfully inserted {len(data_json)} records into {database_name}.{collection_name}")

#         except Exception as e:
#             logging.error(f"Error while inserting data into MongoDB: {str(e)}")
#             raise SensorException(e, sys)
            

#     # def fetch_data_from_mongodb(self,database_name,collection_name):

#     #     self.collection = self.mongo_client[database_name][collection_name]


#     #     df = pd.DataFrame(list(self.collection.find()))

#     #     if 'id' in df.columns.to_list():
#     #         df = df.drop(columns=['id'],axis=1)
                
#     #     df.replace('na',np.nan,inplace=True)

#     #     return df
    




class sensorData:
    def __init__(self):
        try:
            mongo_db_conn = mongo_db_connectionn(DATABASE_NAME)
            self.mongo_client = mongo_db_conn.client  # Ensure correct variable name
            logging.info(self.mongo_client)
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")  # Handle error (or raise it)

    def fetch_data_from_mongodb(self, database_name, collection_name):
        try:
            collection = self.mongo_client[database_name][collection_name]
            df = pd.DataFrame(list(collection.find()))

            if '_id' in df.columns:
                df = df.drop(columns=['_id'])

            df.replace('na', np.nan, inplace=True)  # Replace string 'na' with NaN

            return df
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None  # Return None in case of failure