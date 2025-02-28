from src.exception import SensorException
import sys
from src.logger import logging
from src.utils import send_csv_to_mongo


if __name__ == "__main__":
    try:
        file_path = 'D:/shreeji/mlproject1/data.csv'
        databasename = 'aps_failure'
        collection_name = 'sensor'
        send_csv_to_mongo(file_path, databasename, collection_name)

    except Exception as e:
        logging.error(e)