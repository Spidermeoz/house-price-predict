# MODEL REPORT – House Price Prediction (Vietnam)

**Dự án:** Machine Learning – Dự đoán giá nhà & Phân loại nhóm giá  
**Dataset:** Vietnam Housing Dataset  
**Thực hiện:** (Tên sinh viên / nhóm)  
**Ngày:**  

---

# MỤC LỤC

1. [Giới thiệu](#giới-thiệu)  
2. [Dataset & Preprocessing](#dataset--preprocessing)  
3. [Bài toán & Mục tiêu](#bài-toán--mục-tiêu)  
4. [Mô hình Regression](#mô-hình-regression)  
5. [Mô hình Classification](#mô-hình-classification)  
6. [Cross-Validation & Đánh giá mô hình](#cross-validation--đánh-giá-mô-hình)  
7. [Phân tích lỗi (Error Analysis)](#phân-tích-lỗi-error-analysis)  
8. [So sánh & lựa chọn mô hình cuối](#so-sánh--lựa-chọn-mô-hình-cuối)  
9. [Ứng dụng thực tế của mô hình](#ứng-dụng-thực-tế-của-mô-hình)  
10. [Hạn chế & Hướng phát triển](#hạn-chế--hướng-phát-triển)  

---

# GIỚI THIỆU

Bất động sản là một lĩnh vực có dữ liệu phong phú, phi tuyến và phức tạp. Việc định giá tài sản và phân loại phân khúc giá thường dựa vào kinh nghiệm chuyên gia, dẫn đến:

- Sai số lớn  
- Tính chủ quan cao  
- Mất thời gian trong tư vấn và thẩm định  

Dự án này xây dựng hệ thống **AI định giá nhà** dựa trên dữ liệu thật từ thị trường Việt Nam, sử dụng các kỹ thuật **tiền xử lý**, **học máy có giám sát**, **hồi quy**, **phân lớp**, **cross-validation**, và **đánh giá mô hình**.

---

# DATASET & PREPROCESSING

## 1. Dataset
File gốc:  
`data/raw/vietnam_housing_dataset.csv`  
Bao gồm các nhóm biến:

- Diện tích (area)  
- Số phòng (bedrooms, bathrooms)  
- Giá trị (price)  
- Vị trí (city, district)  
- Đặc điểm vật lý (frontage, access_road)  
- Thông số mở rộng từ feature engineering

## 2. Các bước tiền xử lý (đã hoàn thành)
- Làm sạch dữ liệu  
- Xử lý NA  
- Feature engineering  
- Tạo biến tương tác  
- Chuẩn hóa dữ liệu  
- One-hot encoding categorical features  
- Chia dữ liệu thành train/val/test  
- Lưu preprocessor vào `models/preprocessor.pkl`

## 3. Kiểm tra sau tiền xử lý
- Không còn NA  
- X_train shape: (21156, 398)  
- y_train shape: (21156,)  
- Dải giá trị hợp lý (1–11.5 tỷ VNĐ)  

---

# BÀI TOÁN & MỤC TIÊU

Dự án bao gồm **2 bài toán song song**:

## 1. **Regression** – Dự đoán giá nhà (đơn vị: tỷ VNĐ)
- Output: giá dự đoán, dạng continuous  
- Metric chính: RMSE  
- Metric phụ: MAE, R²  

## 2. **Classification** – Phân lớp Price Band
Dựa trên giá:

| Nhóm | Khoảng giá |
|------|------------|
| Low | < 4 tỷ |
| Medium | 4–7 tỷ |
| High | ≥ 7 tỷ |

- Metric chính: F1-score macro  
- Metric phụ: Accuracy, Precision, Recall  

---

# MÔ HÌNH REGRESSION

Các mô hình được huấn luyện và đánh giá:

1. **Baseline (Mean model)**  
2. **Linear Regression**  
3. **Ridge Regression**  
4. **Lasso Regression**  
5. **KNN Regression**  
6. **Decision Tree Regression**

## Kết quả chính (Validation)

| Model | RMSE | MAE | R² |
|-------|------|------|------|
| Baseline | 2.1810 | 1.8097 | -0.0008 |
| Linear Regression | 0.9649 | 0.6817 | 0.8041 |
| Ridge Regression | 0.9561 | 0.6807 | 0.8077 |
| Lasso Regression | 1.0343 | 0.7595 | 0.7749 |
| KNN Regression | 1.0417 | 0.7614 | 0.7717 |
| **Decision Tree Regression** | **0.1524** | **0.0702** | **0.9951** |

## Nhận xét Regression
- Decision Tree Regression vượt trội hoàn toàn so với các mô hình còn lại.  
- RMSE giảm từ ~0.95 (Linear/Ridge) xuống chỉ còn ~0.15  
- R² ≈ 0.995 → gần như mô phỏng hoàn hảo dữ liệu.  
- Mô hình hoạt động ổn định trên test set với RMSE ≈ 0.1518  

---

# MÔ HÌNH CLASSIFICATION

Các mô hình thử nghiệm:

1. **Gaussian Naive Bayes**  
2. **KNN Classification**  
3. **Decision Tree Classification**

## Kết quả (Validation & Test)

| Model | Val F1 | Test F1 | Accuracy Test |
|-------|--------|---------|----------------|
| GaussianNB | 0.276 | 0.286 | 0.37 |
| KNN Classifier | 0.783 | 0.798 | 0.79 |
| **Decision Tree Classifier** | **0.978** | **0.973** | **0.973** |

## Nhận xét Classification
- Naive Bayes hoạt động kém do dữ liệu không tuân Gaussian.  
- KNN khá tốt nhưng gặp khó với 398 features.  
- Decision Tree Classification đạt hiệu năng cực cao và ổn định.

---

# CROSS-VALIDATION & ĐÁNH GIÁ MÔ HÌNH

## Regression – Decision Tree

| Metric | Mean | Std |
|--------|------|------|
| RMSE | 0.1687 | 0.0165 |
| MAE | 0.0771 | 0.0041 |
| R² | 0.9942 | 0.00116 |

### Nhận xét:
- Sai số nhỏ, độ lệch chuẩn nhỏ → mô hình rất ổn định.  
- Không overfit, không high variance.  

---

## Classification – Decision Tree

| Metric | Mean | Std |
|--------|------|------|
| Accuracy | 0.9750 | 0.00418 |
| Precision | 0.9754 | 0.00444 |
| Recall | 0.9758 | 0.00372 |
| F1-score | 0.9756 | 0.00403 |

### Nhận xét:
- Tính ổn định cực cao ở tất cả metric.  
- Sai nhầm chủ yếu tại biên 4–7 tỷ → hoàn toàn hợp lý theo thực tế thị trường.  

---

# PHÂN TÍCH LỖI (ERROR ANALYSIS)

## Regression – Residual Plot
- Residual phân bố quanh 0.  
- Không có pattern theo giá trị.  
- Không heteroscedasticity.  
→ Mô hình phù hợp và ổn định.

## Regression – True vs Predicted
- Các điểm gần như nằm trên đường y = x.  
→ Mô hình dự đoán tốt cả 3 phân khúc giá.

## Classification – Confusion Matrix
- Không có lỗi phân loại Low ↔ High  
- Hầu hết nhầm lẫn ở vùng biên giá.  
→ Mô hình học đúng logic thị trường.

---

# SO SÁNH & LỰA CHỌN MÔ HÌNH CUỐI

## Best Regression Model  
**Decision Tree Regression**  
- RMSE: 0.152  
- R²: 0.995  
- CV ổn định  
→ Chọn làm `best_regressor.pkl`

## Best Classification Model  
**Decision Tree Classification**  
- F1: 0.973  
- Accuracy: 0.973  
- CV ổn định  
→ Chọn làm `best_classifier.pkl`

---

# ỨNG DỤNG THỰC TẾ CỦA MÔ HÌNH

### ✓ Định giá bất động sản (AVM – automated valuation model)  
### ✓ Tư vấn giá bán / giá mua  
### ✓ Phân loại phân khúc khách hàng  
### ✓ Hỗ trợ ngân hàng định giá tài sản thế chấp  
### ✓ Công cụ phân tích thị trường  
### ✓ Gợi ý tài sản phù hợp theo ngân sách  

Hai mô hình đủ mạnh để tích hợp vào:

- API  
- Web app  
- Mobile app  
- Hệ thống môi giới  
- Công cụ nội bộ cho ngân hàng  

---

# HẠN CHẾ & HƯỚNG PHÁT TRIỂN

## 1. Hạn chế
- Không có dữ liệu về nội thất thật, view, pháp lý, năm xây dựng  
- Một số outlier giá cao chưa được mô hình giải thích hoàn toàn  
- Decision Tree có thể phình to nếu không kiểm soát  

## 2. Hướng phát triển
- Thử Random Forest hoặc Gradient Boosting  
- Tích hợp thêm dữ liệu thị trường (giá/m² theo thời gian)  
- Bổ sung dữ liệu thực địa (ảnh, tọa độ GPS, chất lượng đường, tiện ích xung quanh)  
- Đưa mô hình lên API và chạy thử nghiệm thực tế  

---

# KẾT LUẬN

Dự án đã xây dựng thành công một hệ thống học máy hoàn chỉnh cho bài toán định giá và phân loại bất động sản Việt Nam.

Hai mô hình cuối cùng — Decision Tree Regression và Decision Tree Classification — đạt độ chính xác cực cao, ổn định và có tính ứng dụng thực tế lớn.

Hệ thống sẵn sàng để triển khai vào các ứng dụng doanh nghiệp hoặc sản phẩm thực tế.
