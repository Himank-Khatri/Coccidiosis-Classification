from chickenDiseaseClassifier.config.configuration import ConfigurationManager
from chickenDiseaseClassifier.components.training import Training
from chickenDiseaseClassifier.components.prepare_callbacks import PrepareCallback
from chickenDiseaseClassifier import logger

class TrainingPipeline:
    def __init__(self):
        pass 

    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callbacks_config()
        prepare_callbacks = PrepareCallback(prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

        training_config = config.get_training_config()
        training = Training(training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list=callback_list
        )

if __name__ == '__main__':
    try:
        STAGE_NAME = "Training stage"
        logger.info("*****************************")
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = TrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<")
    except Exception as e:
        raise e