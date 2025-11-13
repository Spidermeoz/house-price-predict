# Data Preprocessing Checklist

## Data Understanding
- [X] Load `vietnam_housing_dataset.csv` from `data/raw`
- [X] Inspect shape, columns, and dtypes
- [X] Summarize missing values per column
- [X] Visualize Price distribution (histogram, log-transform check)
- [X] Check correlation among numeric features
- [X] Extract district and city from `Address`
- [] Save initial summary to `reports/preprocessing_report.md`

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
- [ ] Encode categorical features (OneHotEncoder)
- [ ] Scale numeric features (StandardScaler)
- [ ] ColumnTransformer
- [ ] Pipeline
- [ ] Save feature metadata (`data/processed/feature_info.json`)
- [ ] Save preprocessor.pkl

## Data Splitting
- [ ] Split dataset into Train/Val/Test (70/15/15)
- [ ] Save processed files under `data/processed/`
- [ ] Verify distribution of target `Price` between splits
- [ ] Save `preprocessor.pkl` pipeline

## Quality Validation
- [ ] Ensure no NaN in processed data
- [ ] Check numeric features are normalized (mean≈0, std≈1)
- [ ] Ensure encoded categorical columns consistent across splits
- [ ] Document all changes in `reports/preprocessing_report.md`
