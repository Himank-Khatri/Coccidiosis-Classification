from chickenDiseaseClassifier import logger
from chickenDiseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from chickenDiseaseClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from chickenDiseaseClassifier.pipeline.stage_03_training import TrainingPipeline
from chickenDiseaseClassifier.pipeline.stage_04_evaluation import EvaluationPipeline


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model stage"
try:
    logger.info("*****************************")
    logger.info(f">>>>>>> stage {STAGE_NAME} started")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training stage"
try:
    logger.info("*****************************")
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    # obj = TrainingPipeline()
    # obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Evaluation stage"
try:
    logger.info("*****************************")
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    raise e