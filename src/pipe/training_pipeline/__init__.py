from datetime import datetime
from typing import List

import torch
TIMESTAMP: str = datetime.now().strftime("%d//%m//%Y - %H:%M%:S")

ARTIFACT_DIR: str = 'artifacts'

BUCKET_NAME: str = 'xrayImageDatas'

S3_DATA_FOLDER: str =  'data'

CLASS_LABEL_1: str = 'NORMAL'
CLASS_LABEL_2: str = 'PNEUMONIA'
