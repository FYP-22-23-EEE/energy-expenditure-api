import os

import xgboost as xgb
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

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

# Save the model to a file


for m in model_files:
    # Create a synthetic regression dataset
    X, y = make_regression(n_samples=100, n_features=3, noise=0.1)

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Define the XGBoost regressor model
    params = {'objective': 'reg:squarederror', 'colsample_bytree': 0.3, 'learning_rate': 0.1,
              'max_depth': 5, 'alpha': 10, 'n_estimators': 10}

    model = xgb.XGBRegressor(**params)

    # Train the model
    model.fit(X_train, y_train)

    model.save_model(os.path.join('../models', m))

print("Model has been saved to 'xgboost_regressor.model'")
