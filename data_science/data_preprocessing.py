import numpy as np
import pandas as pd


def preprocess_data(data):
    # Preprocess data using Pandas or NumPy
    # For example, clean missing values, normalize numerical data, or encode categorical data

    # Clean missing values
    data = data.fillna(data.mean())

    # Normalize numerical data
    numerical_data = data.select_dtypes(include=["int64", "float64"])
    numerical_data = (numerical_data - numerical_data.min()) / (
        numerical_data.max() - numerical_data.min()
    )

    # Encode categorical data
    categorical_data = data.select_dtypes(include=["object"])
    encoded_data = pd.get_dummies(categorical_data)

    # Concatenate the preprocessed data
    preprocessed_data = np.concatenate(
        [numerical_data.values, encoded_data.values], axis=1
    )

    return preprocessed_data
