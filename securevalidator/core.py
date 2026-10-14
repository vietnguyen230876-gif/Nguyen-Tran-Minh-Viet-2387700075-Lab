import re
import html

def validate_email(email):
    if not email or not isinstance(email, str):
        return False
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))

def validate_url(url):
    if not url or not isinstance(url, str):
        return False
    pattern = r"^https?://[^\s/$.?#].[^\s]*$"
    return bool(re.match(pattern, url))

def validate_filename(filename):
    if not filename or not isinstance(filename, str):
        return False
    # Chống Path Traversal (kiểm tra dấu ../ hoặc tuyệt đối)
    if ".." in filename or "/" in filename or "\\" in filename:
        return False
    pattern = r"^[\w\.-]+$"
    return bool(re.match(pattern, filename))

def sanitize_sql_input(val):
    if not val or not isinstance(val, str):
        return ""
    # Loại bỏ ký tự nguy hiểm cơ bản chống SQL Injection
    dangerous_patterns = ["--", ";", "OR", "SELECT", "DROP", "UNION"]
    result = val
    for p in dangerous_patterns:
        result = result.replace(p, "")
    return result.strip()

def sanitize_html_input(val):
    if not val or not isinstance(val, str):
        return ""
    # Escape HTML để chống XSS
    return html.escape(val)