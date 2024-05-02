import sys
from src.components.dataIngestion import DataIngestion
from src.entity.artifactEntity import DataIngestionArtifact
from src.entity.configEntity import DataIngestionConfig
from src.exceptions.exception import XrayException
from src.logging import logging

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()
    
    def start_data_ingestion(self)-> DataIngestionArtifact:
        logging.info("Entered the start_data_intestion method of TrainPipeline class")
        try:
            logging.info("Getting the data from s3 bucket")
            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config
            )
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the train_set and test_set from s3")
            
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")
            
            return data_ingestion_artifact
        except Exception as e:
            raise XrayException(e, sys)

if __name__ == "__main__":
    train_pipeline=TrainPipeline()
    train_pipeline.start_data_ingestion()
            
        
        