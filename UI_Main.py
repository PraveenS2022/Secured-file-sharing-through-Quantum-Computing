import tkinter as tk
from tkinter import filedialog, messagebox
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from hashlib import sha256
from Crypto.Random import get_random_bytes

from PIL import ImageTk, Image

# Function to derive AES key from user input (using SHA-256 hash)
from PIL.ImageTk import PhotoImage


def derive_key_from_user_input(user_key, key_size=32):
    hasher = sha256()
    hasher.update(user_key.encode('utf-8'))
    return hasher.digest()[:key_size]  # Return the first key_size bytes


# AES encryption function
def aes_encrypt_file(input_file, output_file, key):
    iv = get_random_bytes(16)  # AES requires a 16-byte IV for CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)

    with open(input_file, 'rb') as f:
        plaintext = f.read()

    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    with open(output_file, 'wb') as f:
        f.write(iv + ciphertext)


# AES decryption function
def aes_decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        iv = f.read(16)  # The first 16 bytes are the IV
        ciphertext = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    with open(output_file, 'wb') as f:
        f.write(plaintext)


# Function to select a file for encryption
def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, file_path)


# Function to encrypt the selected file
def encrypt_file():
    input_file = entry_file_path.get()
    user_key = entry_key.get()

    if not input_file or not user_key:
        messagebox.showwarning("Input Error", "Please provide both a file and a key!")
        return

    output_file = input_file + ".enc"
    derived_key = derive_key_from_user_input(user_key)

    try:
        aes_encrypt_file(input_file, output_file, derived_key)
        messagebox.showinfo("Success", f"File encrypted successfully!\nSaved as {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during encryption: {str(e)}")


# Function to decrypt the selected file
def decrypt_file():
    input_file = entry_file_path.get()
    user_key = entry_key.get()

    if not input_file or not user_key:
        messagebox.showwarning("Input Error", "Please provide both a file and a key!")
        return

    if not input_file.endswith(".enc"):
        messagebox.showwarning("File Error", "Please select an encrypted (.enc) file!")
        return

    output_file = input_file.replace(".enc", "_decrypted")
    derived_key = derive_key_from_user_input(user_key)

    try:
        aes_decrypt_file(input_file, output_file, derived_key)
        messagebox.showinfo("Success", f"File decrypted successfully!\nSaved as {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during decryption: {str(e)}")


# Create the main window
root = tk.Tk()
root.geometry('600x300')
root.title("File Encryption/Decryption")
img= PhotoImage(file='1.png', master=root)
img_label= tk.Label(root, image=img)
img_label.place(x=0, y=0)

# File selection entry and button
lbl_file_path = tk.Label(root, text="File Encryption and Decryption")
lbl_file_path.grid(row=0, column=1, padx=10, pady=10)

lbl_file_path = tk.Label(root, text="Select File:")
lbl_file_path.grid(row=1, column=0, padx=10, pady=10)

entry_file_path = tk.Entry(root, width=60)
entry_file_path.grid(row=1, column=1, padx=10, pady=10)

btn_browse = tk.Button(root, text="Browse", command=select_file)
btn_browse.grid(row=1, column=2, padx=10, pady=10)

# Key input entry
lbl_key = tk.Label(root, text="Enter Key:")
lbl_key.grid(row=2, column=0, padx=10, pady=10)

entry_key = tk.Entry(root, width=50, show='*')  # Show * for security
entry_key.grid(row=2, column=1, padx=10, pady=10)

# Encrypt and Decrypt buttons
btn_encrypt = tk.Button(root, text="Encrypt", command=encrypt_file)
btn_encrypt.grid(row=3, column=1, padx=10, pady=10)

btn_decrypt = tk.Button(root, text="Decrypt", command=decrypt_file)
btn_decrypt.grid(row=4, column=1, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
