# 🗜️ File Compression GUI  
### A simple GUI tool for compressing and decompressing files using Python and zlib

---

## 📝 Project Overview  
This project is a lightweight **File Compression and Decompression Tool** built using **Python** and the built-in **zlib** compression library. The application features an intuitive **Graphical User Interface (GUI)** built with `Tkinter`, allowing users to easily compress and decompress local files with a single click.

---

## 🎯 Objectives  

### 🧾 File Compression & Decompression:  
- Select a file from the local system using a file browser.  
- Compress the selected file using the `zlib` compression algorithm.  
- Save the compressed file with a `.cmp` extension.  
- Decompress any previously compressed `.cmp` file back to its original format.

### 🖥️ User Interface:  
- A clean and minimal GUI interface using Python's `Tkinter`.  
- Interactive buttons for **Browse**, **Compress**, and **Decompress**.  
- Message popups to indicate success or failure of the operation.

---

## 🔍 Key Insights  

- Uses **Python's built-in `zlib` module**, so no third-party compression library is needed.  
- Handles binary files, including `.txt`, `.jpg`, `.pdf`, etc.  
- Automatically appends `.cmp` during compression and removes it during decompression.  
- Prevents overwriting original files by generating new output filenames.  
- Provides meaningful error handling through message pop-ups.

---

## 💡 Recommendations  

### 🌟 Feature Enhancements:  
- Add drag-and-drop support for faster file selection.  
- Allow compressing multiple files or entire folders into `.zip` or `.tar.gz`.  
- Support different compression levels and algorithms.  
- Show file size before and after compression for comparison.

### 🧠 Usability Improvements:  
- Display progress bars during long compress/decompress tasks.  
- Add support for dark mode or themes in the GUI.  
- Save a log of compressed/decompressed files and timestamps.

### 📦 Code Optimization:  
- Refactor the GUI and backend logic into separate modules.  
- Use `threading` or `multiprocessing` to keep the GUI responsive.  
- Add unit tests for compression and decompression functions.

---

## ✅ Conclusion  
The **File Compression GUI** project is a user-friendly desktop utility that demonstrates how to integrate **Python's GUI capabilities** with **file handling and compression** techniques. It's an ideal starting point for learners looking to build desktop applications or understand data compression using Python. With further enhancements, it can evolve into a full-featured file management and backup utility.
