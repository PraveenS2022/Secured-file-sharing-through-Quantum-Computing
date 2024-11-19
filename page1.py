import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Import PIL for handling images


class Page1(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")

        # Title label
        title = tk.Label(self, text="File Encryption and Decryption using AES", font=("Arial", 24), bg="white")
        title.pack(pady=10)

        # Description label
        description = tk.Label(self, text="A secured file sharing system using AES encryption, decryption, steganography and cloud storage involves encrypting \n"
                                          "sensitive data with the AES algorithm, embedding the encryption key within a seemingly innocuous carrier file \n"
                                          "(like an image) using steganography, and then storing the encrypted data along with the stego carrier file on a \n"
                                          "cloud storage platform, ensuring only authorized users with the decryption key can access the original data\n"
                                          " It can affect various parts, including the lips, tongue, cheeks, gums, and tonsils.",
                               font=("Arial", 14), bg="white", wraplength=500, justify="left")
        description.pack(pady=10)

        # Displaying an image
        try:
            # Open the image file and resize it
            image = Image.open("1.png")  # Replace with your image path
            image = image.resize((250, 150), Image.LANCZOS)
            image_tk = ImageTk.PhotoImage(image)

            # Create a label to display the image
            image_label = tk.Label(self, image=image_tk, bg="white")
            image_label.image = image_tk  # Keep a reference to avoid garbage collection
            image_label.pack(pady=10)
        except Exception as e:
            error_label = tk.Label(self, text="Image could not be loaded.", font=("Arial", 12), bg="white", fg="red")
            error_label.pack(pady=10)
            print(f"Error loading image: {e}")

        # Additional content or links
        more_info = tk.Label(self, text="Explore more by navigating through the sidebar!",
                             font=("Arial", 12), bg="white")
        more_info.pack(pady=20)
