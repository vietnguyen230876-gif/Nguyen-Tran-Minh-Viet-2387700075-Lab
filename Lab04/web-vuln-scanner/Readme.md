Báo cáo Thực hành: Web Vulnerability Scanner

Dự án công cụ quét lỗ hổng bảo mật web (Web Vulnerability Scanner) hỗ trợ kiểm tra các lỗ hổng phổ biến như SQL Injection, SSRF, CSRF và XSS thông qua giao diện dòng lệnh (CLI) và giao diện người dùng (Web UI) xây dựng bằng Flask.

📁 1. Cấu trúc thư mục dự án trên GitHub

Để các hình ảnh minh chứng hiển thị chính xác trên giao diện GitHub, hãy lưu trữ các tệp ảnh vào thư mục images/ nằm cùng cấp với tệp README.md theo cấu trúc sau:

web-vulner-scanner/
├── images/
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   ├── 4.png
│   └── 5.png
├── ui/
│   └── app.py
├── tests/
├── main.py
└── README.md


🛠️ 2. Các bước thực hiện & Phân tích chi tiết

Bước 1: Kiểm thử Tự động (Unit Test)

Thực hiện chạy bộ kiểm thử đơn vị (unittest) để kiểm tra tính chính xác của các mô-đun phát hiện lỗ hổng trước khi vận hành thực tế.

Lệnh thực thi:

python -m unittest discover tests


Hình ảnh minh chứng:![Chạy Unit Test](images/1.png)

Phân tích kết quả:

Hệ thống đã tìm kiếm và thực thi thành công 9 kịch bản kiểm thử (test cases) nằm trong thư mục tests.

Thời gian phản hồi nhanh chóng: 0.043 giây.

Kết quả trả về OK màu xanh, xác nhận các hàm kiểm tra phát hiện lỗ hổng (SQLi, SSRF, CSRF, XSS) hoạt động chính xác theo đúng logic thiết kế ban đầu.

Bước 2: Quét Lỗ hổng bằng Giao diện Dòng lệnh (CLI)

Thực thi chương trình chính thông qua CLI để kiểm tra khả năng phát hiện lỗ hổng và in kết quả trực tiếp ra màn hình terminal.

Lệnh thực thi:

python main.py


Hình ảnh minh chứng:![Kết quả quét CLI](images/2.png)

Phân tích kết quả:
Báo cáo lỗ hổng (=== Vulnerability Report ===) quét được bao gồm:

Tham số id: Phát hiện nguy cơ Potential SQL Injection với mức độ rủi ro Critical (Chí mạng).

Tham số N/A: Không ghi nhận lỗ hổng rủi ro (Risk: None).

Tham số url: Phát hiện nguy cơ Potential SSRF to internal resource (Lỗ hổng Server-Side Request Forgery truy cập tài nguyên nội bộ) với mức độ rủi ro High (Cao).

Bước 3: Khởi chạy Máy chủ Giao diện Web (Flask UI Server)

Khởi chạy ứng dụng Web Flask để cung cấp giao diện tương tác trực quan cho người dùng.

Lệnh thực thi:

python ui/app.py


Hình ảnh minh chứng:![Khởi chạy Flask App](images/3.png)

Phân tích kết quả:

Máy chủ web Flask khởi động thành công ở chế độ phát triển (Debug mode: on).

Ứng dụng lắng nghe và phục vụ các kết nối tại địa chỉ cục bộ: http://127.0.0.1:5000.

Trình khắc lỗi (Debugger) đã kích hoạt kèm mã PIN xác thực (327-492-248).

Bước 4: Thiết lập Thông số Quét trên Giao diện Web

Nguời dùng truy cập địa chỉ http://127.0.0.1:5000 trên trình duyệt web để thiết lập cấu hình kiểm thử.

Hình ảnh minh chứng:![Giao diện Web Scanner](images/4.png)

Phân tích kết quả:

Trường nhập liệu URL: Cho phép điền địa chỉ mục tiêu cần quét (ví dụ trong hình là http://example.com).

Tùy chọn công cụ kiểm thử: Cung cấp các checkbox linh hoạt cho phép kích hoạt từng loại hình kiểm thử:

XSS Scanner: Quét lỗ hổng Cross-Site Scripting.

SQL Injection Tester: Kiểm tra lỗ hổng tiêm lệnh SQL.

CSRF Detector: Phát hiện thiếu sót bảo mật chống Cross-Site Request Forgery.

SSRF Tester: Kiểm tra lỗ hổng giả mạo yêu cầu từ phía máy chủ.

Nút bấm "Bắt đầu kiểm thử" kích hoạt quá trình quét trên máy chủ.

Bước 5: Xem Kết quả Báo cáo Lỗ hổng trên Giao diện Web

Sau khi hoàn tất quét, trang web tự động chuyển hướng và hiển thị kết quả chi tiết lỗ hổng phát hiện được.

Hình ảnh minh chứng:![Báo cáo lỗ hổng Web UI](images/5.png)

Phân tích kết quả:

Loại lỗ hổng: Ghi nhận báo cáo thuộc nhóm Lỗ hổng chưa xác định chi tiết vị trí.

Mô tả chi tiết: No CSRF token found, vulnerable to CSRF — Hệ thống phát hiện biểu mẫu/trang web không trang bị CSRF Token, dẫn đến nguy cơ bị tấn công giả mạo yêu cầu.

Mức độ rủi ro: Medium (Trung bình).

Tích hợp liên kết "Quay lại trang kiểm thử" giúp người dùng dễ dàng chuyển về trang chủ để thực hiện các lượt quét tiếp theo.

3. Tổng kết

Hệ thống đã vận hành ổn định trên cả 2 môi trường Dòng lệnh (CLI) và Giao diện Web (Flask UI).

Các module quét bảo mật vượt qua bộ kiểm thử tự động unittest đạt chuẩn.

Công cụ có khả năng phát hiện chính xác các rủi ro bảo mật thực tế như SQL Injection, SSRF, CSRF và đưa ra cảnh báo mức độ nguy hiểm cụ thể.