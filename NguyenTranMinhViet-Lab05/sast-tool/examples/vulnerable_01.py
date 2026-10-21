password = "123456"  # Hardcoded password[cite: 5]

import pickle  # Có thể gây nguy hiểm[cite: 5]

def unsafe_func(data):
    return eval(data)  # Rất nguy hiểm, eval dùng tùy ý[cite: 5]

def safe_func():
    print("Hello world!")

if __name__ == "__main__":
    unsafe_func("2+2")
    safe_func()