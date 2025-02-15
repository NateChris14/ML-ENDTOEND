import sys
from src.exception import CustomException
from src.logger import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

class TrainPipeline:
    def __init__(self):
        pass

    def run(self):
        try:
            logging.info("Starting the training pipeline...")

            #Data Ingestion
            data_ingestion = DataIngestion()
            train_path, test_path = data_ingestion.initiate_data_ingestion()
            logging.info(f"Data Ingestion completed: Train - {train_path}, Test - {test_path}")

            #Data Transformation
            data_transformation = DataTransformation()
            train_array, test_array, preprocessor_path = data_transformation.initiate_data_transformation(train_path, test_path)
            logging.info(f"Data Transformation completed. Preprocessor saved at {preprocessor_path}")

            #Model Training
            model_trainer = ModelTrainer()
            model_score = model_trainer.initiate_model_trainer(train_array, test_array)
            logging.info(f"Model training completed with R² Score: {model_score}")

        except Exception as e:
            logging.error("Error occurred in training pipeline")
            raise CustomException(e, sys)

if __name__ == "__main__":
    pipeline = TrainPipeline()
    pipeline.run()
