Here’s the updated README with the mention of the installer file available in the repository:

---

# PDF Utility GUI

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [User Interface](#user-interface)
- [Operations](#operations)
  - [Extracting Text](#extracting-text)
  - [Merging PDFs](#merging-pdfs)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Troubleshooting](#troubleshooting)
- [Warnings and Considerations](#warnings-and-considerations)

## Introduction
**PDF Utility GUI** is a Python application that provides a graphical user interface for performing common operations on PDF files. It allows users to extract text from PDFs and merge multiple PDF files into a single document.

## Features
- Dark-themed, user-friendly interface
- Text extraction from PDF files
- Merging multiple PDF files
- Fullscreen mode
- Resizable window

## Requirements
- Python 3.x
- `tkinter` (usually comes pre-installed with Python)
- `pypdf` library

## Installation

You can install the application by using the setup file provided in the repository.

### Method 1: Using the Installer
- Download the installer (`setup.exe`) from the GitHub repository.
- Double-click the installer to install the application on your system.
- After installation, you can launch the PDF Utility directly from your Start Menu or desktop shortcut.

### Method 2: Run the Script

1. Ensure you have Python 3.x installed on your system.
2. Install the required `pypdf` library using pip:
    ```bash
    pip install pypdf
    ```
3. Download the `pdf_utility_gui.py` file to your local machine.
4. Run the script using Python:
    ```bash
    python pdf_utility_gui.py
    ```

## Usage
Once installed, simply run the application by launching the installed program or running the Python script.

## User Interface
The application window contains the following elements:
- **Operation selection radio buttons**: "Extract Text" and "Merge PDFs"
- **File selection button**
- **Process button**

## Operations

### Extracting Text
1. Select the "Extract Text" operation.
2. Click "Browse Files" and select a single PDF file.
3. Click "Process".
4. The extracted text will appear in a new window.

### Merging PDFs
1. Select the "Merge PDFs" operation.
2. Click "Browse Files" and select multiple PDF files.
3. Click "Process".
4. Choose a location and filename for the merged PDF.
5. A success message will appear once the merge is complete.

## Keyboard Shortcuts
- `F11`: Toggle fullscreen mode
- `Esc`: Exit fullscreen mode

## Troubleshooting
- **FileNotFoundError**: Ensure that the selected PDF files exist and have not been moved or deleted.
- **PermissionError**: Make sure you have the necessary permissions to read the input files and write to the output location.
- **Memory Error**: When processing very large PDF files, you may encounter memory issues. Try closing other applications or using smaller PDF files.

## Warnings and Considerations
- **File Selection**: Always verify that you've selected the correct files before processing.
- **Merged File Size**: When merging multiple PDFs, be aware that the resulting file may be quite large.
- **Text Extraction Accuracy**: The quality of text extraction can vary depending on how the PDF was created. Some PDFs (e.g., scanned documents) may not yield accurate results.
- **Processing Time**: Large PDF files may take some time to process. The application may appear unresponsive during this time, but it is still working.
- **Output Location**: When merging PDFs, ensure you have write permissions for the chosen output location.
- **File Overwriting**: The application will overwrite existing files without warning when saving merged PDFs. Always double-check the save location and filename.
- **Unsupported PDF Features**: Complex PDFs with forms, encryption, or other advanced features may not be fully supported.
- **Error Handling**: While the application handles basic errors, unexpected issues may cause it to crash. Always save your work before processing important documents.

--- 

This version directs users to the setup file available in your GitHub repository for a more user-friendly installation process.
