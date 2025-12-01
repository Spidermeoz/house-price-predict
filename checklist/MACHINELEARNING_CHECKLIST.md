# Machine Learning Checklist – House Price Prediction (Vietnam)

---

## A. Chuẩn bị cho Học máy

- [x] A1. Load dữ liệu đã tiền xử lý

  - [x] Load `X_train.npy`, `X_val.npy`, `X_test.npy`
  - [x] Load `y_train.csv`, `y_val.csv`, `y_test.csv`
  - [x] Load `models/preprocessor.pkl` (nếu cần dùng lại)
  - [x] Load `data/processed/feature_info.json` (tên feature)

- [x] A2. Kiểm tra nhanh dữ liệu đầu vào cho Học máy

  - [x] Kiểm tra shape của X_train, X_val, X_test
  - [x] Kiểm tra phân phối lại của `y_train` (Price)
  - [x] Đảm bảo không còn NaN (double-check)

- [ ] A3. Định nghĩa bài toán & metric
  - [x] Bài toán 1: **Hồi quy (Regression)** – dự đoán `Price` (tỷ VND)
  - [x] Bài toán 2: **Phân lớp (Classification)** – phân loại nhóm giá (Low/Medium/High)
  - [x] Chọn metric cho Regression: MSE, RMSE, MAE, R²
  - [x] Chọn metric cho Classification: Accuracy, Precision, Recall, F1-score

---

## B. Regression – Dự đoán giá nhà (Price)

### B1. Baseline model (ước lượng tham số thống kê)

- [X] B1.1 Tạo baseline:
  - [X] Mô hình dự đoán **giá trung bình** (mean of y_train)
  - [X] Tính MSE, RMSE, MAE, R² trên tập validation
- [X] B1.2 Ghi lại kết quả baseline để so sánh với các model khác

---

### B2. Linear Regression (Hồi quy tuyến tính)

- [X] B2.1 Huấn luyện mô hình `LinearRegression`
  - [X] Fit trên X_train, y_train
- [X] B2.2 Đánh giá trên tập validation
  - [X] Tính MSE, RMSE, MAE, R²
  - [X] So sánh với baseline
- [X] B2.3 Phân tích hệ số hồi quy (coefficients)
  - [X] Xem top feature có trọng số lớn (|coef| cao)
  - [X] Ghi nhận trong báo cáo

---

### B3. Ridge & Lasso Regression (Ước lượng tham số có regularization)

- [X] B3.1 Thiết lập lưới tham số (alpha)
  - [X] alpha ∈ {0.01, 0.1, 1.0, 10}
- [X] B3.2 Dùng `GridSearchCV` với k-fold (k=5)
  - [X] Ridge Regression
  - [X] Lasso Regression
- [X] B3.3 Chọn mô hình tốt nhất theo RMSE trên validation
- [X] B3.4 Đánh giá trên test:
  - [X] MSE, RMSE, MAE, R²
- [X] B3.5 Ghi lại tham số tối ưu (alpha tốt nhất)

---

### B4. KNN Regression (K-Nearest Neighbors)

- [X] B4.1 Chọn khoảng k (ví dụ k ∈ {3, 5, 7, 9, 15})
- [X] B4.2 Dùng `GridSearchCV` để tìm k tốt nhất (k-fold)
- [X] B4.3 Đánh giá mô hình tốt nhất trên validation
- [X] B4.4 Đánh giá trên test:
  - [X] MSE, RMSE, MAE, R²
- [X] B4.5 So sánh với Linear/Ridge/Lasso

---

### B5. Decision Tree Regression (Cây quyết định – Regression)

- [X] B5.1 Thiết lập lưới tham số cho cây:
  - [X] max_depth
  - [X] min_samples_split
  - [X] min_samples_leaf
- [X] B5.2 Dùng `GridSearchCV` (k-fold) tìm tham số tốt nhất
- [X] B5.3 Đánh giá trên validation & test
- [X] B5.4 Phân tích feature importance từ cây quyết định

---

### B6. Cross-Validation & So sánh mô hình Regression

- [X] B6.1 Dùng k-fold cross-validation (k=5 hoặc 10) trên train cho:
  - [X] Linear Regression
  - [X] Ridge
  - [X] Lasso
  - [X] KNN Regression
  - [X] Decision Tree Regression
- [X] B6.2 Tạo bảng tổng hợp:
  - [X] Metric trung bình (RMSE, MAE, R²)
  - [X] Độ lệch chuẩn của metric
- [X] B6.3 Chọn mô hình Regression tốt nhất
- [X] B6.4 Lưu mô hình Regression tốt nhất:
  - [X] `models/best_regressor.pkl`

---

## C. Classification – Phân lớp nhóm giá (Price Band)

### C1. Tạo nhãn phân lớp từ Price

- [X] C1.1 Định nghĩa các khoảng giá (ví dụ):
  - [X] Low: Price < 4
  - [X] Medium: 4 ≤ Price < 7
  - [X] High: Price ≥ 7
- [X] C1.2 Tạo cột `price_band` từ `price`
- [X] C1.3 Kiểm tra phân bố số lượng mẫu mỗi lớp
- [X] C1.4 Chia lại y_class_train, y_class_val, y_class_test tương ứng

---

### C2. Naive Bayes Classification (Phân lớp kiểu Bayes)

- [X] C2.1 Chọn loại Naive Bayes phù hợp (Gaussian / Multinomial)
- [X] C2.2 Train trên (X_train, y_class_train)
- [X] C2.3 Đánh giá trên Validation:
  - [X] Confusion Matrix
  - [X] Accuracy
  - [X] Precision, Recall, F1 (macro)
- [X] C2.4 Đánh giá trên Test với các metric tương tự
- [X] C2.5 Ghi nhận ưu/nhược điểm mô hình Bayes

---

### C3. KNN Classification

- [X] C3.1 Chọn tập giá trị k (3, 5, 7, 9, …)
- [X] C3.2 Dùng `GridSearchCV` với k-fold
- [X] C3.3 Đánh giá mô hình tốt nhất trên Validation
  - [X] Accuracy
  - [X] Precision, Recall, F1
- [X] C3.4 Đánh giá trên Test

---

### C4. Decision Tree Classification

- [X] C4.1 Thiết lập lưới tham số:
  - [X] max_depth
  - [X] min_samples_split
  - [X] min_samples_leaf
- [X] C4.2 Dùng `GridSearchCV` (k-fold)
- [X] C4.3 Đánh giá trên Validation & Test:
  - [X] Confusion Matrix
  - [X] Accuracy, Precision, Recall, F1
- [X] C4.4 Phân tích feature importance

---

## D. Model Comparison & Selection

- [ ] D1. Tạo bảng so sánh Regression models:
  - [ ] Baseline vs Linear vs Ridge vs Lasso vs KNN vs Decision Tree
  - [ ] Ghi lại: RMSE, MAE, R² (Val & Test)
- [ ] D2. Tạo bảng so sánh Classification models:
  - [ ] Naive Bayes vs KNN vs Decision Tree
  - [ ] Ghi lại: Accuracy, Precision, Recall, F1 (Val & Test)
- [ ] D3. Chọn:
  - [ ] Best Regression model
  - [ ] Best Classification model
- [ ] D4. Lưu:
  - [ ] `models/best_regressor.pkl`
  - [ ] `models/best_classifier.pkl`

---

## E. Cross-Validation & Xác thực mô hình

- [ ] E1. Áp dụng k-fold (k=5 hoặc 10) cho mô hình tốt nhất
- [ ] E2. Ghi lại:
  - [ ] Mean & std của metric qua các fold
- [ ] E3. Giải thích ý nghĩa của Cross-Validation trong báo cáo

---

## F. Đánh giá & Diễn giải Kết quả

- [ ] F1. Phân tích lỗi (Error Analysis) cho Regression
  - [ ] Biểu đồ Residuals (y_true - y_pred)
  - [ ] Scatter plot: y_true vs y_pred
- [ ] F2. Phân tích Classification:
  - [ ] Confusion Matrix rõ ràng
  - [ ] Class-wise Recall & Precision
- [ ] F3. Đánh giá ý nghĩa thực tế của mô hình
  - [ ] Mức độ tin cậy của dự đoán giá nhà
  - [ ] Ứng dụng: gợi ý giá, tham khảo cho môi giới/khách hàng

---

## G. Lưu mô hình & Tích hợp với Pipeline

- [ ] G1. Đảm bảo mô hình dùng chung `preprocessor.pkl`
- [ ] G2. Tạo hàm `predict_price(raw_input)`:
  - [ ] Nhận input dạng raw (giống dữ liệu gốc)
  - [ ] Dùng preprocessor → transform
  - [ ] Dùng best_regressor → dự đoán Price
- [ ] G3. Tạo hàm `predict_price_band(raw_input)`:
  - [ ] Dự đoán nhóm giá (Low/Medium/High)
- [ ] G4. Lưu toàn bộ:
  - [ ] preprocessor.pkl
  - [ ] best_regressor.pkl
  - [ ] best_classifier.pkl

---

## H. Báo cáo Học máy (Model Report)

- [ ] H1. Tạo file `reports/model_report.md`
- [ ] H2. Ghi lại:
  - [ ] Bài toán & mục tiêu
  - [ ] Dataset & preprocessing (tóm tắt)
  - [ ] Các mô hình đã thử
  - [ ] Kết quả chi tiết (bảng metric)
  - [ ] So sánh & chọn mô hình cuối cùng
  - [ ] Hạn chế & hướng phát triển
