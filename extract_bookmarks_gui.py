import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog, messagebox

def extract_bookmarks(pdf_path):
    doc = fitz.open(pdf_path)
    bookmarks = []

    def _get_bookmarks(toc, level=0):
        for item in toc:
            current_level = item[0]
            title = item[1]
            page = item[2]
            bookmarks.append(f"{' ' * (current_level - 1) * 2}{title} (Page {page})")
    
    toc = doc.get_toc()
    _get_bookmarks(toc)
    return bookmarks

def main():
    root = tk.Tk()
    root.withdraw()
    pdf_path = filedialog.askopenfilename(title="选择PDF文件", filetypes=[("PDF文件", "*.pdf")])
    if not pdf_path:
        return
    bookmarks = extract_bookmarks(pdf_path)
    
    output_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("文本文件", "*.txt")], title="保存书签文件")
    if not output_path:
        return
    
    with open(output_path, 'w', encoding='utf-8') as f:
        for bookmark in bookmarks:
            f.write(f"{bookmark}\n")
    
    messagebox.showinfo("完成", f"书签已导出到 {output_path}")

if __name__ == "__main__":
    main()
