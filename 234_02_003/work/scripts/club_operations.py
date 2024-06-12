# -*- coding: utf-8 -*-
"""
Created on Sun May 15 20:04:57 2024

@author: Осинцев К.
"""
import tkinter as tk
from tkinter import messagebox
import pandas as pd
from library import save_data


def add_club(app, button_color=None):
    """
    Отображает форму для добавления нового клуба.

    Аргументы:
        app (Application): Экземпляр главного приложения.
        button_color (str): Цвет кнопки для добавления клуба.

    Действия:
        Очищает текущий фрейм отображения и создает новую форму для ввода данных клуба.
        При нажатии кнопки "Добавить клуб" вызывается функция success_added_club.
    """
    for widget in app.display_frame.winfo_children():
        widget.destroy()

    form_frame = tk.Frame(app.display_frame, bg="grey")
    form_frame.pack(fill="both", expand=True)

    fields = [
        ("ID клуба", app.entry_club_id),
        ("Название клуба", app.entry_club_name),
        ("Позиция клуба", app.entry_club_position),
        ("Имя менеджера", app.entry_manager_name),
        ("Стратегия клуба", app.entry_club_formation)
    ]

    app.entries = {}

    for label_text, entry_var in fields:
        label = tk.Label(form_frame, text=label_text, bg="white")
        label.pack(pady=5)
        entry_var = tk.Entry(form_frame)
        entry_var.pack(pady=5)
        app.entries[label_text] = entry_var

    submit_button = tk.Button(form_frame, text="Добавить клуб", command=lambda: success_added_club(app), bg=button_color,
                              fg="#9400D3", padx=10, pady=5, font=("Times New Roman", 14))
    submit_button.pack(pady=10)


def success_added_club(app):
    """
    Добавляет новый клуб в DataFrame и сохраняет обновленные данные.

    Аргументы:
        app (Application): Экземпляр главного приложения.

    Действия:
        Получает данные из полей ввода, добавляет новую строку в DataFrame клубов,
        сохраняет обновленный DataFrame в файл и отображает сообщение о успешном добавлении клуба.
    """
    new_row = pd.DataFrame([[
        app.entries["ID клуба"].get(),
        app.entries["Название клуба"].get(),
        app.entries["Позиция клуба"].get(),
        app.entries["Имя менеджера"].get(),
        app.entries["Стратегия клуба"].get()
    ]], columns=app.clubs_df.columns)

    app.clubs_df = pd.concat([app.clubs_df, new_row], ignore_index=True)

    save_data(app.data_file_path, clubs_normalized=app.clubs_df, matches_normalized=app.matches_df,
              club_managers=app.managers_df)

    messagebox.showinfo("Добавить клуб", "Клуб успешно добавлен.")


def view_clubs(app):
    """
    Отображает таблицу с данными о клубах.

    Аргументы:
        app (Application): Экземпляр главного приложения.

    Действия:
        Вызывает метод view_excel_table главного приложения для отображения данных о клубах.
    """
    app.view_excel_table()
