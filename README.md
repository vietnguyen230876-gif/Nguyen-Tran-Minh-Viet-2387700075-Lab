# Bài 1: Cơ sở lập trình bảo mật và kiểm tra đầu vào (Secure Input Validation & Secure Logger)

Dự án thực hành môn lập trình bảo mật tập trung vào các kỹ thuật phòng chống lỗ hổng ứng dụng web, bao gồm: kiểm tra và làm sạch dữ liệu đầu vào, ghi nhật ký ưu tiên bảo mật (Secure Logging), phát hiện chỉnh sửa log trái phép (Tamper Detection) và bảo mật mã nguồn qua Git Hooks.

---

## 📁 Cấu trúc dự án
```text
secure-validator-lab/
├── .githooks/
│   └── pre-commit         # Git hook quét thông tin nhạy cảm trước khi commit
├── securevalidator/
│   ├── __init__.py
│   └── core.py            # Các hàm validate email, url, filename và sanitize SQLi, XSS
├── securelogger/
│   ├── __init__.py
│   └── logger.py          # Hệ thống Secure Logger (JSON, PII Masking, Tamper Detection)
├── app.py                 # API Flask chính
├── requirements.txt       # Các thư viện phụ thuộc
└── README.md              # Tài liệu hướng dẫn dự án