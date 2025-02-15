import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)

def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}
        best_model = None
        best_score = float('-inf')  # Initialize best_score with the lowest possible value

        for model_name, model in models.items():
            gs = GridSearchCV(model, param[model_name], cv=3)
            gs.fit(X_train, y_train)

            best_model_current = gs.best_estimator_

            y_train_pred = best_model_current.predict(X_train)
            y_test_pred = best_model_current.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_model_score

            # Update best model if test score is higher
            if test_model_score > best_score:
                best_score = test_model_score
                best_model = best_model_current

        return report, best_model

    except Exception as e:
        raise CustomException(e, sys)

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
