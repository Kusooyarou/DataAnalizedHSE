import tkinter as tk
import graph_reports


def open_view_graphs_window():
    """
    Открывает новое окно с кнопками для просмотра различных графиков.

    Кнопки:
        - График 1: Отображает график 1.
        - График 2: Отображает график 2.
        - График 3: Отображает график 3.
        - График 4: Отображает график 4.
        - График 5: Отображает график 5.
        - График 6: Отображает график 6.
        - График 7: Отображает график 7.

    Каждая кнопка вызывает соответствующую функцию из модуля graph_reports для отображения графика.
    """
    clubs_window = tk.Toplevel()
    clubs_window.title("View Graphs")
    clubs_window.geometry("500x500")

    button_color = "#9400D3"
    button_config = {
        "bg": button_color,
        "fg": "white",
        "padx": 10,
        "pady": 5,
        "font": ("Times new roman", 14)
    }

    buttons = [
        ("График 1", graph_reports.view_graph_1),
        ("График 2", graph_reports.view_graph_2),
        ("График 3", graph_reports.view_graph_3),
        ("График 4", graph_reports.view_graph_4),
        ("График 5", graph_reports.view_graph_5),
        ("График 6", graph_reports.view_graph_6),
        ("График 7", graph_reports.view_graph_7)
    ]

    for text, command in buttons:
        tk.Button(clubs_window, text=text, command=command, **button_config).pack(pady=10)
