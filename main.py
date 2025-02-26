from src.exception import SensorException
import sys
from src.logger import logging


def test_error():
    try:
        logging.info("This is a test log")
        a = 1 / 0

    except Exception as e:
        
        raise SensorException(e,sys)
    

if __name__ == "__main__":
    try:
        test_error()
    except Exception as e :
        logging.error(e)
        print(e)