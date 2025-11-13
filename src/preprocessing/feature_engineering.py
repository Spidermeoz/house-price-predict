import pandas as pd
import re


def clean_location(text: str) -> str:
    text = text.lower().strip()
    patterns = [
        r"^quận\s*", r"^huyện\s*", r"^tp\.\s*",
        r"^tỉnh\s*", r"thành phố\s*"
    ]
    for p in patterns:
        text = re.sub(p, "", text)
    return text.strip()


def add_features(df: pd.DataFrame):

    # Price per m2
    df["price_per_m2"] = df["price"] / df["area"]

    # Total rooms
    df["total_rooms"] = df["bedrooms"] + df["bathrooms"]

    # Area binning
    df["area_category"] = pd.cut(
        df["area"],
        bins=[0,40,80,120,200,600],
        labels=["small", "medium", "large", "xlarge", "xxlarge"],
        include_lowest=True
    )

    # Clean district and city
    df["district"] = df["district"].apply(clean_location)
    df["city"] = df["city"].apply(clean_location)

    # Ratios and interactions
    df["frontage_ratio"] = df["frontage"] / df["area"]
    df["area_x_bedrooms"] = df["area"] * df["bedrooms"]
    df["ppm2_x_rooms"] = df["price_per_m2"] * df["total_rooms"]

    return df
