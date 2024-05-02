import sys 
from data.s3Operation import S3Operation
from xrayClassification.src.pipe.training_pipeline import trainingPipeline
from xrayClassification.src.entity.configEntity import DataIngestionConfig
from xrayClassification.src.entity.artifactEntity import DataIngestionArtifact
from xrayClassification.src.exceptions.exception import XrayException
from xrayClassification.src.logging import logging
from dataclasses import dataclass
@dataclass
class DataIngestion:
    def __init__(self, data_ingestion_config:DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config
        self.S3=S3Operation()
        
    def get_data_from_s3(self):
        try:
            logging.info("Entered the get_data_from s3 method of DataIngestion Class")
            self.S3.sync_folder_from_s3(
                folder=self.data_ingestion_config.data_path,
                bucket_name=self.data_ingestion_config.bucket_name,
                bucket_folder_name=self.data_ingestion_config.S3_data_folder
            )
            logging.info("Exited the get_data_from_s3 method from DataIngestion Class")
        
        except Exception as e:
            raise XrayException(e, sys)
        
    def initiate_data_ingestion(self):
        logging.info("Entered the initiate_data_ingestion method of DataIngestion Class")
        try:
            self.get_data_from_s3()
            data_ingestion_artifact: DataIngestionArtifact=DataIngestionArtifact(
                train_file_path=self.data_ingestion_config.train_data_path,
                test_file_path=self.data_ingestion_config.test_data_path
            )
            logging.info("Exited the initiate_data_ingestion method of DataIngestion Class")
            return data_ingestion_artifact
        except Exception as e:
            raise XrayException(e, sys)
        
        