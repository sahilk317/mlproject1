import yaml
import pandas as pd
import numpy as np
import os 
import sys
from src.logger import logging
from src.exception import SensorException
import dill

def read_yaml(file_path):

    try : 

        with open(file_path,'rb') as file:
            content = yaml.safe_load(file)
            logging.info(f"yaml file : {file_path} loaded successfully")
            return content
        

    except Exception as e:
        logging.info(f"error occured while reading yaml file : {file_path} : {e}") 
        raise SensorException(e, sys)
    
# if replace true that mean data drifting is there and if the file exist we need to remove it 
# and if replace is false that mean datadrifting is not there and we need to append the data to the file and create file if it does not exist not exist

    
def write_yaml(file_path,content,replace):

    try:
        if replace :
            os.path.exists(file_path)
            os.remove(file_path)
            logging.info(f"file : {file_path} already exist and removed")
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,'w') as file:
            yaml.dump(content,file)
            logging.info(f"yaml file : {file_path} created successfully")

    except Exception as e:
        logging.info(f"error occured while writing yaml file : {file_path} : {e}") 
        raise SensorException(e, sys)
        

