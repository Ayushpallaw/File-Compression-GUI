# file_compression_project.py

import os
import zlib
import tkinter as tk
from tkinter import filedialog, messagebox

# ------------------------
# File Compression Module
# ------------------------
def compress_file(input_path, output_path):
    with open(input_path, 'rb') as f_in:
        data = f_in.read()
        compressed_data = zlib.compress(data, level=9)
    with open(output_path, 'wb') as f_out:
        f_out.write(compressed_data)

# --------------------------
# File Decompression Module
# --------------------------
def decompress_file(input_path, output_path):
    with open(input_path, 'rb') as f_in:
        compressed_data = f_in.read()
        original_data = zlib.decompress(compressed_data)
    with open(output_path, 'wb') as f_out:
        f_out.write(original_data)

# ------------------
# Utility Functions
# ------------------
def browse_input_file(entry_box):
    file_path = filedialog.askopenfilename(title="Select file")
    if file_path:
        entry_box.delete(0, tk.END)
        entry_box.insert(0, file_path)

def compress_via_gui(entry):
    input_path = entry.get()
    if not input_path:
        messagebox.showerror("Error", "Please select a file to compress.")
        return
    output_path = input_path + ".cmp"
    try:
        compress_file(input_path, output_path)
        messagebox.showinfo("Success", f"Compressed to: {output_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decompress_via_gui():
    input_path = filedialog.askopenfilename(title="Select compressed file")
    if not input_path:
        return
    output_path = os.path.splitext(input_path)[0] + "_decompressed" + os.path.splitext(input_path)[1].replace(".cmp", "")
    try:
        decompress_file(input_path, output_path)
        messagebox.showinfo("Success", f"Decompressed to: {output_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---------------------
# GUI Design Interface
# ---------------------
def launch_gui():
    window = tk.Tk()
    window.title("Python File Compressor & Decompressor")
    window.geometry("550x200")

    input_label = tk.Label(window, text="Select File:")
    input_entry = tk.Entry(window, width=50)
    browse_button = tk.Button(window, text="Browse", command=lambda: browse_input_file(input_entry))

    compress_button = tk.Button(window, text="Compress File", width=20, command=lambda: compress_via_gui(input_entry))
    decompress_button = tk.Button(window, text="Decompress File", width=20, command=decompress_via_gui)

    input_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    input_entry.grid(row=0, column=1, padx=5, pady=10)
    browse_button.grid(row=0, column=2, padx=5)

    compress_button.grid(row=1, column=1, pady=10)
    decompress_button.grid(row=2, column=1, pady=10)

    window.mainloop()

# ----------------------
# Main Entry Point
# ----------------------
if __name__ == "__main__":
    launch_gui()
