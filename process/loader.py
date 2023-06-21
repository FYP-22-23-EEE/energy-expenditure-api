import os
import random

import xgboost as xgb

from process.process import preprocess


class ModelPredictor:
    def __init__(self):
        # List of model file names
        model_files = [
            'xgboost-e4-general.model',
            'xgboost-muse-general.model',
            'xgboost-earbuds-general.model',
            'xgboost-zephyr-general.model',
            'xgboost-e4-running.model',
            'xgboost-muse-running.model',
            'xgboost-earbuds-running.model',
            'xgboost-zephyr-running.model',
            'xgboost-e4-cycling.model',
            'xgboost-muse-cycling.model',
            'xgboost-earbuds-cycling.model',
            'xgboost-zephyr-cycling.model'
        ]

        # Load the models into memory
        self.models = {}
        for model_file in model_files:
            model = xgb.Booster()
            model.load_model(os.path.join('models', model_file))
            model_name = model_file.rsplit('.', 1)[0]  # Remove file extension
            self.models[model_name] = model

    def _predict(self, input_data, model_name):
        # Preprocess the input data
        preprocessed_data = preprocess(input_data)

        # Make predictions using the specified model
        dmatrix = xgb.DMatrix(preprocessed_data)
        model_name = 'xgboost-e4-cycling.model'
        predictions = self.models[model_name].predict(dmatrix)

        return predictions
























    def predict(self, input_data, model_name):
        return random.uniform(0, 1)
