# from dataclasses import dataclass

# @dataclass

# class DataIngestionArtifact:
#     trained_file_path: str
#     test_file_path: str 

from src.logger import logging
from src.exception import SensorException
import sys
import os


class DataIngestionArtifact:

    def __init__(self,training_file_path ,testing_file_path):

        try:
            self.training_file_path  = training_file_path 
            self.testing_file_path = testing_file_path

            logging.info("Initialized DataIngestionArtifact")
            logging.info("Exited DataIngestionArtifact")

        except Exception as e:
            raise SensorException(e,sys)
        

class DataValidationArtifact:

    def __init__(self,validation_status ,valid_training_file_path,valid_testing_file_path,invalid_training_file_path,invalid_testing_file_path,drift_report_file_path):


        try:
            self.validation_status = validation_status  
            self.valid_training_file_path = valid_training_file_path
            self.valid_testing_file_path = valid_testing_file_path 
            self.invalid_training_file_path =invalid_training_file_path
            self.invalid_testing_file_path = invalid_testing_file_path
            self.drift_report_file_path = drift_report_file_path

            logging.info("Initialized DataValidationArtifacts")

        except Exception as e:
            raise SensorException(e,sys)
        
