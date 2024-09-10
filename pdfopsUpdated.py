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
        master.geometry("800x600")  # Increased window size
        master.resizable(True, True)  # Allow resizing
        master.bind("<F11>", self.toggle_fullscreen)  # Bind F11 key to toggle full screen
        master.bind("<Escape>", self.end_fullscreen)  # Bind Esc key to exit full screen

        # Set dark theme
        master.configure(bg='#333333')

        # Create frames for better organization
        self.operation_frame = tk.Frame(master, bg='#333333')
        self.operation_frame.pack(pady=20)

        self.file_frame = tk.Frame(master, bg='#333333')
        self.file_frame.pack(pady=20)

        self.process_frame = tk.Frame(master, bg='#333333')
        self.process_frame.pack(pady=20)

        # Operation selection
        self.operation = tk.StringVar(value="extract")
        tk.Label(self.operation_frame, text="Select operation:", bg='#333333', fg='white', font=('Helvetica', 18)).pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(self.operation_frame, text="Extract Text", variable=self.operation, value="extract", bg='#333333', fg='white', font=('Helvetica', 18)).pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(self.operation_frame, text="Merge PDFs", variable=self.operation, value="merge", bg='#333333', fg='white', font=('Helvetica', 18)).pack(side=tk.LEFT, padx=10)

        # File selection
        tk.Label(self.file_frame, text="Select PDF file(s):", bg='#333333', fg='white', font=('Helvetica', 18)).pack(side=tk.LEFT, padx=10)
        self.file_button = tk.Button(self.file_frame, text="Browse Files", command=self.browse_files, bg='#444444', fg='white', font=('Helvetica', 18))
        self.file_button.pack(side=tk.LEFT, padx=10)

        # Process button
        self.process_button = tk.Button(self.process_frame, text="Process", command=self.process, bg='#444444', fg='white', font=('Helvetica', 18))
        self.process_button.pack(pady=20)

        self.selected_files = []
        self.fullscreen = False

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
        text_window.geometry("800x600")

        text_area = scrolledtext.ScrolledText(text_window, wrap=tk.WORD, font=('Helvetica', 18))
        text_area.pack(expand=True, fill='both')
        text_area.insert(tk.END, text)
        text_area.config(state=tk.DISABLED)  # Make the text area read-only

    def toggle_fullscreen(self, event=None):
        self.fullscreen = not self.fullscreen
        self.master.attributes("-fullscreen", self.fullscreen)

    def end_fullscreen(self, event=None):
        self.fullscreen = False
        self.master.attributes("-fullscreen", False)

# Main function to run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    gui = PDFUtilityGUI(root)
    root.mainloop()
