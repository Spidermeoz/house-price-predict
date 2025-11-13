import pandas as pd
from src.utils.helpers import safe_group_median_impute


def clean_data(df: pd.DataFrame):

    # 1. Chuẩn hóa tên cột
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    # 2. Drop columns with extremely high missing values
    df = df.drop(columns=["house_direction", "balcony_direction"], errors="ignore")

    # 3. Remove unrealistic area values
    df = df[df["area"].between(10, 600)]

    # 4. Winsorize frontage & access road
    df["frontage"] = df["frontage"].clip(1, 30)
    df["access_road"] = df["access_road"].clip(1, 40)

    # 5. Impute categorical
    df["furniture_state"] = df["furniture_state"].fillna("unknown")
    df["legal_status"] = df["legal_status"].fillna("unknown")

    # 6. Create area bins
    df["area_bin"] = pd.cut(
        df["area"],
        bins=[0, 40, 80, 120, 200, 600],
        labels=False,
        include_lowest=True,
    )

    # 7. Impute numeric using safe group median
    df["bedrooms"] = safe_group_median_impute(df, "area_bin", "bedrooms")
    df["bathrooms"] = safe_group_median_impute(df, "bedrooms", "bathrooms")
    df["floors"] = safe_group_median_impute(df, "bedrooms", "floors")
    df["frontage"] = safe_group_median_impute(df, "area_bin", "frontage")
    df["access_road"] = safe_group_median_impute(df, "district", "access_road")

    # 8. Remove helper column
    df = df.drop(columns=["area_bin"])

    # 9. Normalize text columns
    text_cols = ["district", "city", "legal_status", "furniture_state"]
    for col in text_cols:
        df[col] = df[col].astype(str).str.lower().str.strip()

    return df
