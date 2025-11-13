# Data Preprocessing Checklist

## Data Understanding
- [X] Load `vietnam_housing_dataset.csv` from `data/raw`
- [X] Inspect shape, columns, and dtypes
- [X] Summarize missing values per column
- [X] Visualize Price distribution (histogram, log-transform check)
- [X] Check correlation among numeric features
- [X] Extract district and city from `Address`

## Data Cleaning
- [X] Handle missing numeric columns (median imputation)
- [X] Handle missing categorical columns (most_frequent/“Unknown”)
- [X] Standardize text fields (lowercase, strip)
- [X] Remove or cap extreme outliers in `Price` and `Area`
- [X] Convert units (e.g., Price in billions VND)

## Feature Engineering
- [X] Create `Price_per_m2 = Price / Area`
- [X] Create `Rooms = Bedrooms + Bathrooms`
- [X] Derive `District` and `City` from `Address`

## Encoding & Scaling
- [X] Encode categorical features (OneHotEncoder)
- [X] Scale numeric features (StandardScaler)
- [X] ColumnTransformer
- [X] Pipeline
- [X] Save feature metadata (`data/processed/feature_info.json`)
- [X] Save preprocessor.pkl

## Data Splitting
- [X] Split dataset into Train/Val/Test (70/15/15)
- [X] Save processed files under `data/processed/`
- [X] Verify distribution of target `Price` between splits
- [X] Save `preprocessor.pkl` pipeline

## Quality Validation
- [X] Ensure no NaN in processed data
- [X] Check numeric features are normalized (mean≈0, std≈1)
- [X] Ensure encoded categorical columns consistent across splits
- [X] Document all changes in `reports/preprocessing_report.md`
