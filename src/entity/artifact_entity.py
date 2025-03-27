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