import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import pypdf
from pypdf import PdfReader, PdfWriter
import os

def extract_text(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n\n"
    return text

def merge_pdfs(file_paths, output_path):
    merger = PdfWriter()
    for pdf in file_paths:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()

class PDFUtilityGUI:
    def __init__(self, master):
        self.master = master
        master.title("PDF Utility")
        master.geometry("400x200")

        self.operation = tk.StringVar(value="extract")
        
        tk.Label(master, text="Select operation:").pack(pady=5)
        
        tk.Radiobutton(master, text="Extract Text", variable=self.operation, value="extract").pack()
        tk.Radiobutton(master, text="Merge PDFs", variable=self.operation, value="merge").pack()

        tk.Label(master, text="Select PDF file(s):").pack(pady=5)
        
        self.file_button = tk.Button(master, text="Browse Files", command=self.browse_files)
        self.file_button.pack(pady=5)

        self.process_button = tk.Button(master, text="Process", command=self.process)
        self.process_button.pack(pady=10)

        self.selected_files = []

    def browse_files(self):
        if self.operation.get() == "extract":
            files = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        else:
            files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        
        if isinstance(files, str):  # Single file for extract
            self.selected_files = [files] if files else []
        else:  # Multiple files for merge
            self.selected_files = list(files)
        
        num_files = len(self.selected_files)
        self.file_button.config(text=f"{num_files} file{'s' if num_files != 1 else ''} selected")

    def process(self):
        if not self.selected_files:
            messagebox.showerror("Error", "Please select PDF file(s).")
            return

        if self.operation.get() == "extract":
            text = extract_text(self.selected_files[0])
            self.show_extracted_text(text)
        else:
            if len(self.selected_files) < 2:
                messagebox.showerror("Error", "Please select at least two PDF files to merge.")
                return
            output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
            if output_path:
                merge_pdfs(self.selected_files, output_path)
                messagebox.showinfo("Success", f"PDFs merged successfully. Saved as {output_path}")

    def show_extracted_text(self, text):
        text_window = tk.Toplevel(self.master)
        text_window.title("Extracted Text")
        text_window.geometry("600x400")

        text_area = scrolledtext.ScrolledText(text_window, wrap=tk.WORD)
        text_area.pack(expand=True, fill='both')
        text_area.insert(tk.END, text)
        text_area.config(state='disabled')

root = tk.Tk()
gui = PDFUtilityGUI(root)
root.mainloop()
