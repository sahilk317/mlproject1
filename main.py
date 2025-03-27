# from src.utils import send_csv_to_mongo
# from src.entity import config_entity
# from datetime import datetime
import numpy as np
import pandas as pd
from src.components.data_ingestion import DataIngestion
from src.data_access.sensor_data import sensorData
from src.constant.database import DATABASE_NAME,COLLECTION_NAME
from src.entity.artifact_entity import DataIngestionArtifact
from src.entity.config_entity import training_pipeline,DataIngestionConfig
from src.exception import SensorException
from src.logger import logging
import sys
from datetime import datetime
from src.entity.config_entity import TrainingPipelineConfig




if __name__ == "__main__":
    # try:
    #     file_path = 'D:/shreeji/mlproject1/data.csv'
    #     databasename = 'aps_failure'
    #     collection_name = 'sensor'
    #     send_csv_to_mongo(file_path, databasename, collection_name)

    # except Exception as e:
    #     logging.error(e)

    data_ingestion_config = DataIngestionConfig(TrainingPipelineConfig(datetime.now()))
    data_ingestion = DataIngestion(data_ingestion_config)

    a = data_ingestion.initiate_data_ingestion()
    print(a.training_file_path)
    print(a.testing_file_path)

    