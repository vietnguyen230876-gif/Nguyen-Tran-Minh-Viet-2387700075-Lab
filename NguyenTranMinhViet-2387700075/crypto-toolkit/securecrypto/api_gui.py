import tkinter as tk
from tkinter import filedialog
from securecrypto import aes_utils

def encrypt():
    file = filedialog.askopenfilename()
    pw = password_entry.get()
    key = aes_utils.encrypt_file_aes(file, pw)
    result_label.config(text=f"Key: {key}")

def decrypt():
    file = filedialog.askopenfilename()
    pw = password_entry.get()
    out = aes_utils.decrypt_file_aes(file, pw)
    result_label.config(text=f"Output: {out}")

root = tk.Tk()
root.title("SecureCrypto GUI")
root.geometry("450x250")

password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=10)
tk.Button(root, text="Encrypt", command=encrypt).pack(pady=5)
tk.Button(root, text="Decrypt", command=decrypt).pack(pady=5)
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()