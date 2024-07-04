from dataclasses import dataclass
from pathlib import Path
from typing import List



@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict    
    
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    x_train_data_path: Path
    x_test_data_path: Path
    y_train_data_path: Path
    y_test_data_path: Path    
    model_name: str
    RANDOM_STATE: int
    EPOCH: int
    BATCH_SIZE: int
    VALIDATION_SPLIT: float
    MAX_WORDS : int
    MAX_LEN : int
    LOSS : str
    METRICS : List[str]
    ACTIVATION : str
    target_column: str
    
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    train_data_path : Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    model_evaluation_file_name: Path
    target_column: str