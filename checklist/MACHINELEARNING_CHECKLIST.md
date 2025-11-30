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

- [ ] B1.1 Tạo baseline:
  - [ ] Mô hình dự đoán **giá trung bình** (mean of y_train)
  - [ ] Tính MSE, RMSE, MAE, R² trên tập validation
- [ ] B1.2 Ghi lại kết quả baseline để so sánh với các model khác

---

### B2. Linear Regression (Hồi quy tuyến tính)

- [ ] B2.1 Huấn luyện mô hình `LinearRegression`
  - [ ] Fit trên X_train, y_train
- [ ] B2.2 Đánh giá trên tập validation
  - [ ] Tính MSE, RMSE, MAE, R²
  - [ ] So sánh với baseline
- [ ] B2.3 Phân tích hệ số hồi quy (coefficients)
  - [ ] Xem top feature có trọng số lớn (|coef| cao)
  - [ ] Ghi nhận trong báo cáo

---

### B3. Ridge & Lasso Regression (Ước lượng tham số có regularization)

- [ ] B3.1 Thiết lập lưới tham số (alpha)
  - [ ] alpha ∈ {0.01, 0.1, 1.0, 10}
- [ ] B3.2 Dùng `GridSearchCV` với k-fold (k=5)
  - [ ] Ridge Regression
  - [ ] Lasso Regression
- [ ] B3.3 Chọn mô hình tốt nhất theo RMSE trên validation
- [ ] B3.4 Đánh giá trên test:
  - [ ] MSE, RMSE, MAE, R²
- [ ] B3.5 Ghi lại tham số tối ưu (alpha tốt nhất)

---

### B4. KNN Regression (K-Nearest Neighbors)

- [ ] B4.1 Chọn khoảng k (ví dụ k ∈ {3, 5, 7, 9, 15})
- [ ] B4.2 Dùng `GridSearchCV` để tìm k tốt nhất (k-fold)
- [ ] B4.3 Đánh giá mô hình tốt nhất trên validation
- [ ] B4.4 Đánh giá trên test:
  - [ ] MSE, RMSE, MAE, R²
- [ ] B4.5 So sánh với Linear/Ridge/Lasso

---

### B5. Decision Tree Regression (Cây quyết định – Regression)

- [ ] B5.1 Thiết lập lưới tham số cho cây:
  - [ ] max_depth
  - [ ] min_samples_split
  - [ ] min_samples_leaf
- [ ] B5.2 Dùng `GridSearchCV` (k-fold) tìm tham số tốt nhất
- [ ] B5.3 Đánh giá trên validation & test
- [ ] B5.4 Phân tích feature importance từ cây quyết định

---

### B6. Cross-Validation & So sánh mô hình Regression

- [ ] B6.1 Dùng k-fold cross-validation (k=5 hoặc 10) trên train cho:
  - [ ] Linear Regression
  - [ ] Ridge
  - [ ] Lasso
  - [ ] KNN Regression
  - [ ] Decision Tree Regression
- [ ] B6.2 Tạo bảng tổng hợp:
  - [ ] Metric trung bình (RMSE, MAE, R²)
  - [ ] Độ lệch chuẩn của metric
- [ ] B6.3 Chọn mô hình Regression tốt nhất
- [ ] B6.4 Lưu mô hình Regression tốt nhất:
  - [ ] `models/best_regressor.pkl`

---

## C. Classification – Phân lớp nhóm giá (Price Band)

### C1. Tạo nhãn phân lớp từ Price

- [ ] C1.1 Định nghĩa các khoảng giá (ví dụ):
  - [ ] Low: Price < 4
  - [ ] Medium: 4 ≤ Price < 7
  - [ ] High: Price ≥ 7
- [ ] C1.2 Tạo cột `price_band` từ `price`
- [ ] C1.3 Kiểm tra phân bố số lượng mẫu mỗi lớp
- [ ] C1.4 Chia lại y_class_train, y_class_val, y_class_test tương ứng

---

### C2. Naive Bayes Classification (Phân lớp kiểu Bayes)

- [ ] C2.1 Chọn loại Naive Bayes phù hợp (Gaussian / Multinomial)
- [ ] C2.2 Train trên (X_train, y_class_train)
- [ ] C2.3 Đánh giá trên Validation:
  - [ ] Confusion Matrix
  - [ ] Accuracy
  - [ ] Precision, Recall, F1 (macro)
- [ ] C2.4 Đánh giá trên Test với các metric tương tự
- [ ] C2.5 Ghi nhận ưu/nhược điểm mô hình Bayes

---

### C3. KNN Classification

- [ ] C3.1 Chọn tập giá trị k (3, 5, 7, 9, …)
- [ ] C3.2 Dùng `GridSearchCV` với k-fold
- [ ] C3.3 Đánh giá mô hình tốt nhất trên Validation
  - [ ] Accuracy
  - [ ] Precision, Recall, F1
- [ ] C3.4 Đánh giá trên Test
- [ ] C3.5 So sánh với Naive Bayes

---

### C4. Decision Tree Classification

- [ ] C4.1 Thiết lập lưới tham số:
  - [ ] max_depth
  - [ ] min_samples_split
  - [ ] min_samples_leaf
- [ ] C4.2 Dùng `GridSearchCV` (k-fold)
- [ ] C4.3 Đánh giá trên Validation & Test:
  - [ ] Confusion Matrix
  - [ ] Accuracy, Precision, Recall, F1
- [ ] C4.4 Phân tích feature importance
- [ ] C4.5 So sánh với KNN & Naive Bayes

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
