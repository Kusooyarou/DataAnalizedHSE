# -*- coding: utf-8 -*-
"""
Created on Sun May 15 20:04:57 2024

@author: Сорокин Г.
"""

import os
import sys
from tkinter import messagebox
import subprocess
import sheet_report


def open_reports():
    """Открыть файл отчетов.

    Пытается открыть файл "reports.xlsx" при помощи приложения по умолчанию в системе.
    Если файл не найден, выводит сообщение об ошибке.

    Raises:
        FileNotFoundError: Если файл отчетов не найден.
        Exception: Если произошла ошибка при открытии файла отчетов.
    """
    try:
        base_dir = os.path.abspath(os.path.dirname(__file__))
        output_dir = os.path.join(base_dir, "..", "outputs", "reports.xlsx")

        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, output_dir])
    except FileNotFoundError:
        messagebox.showerror("Ошибка", "Файл отчетов не найден.")
    except Exception as e:
        messagebox.showerror(
            "Ошибка", f"Произошла ошибка при открытии файла отчетов: {e}")


def generate_reports():
    """Создать отчеты.

    Запускает процесс создания отчетов при помощи функции main из модуля sheet_report.
    Выводит сообщение об успешном создании отчетов.
    """
    sheet_report.main()
    messagebox.showinfo("Создать отчеты", "Отчеты успешно созданы.")
