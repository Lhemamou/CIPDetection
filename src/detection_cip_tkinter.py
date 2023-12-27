import re
import pandas as pd
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog
import os

# Function to find unique numbers in text
def find_unique_numbers(string):
    pattern = r'\b\d{7}\b|\b\d{13}\b'
    matches = re.findall(pattern, string)
    return matches

# Function to process text and show results
def process_text():
    text = text_area.get('1.0', tk.END)
    unique_numbers = find_unique_numbers(text)
    result_area.delete('1.0', tk.END)
    result_area.insert('1.0', '\n'.join(unique_numbers))

# Function to save results to CSV
def save_to_csv():
    data = result_area.get('1.0', tk.END).strip()
    if data:
        numbers = data.split('\n')
        df = pd.DataFrame({'Number': numbers, 'Value': [1] * len(numbers)})
        filepath = filedialog.asksaveasfilename(defaultextension=".csv",
                                                filetypes=[("CSV Files", "*.csv")])
        if filepath:
            df.to_csv(filepath, index=False, header=False, sep=';')
            messagebox.showinfo("Info", "File saved successfully")
    else:
        messagebox.showwarning("Warning", "No data to save")

# Function to clear the text area
def clear_text():
    text_area.delete('1.0', tk.END)

# Creating main window
root = tk.Tk()
root.title("Unique Number Finder")

# Text area for input
text_area = scrolledtext.ScrolledText(root, height=10)
text_area.pack(pady=10)

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

# Button to process text
process_button = tk.Button(button_frame, text="Process Text", command=process_text)
process_button.grid(row=0, column=0, padx=5)

# Button to clear the text area
clear_button = tk.Button(button_frame, text="Clear Text", command=clear_text)
clear_button.grid(row=0, column=1)

# Area to display results
result_area = scrolledtext.ScrolledText(root, height=10)
result_area.pack(pady=10)

# Button to save to CSV
save_button = tk.Button(root, text="Save to CSV", command=save_to_csv)
save_button.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()