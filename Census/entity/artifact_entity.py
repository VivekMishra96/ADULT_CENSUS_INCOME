from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    feature_store_file_path:str
    train_file_path:str 
    test_file_path:str


@dataclass
class DataValidationArtifact:
    report_file_path:str

@dataclass
class DataTransformationArtifact:
    transform_object_path:str
    transformed_train_path:str
    transformed_test_path:str
    target_encoder_path:str
    input_feature_encoder_path:str


@dataclass
class ModelTrainerArtifact:
    model_path:str 
    f1_train_score:float 
    f1_test_score:float
