# Báo cáo Bài lab: Bảo mật Đầu vào & Kiểm thử Lỗ hổng (Secure Input Validation)

## 1. Giải thích về các hình thức tấn công (Attack Explanation)
- **SQL Injection (SQLi):** Kẻ tấn công chèn các cú pháp SQL độc hại (vd: \1=1 --\) vào dữ liệu đầu vào để thao túng câu lệnh truy vấn gốc, qua mặt cơ chế kiểm tra dữ liệu.
- **Cross-Site Scripting (XSS):** Kẻ tấn công tiêm mã kịch bản độc hại (vd: \<script>alert(1)</script>\) vào ứng dụng để thực thi mã độc trên trình duyệt nạn nhân.

## 2. How to bypass (Cách thực hiện tấn công / bypass)
- **Bypass SQLi:** Sử dụng các payload chứa toán tử logic luôn đúng kèm ký tự chú thích (vd: \"OR 1=1 --"\ hoặc \"1' OR '1'='1"\) để làm sai lệch logic kiểm tra.
- **Bypass XSS:** Sử dụng các payload thay thế thẻ script (vd: \<img src=x onerror=alert(1)>\) hoặc dùng các kỹ thuật mã hóa ký tự để lách qua bộ lọc thô sơ.

## 3. Tại sao bypass được? (Why it can be bypassed)
- **Khi chưa có bảo vệ:** Ứng dụng xử lý trực tiếp "dữ liệu bẩn" từ người dùng (Untrusted Input) mà không kiểm định, dẫn đến việc trình duyệt hoặc hệ quản trị cơ sở dữ liệu hiểu nhầm mã độc thành lệnh thực thi hợp lệ.
- **Giải pháp khắc phục:** Ứng dụng tích hợp bộ lọc kiểm tra nghiêm ngặt (\securevalidator\), thực hiện Escape HTML chống XSS và lọc bỏ các từ khóa/ký tự đặc biệt chống SQLi, giúp vô hiệu hóa hoàn toàn payload tấn công.

## 4. Hình ảnh minh chứng kết quả (Screenshots)

### Minh chứng 1
![Anh 1](https://raw.githubusercontent.com/vietnguyen230876-gif/Nguyen-Tran-Minh-Viet-2387700075-Lab/main/image/1.png)

### Minh chứng 2
![Anh 2](https://raw.githubusercontent.com/vietnguyen230876-gif/Nguyen-Tran-Minh-Viet-2387700075-Lab/main/image/2.png)

### Minh chứng 3
![Anh 3](https://raw.githubusercontent.com/vietnguyen230876-gif/Nguyen-Tran-Minh-Viet-2387700075-Lab/main/image/3.png)

### Minh chứng 4
![Anh 4](https://raw.githubusercontent.com/vietnguyen230876-gif/Nguyen-Tran-Minh-Viet-2387700075-Lab/main/image/4.png)
