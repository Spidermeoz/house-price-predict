# 🧹 Preprocessing Report – House Price Dataset (Vietnam)

## 1. Introduction
Tài liệu này ghi lại toàn bộ quá trình tiền xử lý (Data Preprocessing) được áp dụng cho bộ dữ liệu bất động sản Việt Nam được crawl từ batdongsan.vn.  
Mục tiêu của phần tiền xử lý:
- Làm sạch dữ liệu
- Chuẩn hóa định dạng
- Xử lý giá trị thiếu
- Tạo đặc trưng mới
- Chuyển đổi dữ liệu cho phù hợp mô hình học máy
- Lưu pipeline thống nhất để tái sử dụng

---

## 2. Dataset Overview

### 2.1 Thông tin tổng quan
- **Số dòng ban đầu:** 30,229  
- **Số cột ban đầu:** 12  
- **Kiểu dữ liệu:**
  - Numeric: area, frontage, access_road, floors, bedrooms, bathrooms, price  
  - Categorical: address, legal_status, furniture_state, house_direction, balcony_direction  

### 2.2 Nhận xét ban đầu
- Giá trị thiếu ở house_direction (70.26%) và balcony_direction (82.65%) → cần loại bỏ.  
- Không có missing ở `address`, `area`, `price`.  
- Một số cột có outlier lớn: area, frontage, access_road.  
- Cột address chứa thông tin quận/huyện và tỉnh/thành → có thể tách để dùng trong mô hình.

---

## 3. Missing Values Analysis

### 3.1 Bảng Missing Values
| Column | Missing % |
|--------|-----------|
| balcony_direction | 82.65% |
| house_direction | 70.26% |
| furniture_state | 46.71% |
| access_road | 43.99% |
| frontage | 38.25% |
| bathrooms | 23.40% |
| bedrooms | 17.08% |
| legal_status | 14.91% |
| floors | 11.92% |
| area | 0% |
| address | 0% |
| price | 0% |

### 3.2 Chiến lược xử lý
- **Dropped:** house_direction, balcony_direction  
- **Impute categorical:** furniture_state, legal_status → `"unknown"`  
- **Impute numeric (group median):**
  - bedrooms → theo area_bin  
  - bathrooms → theo bedrooms  
  - floors → theo bedrooms  
  - frontage → theo area_bin  
  - access_road → theo district  

### 3.3 Kết quả sau xử lý
Toàn bộ tập dữ liệu sạch missing:

```
{
 'X_train': 0,
 'X_val': 0,
 'X_test': 0,
 'y_train': 0,
 'y_val': 0,
 'y_test': 0
}
```

---

## 4. Data Cleaning Steps

### 4.1 Chuẩn hóa text
- Chuyển về lowercase  
- Loại ký tự thừa  
- Chuẩn hóa district & city bằng regex  

### 4.2 Loại bỏ cột không cần thiết
- house_direction  
- balcony_direction  

### 4.3 Xử lý outlier
- area < 10 bị loại  
- frontage clipped 1 → 30  
- access_road clipped 1 → 40  

### 4.4 Imputation
- Numeric: median per-group (safe_group_median_impute)  
- Categorical: “unknown”  

### 4.5 Kết quả
- Dữ liệu sau cleaning: **30,223 dòng**  
- Không còn giá trị thiếu  
- Không còn outlier extreme  

---

## 5. Feature Engineering

### 5.1 Các đặc trưng mới
- price_per_m2  
- total_rooms  
- area_category (binning)  
- frontage_ratio  
- area_x_bedrooms  
- ppm2_x_rooms  

### 5.2 Chuẩn hóa District & City
- Loại bỏ “quận”, “huyện”, “tp.”, “tỉnh”  
- Chuyển về dạng standardized  

### 5.3 Kết quả
- Tổng số cột sau Feature Engineering: **17**  
- Không missing, phân phối hợp lý  

---

## 6. Encoding & Scaling

### 6.1 One-hot encoding
- Encode district, city, legal_status, furniture_state, area_category  
- handle_unknown="ignore"  
- Không sinh NaN  

### 6.2 Scaling (StandardScaler)
- Áp dụng cho toàn bộ numeric  
- Kết quả kiểm tra:
```
mean≈0 count = 388
std≈1 count  = 11
```

### 6.3 Số lượng feature sau transform
```
398 features
```

### 6.4 Lưu metadata
- File: `data/processed/feature_info.json`  
- Tổng số feature: 398 → khớp X_train.shape[1]

---

## 7. Dataset Splitting

### 7.1 Tỷ lệ chia
- Train: 70%  
- Validation: 15%  
- Test: 15%  

### 7.2 Kích thước thật
```
Train: (21156, 398)
Val:   (4533, 398)
Test:  (4534, 398)
```

### 7.3 Phân phối Price
| Metric | Train | Val | Test |
|--------|--------|--------|--------|
| mean | 5.873 | 5.810 | 5.931 |
| std | 2.224 | 2.180 | 2.181 |
| min | 1.0 | 1.0 | 1.0 |
| max | 11.5 | 10.9 | 10.0 |

→ Các phân phối gần như tương đồng.

---

## 8. Preprocessing Pipeline

### 8.1 Các bước trong ColumnTransformer
- numeric → StandardScaler  
- categorical → OneHotEncoder  

### 8.2 Lưu pipeline
- `models/preprocessor.pkl`  
- Sử dụng lại ở bước inference / Streamlit UI  

### 8.3 Lợi ích
- Đảm bảo train/test consistency  
- Đảm bảo deploy model dùng đúng preprocessing  

---

## 9. Final Clean Dataset Summary

- Số dòng cuối: **30,223**  
- Số feature cuối cùng: **398**  
- Số feature mới thêm: 6  
- Không còn Missing  
- Không còn outlier extreme  
- Dữ liệu phù hợp hoàn toàn để train mô hình  

---

## 10. Conclusion

Quá trình tiền xử lý đã hoàn tất thành công:
- Làm sạch đầy đủ  
- Xử lý missing theo nhóm  
- Tạo đặc trưng mới giá trị  
- Mã hóa và chuẩn hóa bài bản  
- Tách dữ liệu hợp lý  
- Kiểm tra chất lượng nghiêm ngặt  