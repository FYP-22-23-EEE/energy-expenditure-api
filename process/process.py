import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


class MovingAverageTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, window_size):
        self.window_size = window_size

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X.rolling(window=self.window_size).mean()
        return X


def convert_to_dataframe(data_list):
    return pd.DataFrame(data_list)


def set_datetime_index(data):
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    data.set_index('timestamp', inplace=True)
    return data


def calculate_window_size(data):
    return int(0.5 * len(data) / (data.index[-1] - data.index[0]).total_seconds())


def create_processing_pipeline(window_size):
    return Pipeline([
        ('moving_avg', MovingAverageTransformer(window_size=window_size)),
        ('normalize', StandardScaler())
    ])


def preprocess(data_list):
    # Convert the list of dictionaries to a DataFrame
    data = convert_to_dataframe(data_list)

    # Ensure timestamp is in datetime format and set as index
    data = set_datetime_index(data)

    # Calculate the window size for 0.5 seconds
    window_size = calculate_window_size(data)

    # Create a processing pipeline
    pipeline = create_processing_pipeline(window_size)

    # Apply moving average and normalization
    processed_data = pipeline.fit_transform(data)

    # Convert the processed data back into a DataFrame
    processed_data = pd.DataFrame(processed_data, columns=['x', 'y', 'z'], index=data.index)

    # Select 300 data points
    selected_data = processed_data.iloc[:300]

    # Calculate the average for x, y, z values
    avg_x = selected_data['x'].mean()
    avg_y = selected_data['y'].mean()
    avg_z = selected_data['z'].mean()

    return avg_x, avg_y, avg_z
