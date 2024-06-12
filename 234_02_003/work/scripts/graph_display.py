# -*- coding: utf-8 -*-
"""
Created on May 10 15:04:57 2024

@author: Бабенко А. Осинцев К.
"""
import os
import sys
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
import graph_reports

sys.path.append("../../work")

base_dir = os.path.abspath(os.path.dirname(__file__))
output_dir = os.path.join(base_dir, "..", "outputs")

def show_graph(display_frame, graph_function):
    """
    Отображает график, сгенерированный указанной функцией, в указанном фрейме отображения.

    Аргументы:
        display_frame (tk.Frame): Фрейм для отображения графика.
        graph_function (function): Функция, которая генерирует отображаемый график.
    """
    # Удаление всех виджетов из фрейма отображения
    for widget in display_frame.winfo_children():
        widget.destroy()

    graphs_frame = tk.Frame(display_frame, bg="white")
    graphs_frame.pack(fill="both", expand=True)

    # Генерация графика с помощью переданной функции
    fig = graph_function()

    canvas = tk.Canvas(graphs_frame, bg="white", height=600, width=800)
    canvas.pack(fill="both", expand=True)

    try:
        global img
        img = Image.open(os.path.join(output_dir, fig))
        img = img.resize((800, 600))
        img = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor='nw', image=img)
    except Exception as e:
        messagebox.showerror(
            "Ошибка", f"Не удалось загрузить изображение: {e}")


def open_view_graphs(display_frame):
    """
    Открывает фрейм для выбора и отображения различных графиков.

    Аргументы:
        display_frame (tk.Frame): Фрейм для отображения графиков.
    """
    # Удаление всех виджетов из фрейма отображения
    for widget in display_frame.winfo_children():
        widget.destroy()

    # Создание фрейма для отображения графиков
    graphs_frame = tk.Frame(display_frame, bg="white")
    graphs_frame.pack(fill="both", expand=True)

    button_color = "#9400D3"

    # Список графиков с соответствующими функциями
    graphs = [
        ("График 1", graph_reports.view_graph_1),
        ("График 2", graph_reports.view_graph_2),
        ("График 3", graph_reports.view_graph_3),
        ("График 4", graph_reports.view_graph_4),
        ("График 5", graph_reports.view_graph_5),
        ("График 6", graph_reports.view_graph_6),
        ("График 7", graph_reports.view_graph_7),
    ]

    # Создание кнопок для выбора графиков
    for text, command in graphs:
        button = tk.Button(graphs_frame, text=text, command=lambda cmd=command: show_graph(display_frame, cmd),
                           bg=button_color, fg="white", padx=10, pady=5,
                           font=("Times New Roman", 14), width=20)
        button.pack(pady=10)
