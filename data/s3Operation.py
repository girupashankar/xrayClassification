import os 
import sys
from src.exceptions.exception import XrayException

class S3Operation:
    def sync_folder_to_s3()->None:
        try:
            pass
        except Exception as e:
            raise XrayException(e, sys)
    def sync_folder_from_s3()->None:
           try:
               pass
           except Exception as e:
               raise XrayException(e, sys) 