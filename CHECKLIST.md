# House Price Prediction Project – Checklist

## A. Data Preprocessing
- [ ] Load dataset (`vietnam_housing_dataset.csv`)
- [ ] Explore data (EDA: histogram, correlation, missing values)
- [ ] Handle missing values (median/mode imputation)
- [ ] Outlier treatment (log-transform or winsorize)
- [ ] Feature engineering (price/m², rooms, district)
- [ ] Encode categorical variables (OneHot/Target encoding)
- [ ] Scale numeric features (StandardScaler)
- [ ] Split dataset (Train/Val/Test 70/15/15)
- [ ] Save preprocessing pipeline (`preprocessor.pkl`)

## B. Machine Learning
### Regression
- [ ] Linear Regression (baseline)
- [ ] Ridge/Lasso (regularized)
- [ ] KNN Regressor
- [ ] Decision Tree Regressor
- [ ] Evaluate with RMSE, MAE, R²
- [ ] 5-fold Cross-validation

### Classification (Price Bands)
- [ ] Create PriceBand (Low–Mid–High)
- [ ] Gaussian Naive Bayes
- [ ] KNN Classifier
- [ ] Decision Tree Classifier
- [ ] Evaluate with Accuracy, F1, ROC-AUC
- [ ] StratifiedKFold validation

## C. Evaluation & Visualization
- [ ] Feature importance plot
- [ ] Residual plot (Regression)
- [ ] Confusion matrix (Classification)
- [ ] Save best model (`best_model.pkl`)

## D. Web Demo (Streamlit)
- [ ] Build input form (area, rooms, etc.)
- [ ] Load model & predict price
- [ ] Display result dynamically
- [ ] Deploy to Streamlit Cloud or HuggingFace Spaces

## E. Report
- [ ] Introduction & Objectives
- [ ] Dataset description & preprocessing
- [ ] Model building & evaluation
- [ ] Results & discussion
- [ ] Conclusion & future work

---
