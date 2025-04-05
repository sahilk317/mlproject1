import os
from datetime import datetime
from src.constant import training_pipeline

class TrainingPipelineConfig:

    def __init__(self,timestamp):
        
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name = training_pipeline.PIPELINE_NAME
        self.timestamp = timestamp
        self.artifact_dir = os.path.join(training_pipeline.ARTIFACT_DIR, self.timestamp)

    
class DataIngestionConfig:

    def __init__(self , trainging_pipeline_config : TrainingPipelineConfig):


        self.data_ingestion_dir = os.path.join(trainging_pipeline_config.artifact_dir,training_pipeline.DATA_INGESTION_DIR_NAME)
        self.feature_store_file_path = os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR,training_pipeline.FILE_NAME)
        self.training_file_path = os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR,training_pipeline.TRAIN_FILE_NAME)
        self.testing_file_path = os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR,training_pipeline.TEST_FILE_NAME)
        self.train_test_split_ratio = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.collection_name   = training_pipeline.DATA_INGESTION_COLLECTION_NAME

        
class DataValidationConfig:

    def __init__(self , traingin_pipeline_config):
        self.data_validation_dir = os.path.join(training_pipeline.ARTIFACT_DIR,training_pipeline.DATA_VALIDATION_DIR_NAME)
        self.data_validation_valid_dir = os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_VALID_DIR)
        self.data_validation_invalid_dir = os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_INVALID_DIR)
        self.data_validation_drift_report_dir = os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_DRIFT_REPORT_DIR,training_pipeline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME)
        self.valid_train_file_path = os.path.join(self.data_validation_valid_dir,training_pipeline.TRAIN_FILE_NAME)
        self.valid_test_file_path = os.path.join(self.data_validation_valid_dir,training_pipeline.TEST_FILE_NAME)
        self.invalid_train_file_path = os.path.join(self.data_validation_invalid_dir,training_pipeline.TRAIN_FILE_NAME)
        self.invalid_test_file_path = os.path.join(self.data_validation_invalid_dir,training_pipeline.TEST_FILE_NAME)
         
         