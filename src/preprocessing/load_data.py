import pandas as pd

RAW_DATA_PATH = "../../data/raw/vietnam_housing_dataset.csv"
CLEANED_DATA_PATH = "../../data/interim/cleaned_dataset.csv"
ENGINEERED_DATA_PATH = "../../data/processed/engineered_dataset.csv"


def load_raw():
    return pd.read_csv(RAW_DATA_PATH)


def load_cleaned():
    return pd.read_csv(CLEANED_DATA_PATH)


def load_engineered():
    return pd.read_csv(ENGINEERED_DATA_PATH)
