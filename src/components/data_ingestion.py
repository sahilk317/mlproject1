import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from src.data_access.sensor_data import sensorData
from src.constant.database import DATABASE_NAME,COLLECTION_NAME
from src.entity.artifact_entity import DataIngestionArtifact
from src.entity.config_entity import training_pipeline,DataIngestionConfig
from src.exception import SensorException
from src.logger import logging
import sys

import os


class DataIngestion:

    def __init__(self,data_ingestion_config):
        try:
            self.data_ingestion_config = data_ingestion_config

            logging.info('variable self.data_ingestion_config is created')
        except Exception as e:
            raise SensorException(e,sys)
        

    def export_data_to_feature_store(self):
        try:
            sensor_data = sensorData()
            self.df = sensor_data.fetch_data_from_mongodb(DATABASE_NAME,COLLECTION_NAME)
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path            

            #creating folder

            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            
            self.df.to_csv(feature_store_file_path,index=False,header=True)

        except Exception as e:
            raise SensorException(e,sys)


        
        return self.df
    

    def split_data_as_train_test(self,df):
        try:
            train_set, test_set = train_test_split(
                df, test_size=self.data_ingestion_config.train_test_split_ratio
            )

            logging.info("Performed train test split on the dataframe")

            logging.info(
                "Exited split_data_as_train_test method of Data_Ingestion class"
            )

            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)

            os.makedirs(dir_path, exist_ok=True)

            logging.info(f"Exporting train and test file path.")

            train_set.to_csv(
                self.data_ingestion_config.training_file_path, index=False, header=True
            )

            test_set.to_csv(
                self.data_ingestion_config.testing_file_path, index=False, header=True
            )

            logging.info(f"Exported train and test file path.")
        except Exception as e:
            raise SensorException(e,sys)
        

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            dataframe = self.export_data_to_feature_store()

          

            self.split_data_as_train_test(df=self.df)

            data_ingestion_artifact = DataIngestionArtifact(self.data_ingestion_config.training_file_path,self.data_ingestion_config.testing_file_path)

            return data_ingestion_artifact
        
        except Exception as e:
            raise SensorException(e,sys)