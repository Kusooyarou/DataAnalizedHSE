# -*- coding: utf-8 -*-
"""
Created on Sun May 15 20:04:57 2024

@author: Бабенко А.
"""
import tkinter as tk
from tkinter import messagebox, ttk
import os
import pandas as pd
from Scripts import library  # Модуль для загрузки, сохранения и открытия файлов
import graph_reports  # Модуль для отображения графиков
import filter  # Модуль для фильтрации данных
import sheet_report  # Модуль для создания текстовых отчетов


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


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.entries = None
        self.entry_club_position = None
        self.entry_manager_name = None
        self.entry_club_name = None
        self.entry_club_id = None
        self.entry_club_formation = None
        self.open_reports_button = None
        self.generate_reports_button = None
        self.view_excel_button = None
        self.view_graphs_button = None
        self.view_clubs_button = None
        self.add_club_button = None
        self.title("Data Analyze")
        self.geometry("800x600")
        self.configure(bg="white")

        # Определение путей к файлам данных и отчетов относительно расположения скрипта
        base_dir = os.path.abspath(os.path.dirname(__file__))
        self.data_file_path = os.path.join(base_dir, "..", "data", "new_normalized_data.xlsx")
        self.report_file_path = os.path.join(base_dir, "..", "reports.xlsx")

        # Загрузка данных
        try:
            self.clubs_df = library.load_data(self.data_file_path, "clubs_normalized")
            self.matches_df = library.load_data(self.data_file_path, "matches_normalized")
            self.managers_df = library.load_data(self.data_file_path, "club_managers")
        except FileNotFoundError:
            messagebox.showerror("Ошибка", "Файл данных не найден.")
            self.destroy()
            return

        self.button_width = 20
        self.create_widgets()

    def create_widgets(self):
        # Конфигурация кнопок
        button_config = {
            'bg': "#9400D3",
            'fg': "white",
            'padx': 10,  # Corrected from 'pads' to 'padx'
            'pady': 5,  # Corrected from 'pads' to 'pady'
            'font': ("Times New Roman", 14),
            'width': self.button_width
        }

        # Создание кнопок
        self.add_club_button = tk.Button(self, text="Добавить клуб", command=self.add_club, **button_config)
        self.add_club_button.pack(pady=10)

        self.view_clubs_button = tk.Button(self, text="Просмотреть клубы", command=self.view_clubs, **button_config)
        self.view_clubs_button.pack(pady=10)

        self.view_graphs_button = tk.Button(self, text="Посмотреть графики", command=self.open_view_graphs_window,
                                            **button_config)
        self.view_graphs_button.pack(pady=20)

        self.view_excel_button = tk.Button(self, text="Просмотреть таблицу Excel", command=self.view_excel_table,
                                           **button_config)
        self.view_excel_button.pack(pady=10)

        self.generate_reports_button = tk.Button(self, text="Создать отчеты", command=generate_reports,
                                                 **button_config)
        self.generate_reports_button.pack(pady=10)

        self.open_reports_button = tk.Button(self, text="Открыть отчеты", command=open_reports, **button_config)
        self.open_reports_button.pack(pady=10)

    def view_excel_table(self):
        excel_window = tk.Toplevel(self)
        excel_window.title("Просмотр таблицы Excel")

        tree = ttk.Treeview(excel_window, columns=tuple(self.clubs_df.columns), show='headings')

        for col in self.clubs_df.columns:
            tree.heading(col, text=col)

        for _, row in self.clubs_df.iterrows():
            tree.insert("", tk.END, values=tuple(row))

        scrollbar = ttk.Scrollbar(excel_window, orient="vertical", command=tree.yview)
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
                                  command=lambda: filter.apply_filter(tree, entry_filter.get(), self.clubs_df))
        filter_button.grid(row=0, column=2)

    def open_view_graphs_window(self):
        graphs_window = tk.Toplevel(self)
        graphs_window.title("Просмотр графиков")
        graphs_window.geometry("500x500")

        button_color = "#9400D3"

        graphs = [
            ("График 1", graph_reports.view_graph_1),
            ("График 2", graph_reports.view_graph_2),
            ("График 3", graph_reports.view_graph_3),
            ("График 4", graph_reports.view_graph_4),
            ("График 5", graph_reports.view_graph_5),
            ("График 6", graph_reports.view_graph_6),
            ("График 7", graph_reports.view_graph_7),
        ]

        for text, command in graphs:
            button = tk.Button(graphs_window, text=text, command=command, bg=button_color, fg="white", padx=10, pady=5,
                               font=("Times New Roman", 14), width=self.button_width)
            button.pack(pady=10)

    def add_club(self):
        form_window = tk.Toplevel(self)
        form_window.title("Добавить клуб")

        fields = [
            ("ID клуба", self.entry_club_id),
            ("Название клуба", self.entry_club_name),
            ("Позиция клуба", self.entry_club_position),
            ("Имя менеджера", self.entry_manager_name),
            ("Стратегия клуба", self.entry_club_formation)
        ]

        self.entries = {}

        for label_text, entry_var in fields:
            label = tk.Label(form_window, text=label_text)
            label.pack(pady=5)
            entry_var = tk.Entry(form_window)
            entry_var.pack(pady=5)
            self.entries[label_text] = entry_var

        submit_button = tk.Button(form_window, text="Добавить клуб", command=self.success_added_club, bg="#909090",
                                  fg="white",
                                  padx=10, pady=5, font=("Times New Roman", 14))
        submit_button.pack(pady=10)

    def success_added_club(self):
        new_row = pd.DataFrame([[
            self.entries["Club ID"].get(),
            self.entries["Club Name"].get(),
            self.entries["Club Position"].get(),
            self.entries["Manager Name"].get(),
            self.entries["Club Formation"].get()
        ]], columns=self.clubs_df.columns)

        self.clubs_df = self.clubs_df.append(new_row, ignore_index=True)

        library.save_data(self.data_file_path, clubs_normalized=self.clubs_df, matches_normalized=self.matches_df,
                          club_managers=self.managers_df)

        messagebox.showinfo("Добавить клуб", "Клуб успешно добавлен.")

    def view_clubs(self):
        clubs_window = tk.Toplevel(self)
        clubs_window.title("Club List")

        tree = ttk.Treeview(clubs_window, columns=tuple(self.clubs_df.columns), show='headings')

        for col in self.clubs_df.columns:
            tree.heading(col, text=col)

        for _, row in self.clubs_df.iterrows():
            tree.insert("", tk.END, values=tuple(row))

        scrollbar = ttk.Scrollbar(clubs_window, orient="vertical", command=tree.yview)
        scrollbar.pack(side="right", fill="y")
        tree.configure(yscrollcommand=scrollbar.set)
        tree.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
