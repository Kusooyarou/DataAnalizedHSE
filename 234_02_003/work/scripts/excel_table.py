# -*- coding: utf-8 -*-
"""
Created on Sun May 15 20:04:57 2024

@author: Бабенко А. Свистунов А.
"""
import tkinter as tk
from tkinter import ttk
import filter


def view_excel_table(clubs_df):
    """
    Отображает окно для просмотра таблицы Excel с данными о клубах.

    Аргументы:
        clubs_df (pandas.DataFrame): DataFrame, содержащий данные о клубах.

    Действия:
        Создает новое окно с Treeview для отображения данных о клубах.
        Добавляет возможность фильтрации данных по club_id.
    """
    excel_window = tk.Toplevel()
    excel_window.title("Просмотр таблицы Excel")

    tree = ttk.Treeview(excel_window)

    tree["columns"] = tuple(clubs_df.columns)
    for col in tree["columns"]:
        tree.heading(col, text=col)

    for index, row in clubs_df.iterrows():
        tree.insert("", tk.END, values=tuple(row))

    scrollbar = ttk.Scrollbar(
        excel_window, orient="vertical", command=tree.yview)
    scrollbar.pack(side="right", fill="y")
    tree.configure(yscrollcommand=scrollbar.set)

    tree.pack(fill="both", expand=True)

    filter_frame = tk.Frame(excel_window)
    filter_frame.pack(pady=10)

    label_filter = tk.Label(filter_frame, text="Введите club_id:")
    label_filter.grid(row=0, column=0)

    entry_filter = tk.Entry(filter_frame)
    entry_filter.grid(row=0, column=1)

    filter_button = tk.Button(filter_frame, text="Применить фильтр",
                              command=lambda: filter.apply_filter(tree, entry_filter.get(), clubs_df))
    filter_button.grid(row=0, column=2)
