# -*- coding: utf-8 -*-
"""
Created on Wed May 15 20:04:57 2024

@author: Бабенко А, Осинцев К
"""
import tkinter as tk
from tkinter import messagebox, ttk
import os
import sys
import pandas as pd
from PIL import Image, ImageTk
from library import load_data, save_data  # Модуль для загрузки, сохранения и открытия файлов
import graph_reports  # Модуль для отображения графиков
import filter  # Модуль для фильтрации данных
import sheet_report  # Модуль для создания текстовых отчетов
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import club_operations  # Импорт нового модуля


sys.path.append("../../work")


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
        self.img = None
        self.display_frame = None
        self.canvas = None
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
        self.geometry("1200x650")
        self.configure(bg="white")

        # Определение путей к файлам данных и отчетов относительно расположения скрипта
        base_dir = os.path.abspath(os.path.dirname(__file__))
        self.data_file_path = os.path.join(base_dir, "..", "data", "new_normalized_data.xlsx")
        self.report_file_path = os.path.join(base_dir, "..", "reports.xlsx")
        self.picture1_file_path = os.path.join(base_dir, "..", "data", "picture1.png")

        # Загрузка данных
        try:
            self.clubs_df = load_data(self.data_file_path, "clubs_normalized")
            self.matches_df = load_data(self.data_file_path, "matches_normalized")
            self.managers_df = load_data(self.data_file_path, "club_managers")
        except FileNotFoundError:
            messagebox.showerror("Ошибка", "Файл данных не найден.")
            self.destroy()
            return

        self.button_width = 20
        self.button_height = 2
        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(text='Добро пожаловать', font=('Open Sans Light', 22),
                          justify='center', foreground='black', background='white')

        label.grid(row=0, column=0, padx=10, pady=10)
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=2)

        # Конфигурация кнопок
        button_config = {
            'bg': "#9400D3",
            'fg': "white",
            'padx': 25,
            'pady': 20,
            'font': ("Times New Roman", 14),
            'width': self.button_width
        }

        button_add_clubs = tk.Button(text='Добавить клуб', command=lambda: club_operations.add_club(self), **button_config)
        button_show_clubs = tk.Button(text='Просмотреть клубы', command=lambda: club_operations.view_clubs(self), **button_config)
        button_show_graphs = tk.Button(text='Посмотреть графики', command=self.open_view_graphs, **button_config)
        button_show_excel = tk.Button(text='Открыть таблицу Excel', command=self.view_excel_table, **button_config)
        button_generate_reports = tk.Button(text='Создать отчеты', command=generate_reports, **button_config)
        button_open_reports = tk.Button(text='Открыть отчеты', command=open_reports, **button_config)

        button_add_clubs.grid(row=1, column=0, pady=5)
        button_show_clubs.grid(row=2, column=0, pady=5)
        button_show_graphs.grid(row=3, column=0, pady=5)
        button_show_excel.grid(row=4, column=0, pady=5)
        button_generate_reports.grid(row=5, column=0, pady=5)
        button_open_reports.grid(row=6, column=0, pady=5)

        self.display_frame = tk.Frame(self, bg="white")
        self.display_frame.grid(row=0, column=1, rowspan=7, padx=10, pady=25, sticky="nsew")

        self.canvas = tk.Canvas(self.display_frame, bg="white", height=600, width=800)
        self.canvas.pack(fill="both", expand=True)

        try:
            self.img = Image.open(self.picture1_file_path)
            self.img = self.img.resize((800, 600))
            self.img = ImageTk.PhotoImage(self.img)
            self.canvas.create_image(0, 0, anchor='nw', image=self.img)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить изображение: {e}")

    def view_excel_table(self):
        def reset_filter():
            for item in tree.get_children():
                tree.delete(item)
            for _, row in self.clubs_df.iterrows():
                tree.insert("", tk.END, values=tuple(row))

        for widget in self.display_frame.winfo_children():
            widget.destroy()

        tree = ttk.Treeview(self.display_frame, columns=tuple(self.clubs_df.columns), show='headings')
        for col in self.clubs_df.columns:
            tree.heading(col, text=col)

        for _, row in self.clubs_df.iterrows():
            tree.insert("", tk.END, values=tuple(row))

        scrollbar = ttk.Scrollbar(self.display_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree.pack(fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        filter_frame = tk.Frame(self.display_frame, bg="white")
        filter_frame.pack(pady=10)

        label_filter = tk.Label(filter_frame, text="Введите club_id:", bg="white")
        label_filter.grid(row=0, column=0)

        entry_filter = tk.Entry(filter_frame)
        entry_filter.grid(row=0, column=1)

        filter_button = tk.Button(filter_frame, text="Применить фильтр",
                                  command=lambda: filter.apply_filter(tree, entry_filter.get(), self.clubs_df))
        filter_button.grid(row=0, column=2)

        reset_button = tk.Button(filter_frame, text="Сбросить фильтр", command=reset_filter)
        reset_button.grid(row=0, column=3)

    def show_graph(self, graph_function):
        for widget in self.display_frame.winfo_children():
            widget.destroy()

        fig = graph_function()
        canvas = FigureCanvasTkAgg(fig, master=self.display_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def open_view_graphs(self):
        for widget in self.display_frame.winfo_children():
            widget.destroy()

        graphs_frame = tk.Frame(self.display_frame, bg="white")
        graphs_frame.pack(fill="both", expand=True)

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
            button = tk.Button(graphs_frame, text=text, command=lambda cmd=command: self.show_graph(cmd), bg=button_color, fg="white", padx=10, pady=5,
                               font=("Times New Roman", 14), width=self.button_width)
            button.pack(pady=10)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
