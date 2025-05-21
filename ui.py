import tkinter as tk
from tkinter import filedialog, messagebox
from logic import load_excel_data, generate_waybill
from database import init_db, save_to_database

def launch_app():
    init_db()

    root = tk.Tk()
    root.title("Waybill Generator")

    tk.Label(root, text="Імпортувати Excel-файли:").pack()

    def import_data():
        file_paths = filedialog.askopenfilenames(filetypes=[("Excel files", "*.xlsx")])
        if not file_paths:
            return
        load_excel_data(file_paths)
        messagebox.showinfo("Успіх", "Дані імпортовано")

    def generate():
        result = generate_waybill()
        if result:
            save_to_database(result)
            messagebox.showinfo("Готово", "Шляховий лист сформовано та збережено")

    tk.Button(root, text="Імпортувати Excel", command=import_data).pack(pady=5)
    tk.Button(root, text="Згенерувати шляховий лист", command=generate).pack(pady=5)

    root.mainloop()
