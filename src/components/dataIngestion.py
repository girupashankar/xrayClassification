import sys 
from data.s3Operation import S3Operation
from xrayClassification.src.pipe.training_pipeline import trainingPipeline
from xrayClassification.src.entity.configEntity import DataIngestionConfig
from xrayClassification.src.entity.artifactEntity import DataIngestionArtifactConfig
from xrayClassification.src.exceptions.exception import XrayException
from xrayClassification.src.logging import logging
from dataclasses import dataclass
@dataclass
class DataIngestion:
    def __init__(self) -> None:
        pass
    def get_data_from_s3(self):
        try:
            pass
        except Exception as e:
            raise XrayException(e, sys)
        
    def initiate_data_ingestion(self):
        try:
            pass
        except Exception as e:
            raise XrayException(e, sys)