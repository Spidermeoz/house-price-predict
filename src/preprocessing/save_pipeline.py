import joblib
import json
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer


def save_preprocessor(preprocessor, feature_names):

    joblib.dump(preprocessor, "models/preprocessor.pkl")

    with open("../../data/processed/feature_info.json", "w", encoding="utf-8") as f:
        json.dump(feature_names, f, ensure_ascii=False, indent=2)

