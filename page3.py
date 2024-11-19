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
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
class Page3(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")

        def encode_text_in_image(image_path, text):
            qc = QuantumCircuit(2)
            qc.h(0)
            qc.cx(0, 1)
            image = Image.open(image_path)
            pixels = image.load()

            binary_text = ''.join([format(ord(char), '08b') for char in text]) + '11111111'  # Terminator
            data_index = 0

            for y in range(image.height):
                for x in range(image.width):
                    if data_index < len(binary_text):
                        r, g, b = pixels[x, y]
                        r = (r & ~1) | int(binary_text[data_index])
                        data_index += 1
                        if data_index < len(binary_text):
                            g = (g & ~1) | int(binary_text[data_index])
                            data_index += 1
                        if data_index < len(binary_text):
                            b = (b & ~1) | int(binary_text[data_index])
                            data_index += 1
                        pixels[x, y] = (r, g, b)

            return image

        def decode_text_from_image(image_path):
            qc = QuantumCircuit(2)
            qc.h(0)
            qc.cx(0, 1)
            image = Image.open(image_path)
            pixels = image.load()

            binary_text = ''
            for y in range(image.height):
                for x in range(image.width):
                    r, g, b = pixels[x, y]
                    binary_text += str(r & 1)  # Get the LSB of red
                    binary_text += str(g & 1)  # Get the LSB of green
                    binary_text += str(b & 1)  # Get the LSB of blue

            # Convert binary to characters
            text = ''
            for i in range(0, len(binary_text), 8):
                byte = binary_text[i:i + 8]
                if byte == '11111111':  # Terminator
                    break
                text += chr(int(byte, 2))

            return text

        def encode():
            image_path = filedialog.askopenfilename(title="Select an Image",
                                                    filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
            if image_path:
                text_file_path = filedialog.askopenfilename(title="Select a Text File",
                                                            filetypes=[("Text Files", "*.txt")])
                if text_file_path:
                    with open(text_file_path, "r") as file:
                        text = file.read()
                    encoded_image = encode_text_in_image(image_path, text)
                    encoded_image.save("encoded_image.png")
                    messagebox.showinfo("Success",
                                        "Text has been encoded into the image and saved as 'encoded_image.png'.")

        def decode():
            image_path = filedialog.askopenfilename(title="Select an Encoded Image",
                                                    filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
            if image_path:
                decoded_text = decode_text_from_image(image_path)

                # Save decoded text to a new text file
                save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
                if save_path:
                    with open(save_path, "w") as file:
                        file.write(decoded_text)
                    messagebox.showinfo("Success", f"The hidden text has been saved to '{save_path}'.")

        # Tkinter GUI setup


        encode_button = tk.Button(self, text="Encode Text from File into Image", command=encode)
        encode_button.pack(pady=10)

        decode_button = tk.Button(self, text="Decode Text from Image to File", command=decode)
        decode_button.pack(pady=10)
