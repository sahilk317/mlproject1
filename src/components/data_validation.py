import sys
import os
from src.logger import logging
from src.exception import SensorException

from src.entity.config_entity import DataValidationConfig,DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact

from src.constant.training_pipeline import SCHEMA_FILE_PATH
from src.utils.main_utils import read_yaml, write_yaml




class DataValidation :

    def __init__(self,data_ingestion_artifact : DataIngestionArtifact , data_ingestion_config : DataIngestionConfig):

        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_ingestion_config = data_ingestion_config
            self._schema_config = read_yaml(SCHEMA_FILE_PATH)
            
            logging.info('initialize data ingestion artifact and ingestion config')

        
        except Exception as e : 
            raise SensorException(e,sys)
    