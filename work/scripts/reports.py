import os
from tkinter import messagebox
import sheet_report

def open_reports():
    try:
        os.startfile("reports.xlsx")
    except FileNotFoundError:
        messagebox.showerror("Ошибка", "Файл отчетов не найден.")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка при открытии файла отчетов: {e}")

def generate_reports():
    sheet_report.main()
    messagebox.showinfo("Создать отчеты", "Отчеты успешно созданы.")
