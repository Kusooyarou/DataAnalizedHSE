import tkinter as tk
import graph_reports


def open_view_graphs_window():
    clubs_window = tk.Toplevel()
    clubs_window.title("View Graphs")
    clubs_window.geometry("500x500")

    button_color = "#9400D3"

    view_graph_1_button = tk.Button(clubs_window, text="График 1", command=graph_reports.view_graph_1,
                                    bg=button_color, fg="white", padx=10, pady=5, font=("Times new roman", 14))
    view_graph_1_button.pack(pady=10)

    view_graph_2_button = tk.Button(clubs_window, text="График 2", command=graph_reports.view_graph_2,
                                    bg=button_color, fg="white", padx=10, pady=5, font=("Times new roman", 14))
    view_graph_2_button.pack(pady=10)

    view_graph_3_button = tk.Button(clubs_window, text="График 3", command=graph_reports.view_graph_3,
                                    bg=button_color, fg="white", padx=10, pady=5, font=("Times new roman", 14))
    view_graph_3_button.pack(pady=10)

    view_graph_4_button = tk.Button(clubs_window, text="График 4", command=graph_reports.view_graph_4,
                                    bg=button_color, fg="white", padx=10, pady=5, font=("Times new roman", 14))
    view_graph_4_button.pack(pady=10)

    view_graph_5_button = tk.Button(clubs_window, text="График 5", command=graph_reports.view_graph_5,
                                    bg=button_color, fg="white", padx=10, pady=5, font=("Times new roman", 14))
    view_graph_5_button.pack(pady=10)

    view_graph_6_button = tk.Button(clubs_window, text="График 6", command=graph_reports.view_graph_6,
                                    bg=button_color, fg="white", padx=10, pady=5, font=("Times new roman", 14))
    view_graph_6_button.pack(pady=10)

    view_graph_7_button = tk.Button(clubs_window, text="График 7", command=graph_reports.view_graph_7,
                                    bg=button_color, fg="white", padx=10, pady=5, font=("Times new roman", 14))
    view_graph_7_button.pack(pady=10)
