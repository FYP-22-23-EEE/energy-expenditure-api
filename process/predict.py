import os

import pandas as pd
import xgboost as xgb
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from config.config import DataPoint
from process.loader import ModelPredictor
from process.process import MovingAverageTransformer
from utils import encode


def convert_to_dataframe(data_list):
    return pd.DataFrame(data_list)


def set_datetime_index(data):
    data['timestamp'] = pd.to_datetime('2023-06-20T18:59:47.291469')
    data.set_index('timestamp', inplace=True)
    return data


def calculate_window_size(data):
    return int(0.5 * len(data) / (1 + (data.index[-1] - data.index[0]).total_seconds()))


def create_processing_pipeline(window_size):
    return Pipeline([
        ('moving_avg', MovingAverageTransformer(window_size=window_size)),
        ('normalize', StandardScaler())
    ])


def preprocess(data_list):
    data = convert_to_dataframe(data_list)
    data = set_datetime_index(data)
    window_size = calculate_window_size(data)
    pipeline = create_processing_pipeline(window_size)
    processed_data = pipeline.fit_transform(data)
    processed_data = pd.DataFrame(processed_data, columns=['x', 'y', 'z'], index=data.index)
    return processed_data.iloc[:300]


class ModelPredictorGeneral:
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

    def predict(self, input_data, model_name):
        # Preprocess the input data
        input_data = []
        preprocessed_data = preprocess(input_data)

        # Make predictions using the specified model
        dmatrix = xgb.DMatrix(preprocessed_data)
        predictions = self.models[model_name].predict(dmatrix)

        return predictions


model_predictor_general = ModelPredictor()


def predict(datapoints: list[DataPoint], model) -> float:
    """
    Predicts the activity based on the datapoints.

    :param model:
    :param datapoints: list of datapoints
    :return: predicted activity
    """

    # get predictions
    results = model_predictor_general.predict(datapoints, model)

    # encode
    result = encode(datapoints, results)

    return result
