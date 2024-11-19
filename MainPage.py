import tkinter as tk
from page1 import Page1
from page2 import Page2
from page3 import Page3
from page4 import Page4
from page5 import Page5
from qiskit import IBMQ

# Initialize IBMQ account
def initialize_ibmq():
    try:
        IBMQ.save_account('35ac34752441e928ce5dcb68dec15f93db837e39547c24554ff77060f72761016e1d8bf8e35b409bb63f0bc20962e185087eb3a53360576f6c65925259cdc610', overwrite=True)
        IBMQ.load_account()
    except Exception as e:
        print("Error initializing IBMQ:", e)

# Call the initialize function
initialize_ibmq()

# Initialize main window
root = tk.Tk()
root.title("File Encryption and Decryption Quantum Computing")
root.geometry("1000x600")

# Define a function to switch between pages
def show_frame(frame):
    frame.tkraise()

# Create a container frame for sidebar and content
container = tk.Frame(root)
container.pack(fill="both", expand=True)

# Create the sidebar frame
sidebar = tk.Frame(container, width=150, bg="lightgreen")
sidebar.pack(side="left", fill="y")

# Create the main content frame where pages will be displayed
content = tk.Frame(container, bg="white")
content.pack(side="right", fill="both", expand=True)

# Initialize pages from separate files
pages = {
    "Home": Page1(content),
    "File Encryption": Page2(content),
    "Hide Image in text": Page3(content),
    "Send Email": Page4(content),
    "Contact us": Page5(content)
}

# Stack pages on top of each other
for page in pages.values():
    page.place(relwidth=1, relheight=1)

# Sidebar buttons for page navigation
button_config = {
    "background": "Green",
    "foreground": "white",
    "font": ("arial", 10, "bold"),
    "width": 30
}

for label, page in pages.items():
    btn = tk.Button(sidebar, text=label, command=lambda p=page: show_frame(p), **button_config)
    btn.pack(pady=10)

# Display the first page by default
show_frame(pages["Home"])

# Run the main loop
root.mainloop()
