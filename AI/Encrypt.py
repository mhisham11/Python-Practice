import tkinter as tk
from tkinter import messagebox
import hashlib
import os
import base64

# 🔐 Turn password into a usable key
def derive_key(password: str, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)

# 🔄 XOR encryption/decryption
def xor_data(data: bytes, key: bytes) -> bytes:
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

# 🔒 Encrypt
def encrypt_text():
    text = input_box.get("1.0", tk.END).strip()
    password = password_entry.get()

    if not text or not password:
        messagebox.showwarning("Warning", "Enter both text and password.")
        return

    try:
        salt = os.urandom(16)
        key = derive_key(password, salt)
        encrypted = xor_data(text.encode(), key)

        result = base64.urlsafe_b64encode(salt + encrypted).decode()

        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, result)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# 🔓 Decrypt
def decrypt_text():
    text = input_box.get("1.0", tk.END).strip()
    password = password_entry.get()

    if not text or not password:
        messagebox.showwarning("Warning", "Enter both text and password.")
        return

    try:
        raw = base64.urlsafe_b64decode(text.encode())
        salt = raw[:16]
        encrypted = raw[16:]

        key = derive_key(password, salt)
        decrypted = xor_data(encrypted, key).decode()

        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, decrypted)

    except Exception:
        messagebox.showerror(
            "Error",
            "Decryption failed. Wrong password or invalid text."
        )

# 📋 Paste input
def paste_input():
    try:
        # Try to grab text from the system clipboard
        clipboard_text = root.clipboard_get()
        input_box.delete("1.0", tk.END)
        input_box.insert(tk.END, clipboard_text)
    except tk.TclError:
        # Fails gracefully if the clipboard is empty or contains non-text data
        messagebox.showinfo("Notice", "No text found in clipboard.")

# 📑 Copy output
def copy_output():
    text = output_box.get("1.0", tk.END).strip()
    if text:
        root.clipboard_clear()
        root.clipboard_append(text)
        messagebox.showinfo("Copied", "Copied to clipboard!")

# 🧹 Clear
def clear_all():
    input_box.delete("1.0", tk.END)
    output_box.delete("1.0", tk.END)
    password_entry.delete(0, tk.END)

# 🖥️ GUI
root = tk.Tk()
root.title("Simple Encryptor (No Install Needed)")
root.geometry("640x440") # Slightly taller to fit the credit label

tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack(fill="x", padx=10, pady=5)

tk.Label(root, text="Input").pack()
input_box = tk.Text(root, height=8, wrap="word")
input_box.pack(fill="both", padx=10, pady=5, expand=True)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Encrypt", command=encrypt_text).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Decrypt", command=decrypt_text).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Paste Input", command=paste_input).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Copy Output", command=copy_output).grid(row=0, column=3, padx=5)
tk.Button(btn_frame, text="Clear", command=clear_all).grid(row=0, column=4, padx=5)

tk.Label(root, text="Output").pack()
output_box = tk.Text(root, height=8, wrap="word")
output_box.pack(fill="both", padx=10, pady=5, expand=True)

# ✍️ Credits Label
credit_label = tk.Label(root, text="Program created by Hisham", fg="gray", font=("Arial", 9))
credit_label.pack(side="bottom", pady=5)

root.mainloop()