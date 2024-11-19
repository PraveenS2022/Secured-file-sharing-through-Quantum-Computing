import tkinter as tk
import tkinter as tk
import os
from tkinter import messagebox
from tkinter import filedialog, messagebox
from tkinter import filedialog, messagebox
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from hashlib import sha256
from Crypto.Random import get_random_bytes
from qiskit import QuantumCircuit
#from qiskit_aer import Aer

from qiskit_ibm_runtime import QiskitRuntimeService

from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
class Page2(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")

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
            # Create a quantum circuit

            qc = QuantumCircuit(2)
            qc.h(0)
            qc.cx(0, 1)
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
            # Create a quantum circuit
            qc = QuantumCircuit(2)
            qc.h(0)
            qc.cx(0, 1)
            input_file = entry_file_path.get()
            user_key = entry_key.get()

            if not input_file or not user_key:
                messagebox.showwarning("Input Error", "Please provide both a file and a key!")
                return

            output_file = filedialog.asksaveasfilename(  defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],    title="Save as"
    )
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

            if not input_file.endswith(".txt"):
                messagebox.showwarning("File Error", "Please select an encrypted (.enc) file!")
                return

            output_file = input_file.replace(".txt", ".txt")  # Change to .txt extension
            derived_key = derive_key_from_user_input(user_key)

            try:
                aes_decrypt_file(input_file, output_file, derived_key)
                messagebox.showinfo("Success", f"File decrypted successfully!\nSaved as {output_file}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred during decryption: {str(e)}")

        # Create the main window


        # File selection entry and button
        lbl_file_path = tk.Label(self, text="File Encryption and Decryption")
        lbl_file_path.place(relx=0.4,rely=0.05)

        lbl_select_file = tk.Label(self, text="Select File:")
        lbl_select_file.place(relx=0.10,rely=0.10) # Align right

        entry_file_path = tk.Entry(self, width=60)
        entry_file_path.place(relx=0.20,rely=0.10)  # Center this entry

        btn_browse = tk.Button(self, text="Browse", command=select_file)
        btn_browse.place(relx=0.80,rely=0.10)  # No sticky needed for the button

        # Key input entry
        lbl_key = tk.Label(self, text="Enter Key:")
        lbl_key.place(relx=0.10,rely=0.20)   # Align right

        entry_key = tk.Entry(self, width=60, show='*')  # Show * for security
        entry_key.place(relx=0.20,rely=0.20)  # Center this entry

        # Encrypt and Decrypt buttons
        btn_encrypt = tk.Button(self, text="Encrypt", command=encrypt_file)
        btn_encrypt.place(relx=0.40,rely=0.30)  # Center button

        btn_decrypt = tk.Button(self, text="Decrypt", command=decrypt_file)
        btn_decrypt.place(relx=0.40,rely=0.40)   # Center button

