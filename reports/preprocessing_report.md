# 🧹 Preprocessing Report – House Price Dataset (Vietnam)

## 1. Introduction
Tài liệu này ghi lại toàn bộ quá trình tiền xử lý (Data Preprocessing) được áp dụng lên bộ dữ liệu bất động sản Việt Nam được crawl từ batdongsan.vn.  
Mục tiêu của phần tiền xử lý:
- Làm sạch dữ liệu
- Chuẩn hóa định dạng
- Xử lý giá trị thiếu
- Tạo đặc trưng mới
- Chuyển đổi dữ liệu cho phù hợp mô hình học máy
- Lưu pipeline thống nhất để tái sử dụng

---

## 2. Dataset Overview
**(Sẽ cập nhật từ Mục 1 trong notebook – Data Understanding)**  
- Số dòng  
- Số cột  
- Kiểu dữ liệu  
- Mô tả từng thuộc tính  
- Nhận xét ban đầu

---

## 3. Missing Values Analysis
**(Sẽ cập nhật từ bảng Missing Values)**  
- Bảng % giá trị thiếu  
- Nhận xét từng cột  
- Chiến lược xử lý (drop / impute)

---

## 4. Data Cleaning Steps
**(Cập nhật ở Mục 2 – Data Cleaning)**  
- Chuẩn hóa text  
- Loại bỏ cột direction nếu cần  
- Imputation numeric  
- Imputation categorical  
- Xử lý outlier  
- Xử lý giá trị bất thường (Area < 10, v.v.)

---

## 5. Feature Engineering
**(Cập nhật sau khi làm Mục 3)**  
- Tách District / City  
- Tạo Price_per_m2  
- Tạo Rooms  
- Binning Area  
- Các đặc trưng mở rộng khác

---

## 6. Encoding & Scaling
**(Cập nhật sau Mục 4)**  
- One-hot encoding  
- StandardScaler cho numeric  
- Lý do chọn StandardScaler  
- Kiểm tra consistency

---

## 7. Dataset Splitting
**(Mục 5)**  
- Tỷ lệ train / val / test  
- Lý do chọn split  
- Kiểm tra phân phối Price sau split

---

## 8. Preprocessing Pipeline
**(Mục 6)**  
- Sơ đồ pipeline  
- Các bước trong ColumnTransformer  
- Lưu file preprocessor.pkl  
- Lợi ích khi dùng pipeline

---

## 9. Final Clean Dataset Summary
- Số dòng sau cleaning  
- Số cột sau encoding  
- Số đặc trưng mới  
- Thống kê mô tả mới  
- Bảng kiểm tra NA sau xử lý

---

## 10. Conclusion
Tổng kết toàn bộ phần tiền xử lý và chuẩn bị chuyển sang phần mô hình hóa (Machine Learning).

