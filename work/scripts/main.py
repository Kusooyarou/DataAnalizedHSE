import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import graph_reports  # Модуль для отображения графиков
import filter  # Модуль для фильтрации данных
import sheet_report  # Модуль для создания текстовых отчетов
import os

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.view_graph_7_button = None
        self.view_graph_6_button = None
        self.view_graph_5_button = None
        self.view_graph_4_button = None
        self.view_graph_3_button = None
        self.view_graph_2_button = None
        self.view_graph_1_button = None
        self.title("Анализ футбола")
        self.geometry("800x600")
        self.configure(bg="white")

        # Загружаем данные из Excel-файла в DataFrame
        self.clubs_df = pd.read_excel("C:/Users/Andrey/Desktop/work2/DataAnalized/data/new_normalized_data.xlsx",
                                      sheet_name="clubs_normalized")
        self.matches_df = pd.read_excel("C:/Users/Andrey/Desktop/work2/DataAnalized/data/new_normalized_data.xlsx",
                                        sheet_name="matches_normalized")
        self.managers_df = pd.read_excel("C:/Users/Andrey/Desktop/work2/DataAnalized/data/new_normalized_data.xlsx",
                                         sheet_name="club_managers")

        self.button_width = 20

        # Кнопка для добавления нового клуба
        self.add_club_button = tk.Button(self, text="Добавить клуб", command=self.add_club, bg="#9400D3", fg="white",
                                         padx=10, pady=5, font=("Times new roman", 14), width=self.button_width)
        self.add_club_button.pack(pady=10)

        # Кнопка для просмотра списка клубов
        self.view_clubs_button = tk.Button(self, text="Просмотреть клубы", command=self.view_clubs, bg="#9400D3",
                                           fg="white", padx=10, pady=5, font=("Times new roman", 14),
                                           width=self.button_width)
        self.view_clubs_button.pack(pady=10)

        # Кнопка для просмотра графиков
        self.view_graphs_button = tk.Button(self, text="Посмотреть графики", command=self.open_view_graphs_window,
                                            bg="#9400D3", fg="white", padx=10, pady=5, font=("Times new roman", 14),
                                            width=self.button_width)
        self.view_graphs_button.pack(pady=20)

        # Кнопка для просмотра таблицы Excel
        self.view_excel_button = tk.Button(self, text="Просмотреть таблицу Excel", command=self.view_excel_table,
                                           bg="#9400D3", fg="white", padx=10, pady=5, font=("Times new roman", 14),
                                           width=self.button_width)
        self.view_excel_button.pack(pady=10)

        # Кнопка для создания отчетов
        self.generate_reports_button = tk.Button(self, text="Создать отчеты", command=self.generate_reports,
                                                 bg="#9400D3", fg="white", padx=10, pady=5,
                                                 font=("Times new roman", 14), width=self.button_width)
        self.generate_reports_button.pack(pady=10)

        # Кнопка для открытия отчетов
        self.open_reports_button = tk.Button(self, text="Открыть отчеты", command=self.open_reports,
                                             bg="#9400D3", fg="white", padx=10, pady=5,
                                             font=("Times new roman", 14), width=self.button_width)
        self.open_reports_button.pack(pady=10)

    # Функция для открытия созданных отчетов
    def open_reports(self):
        try:
            os.startfile("reports.xlsx")
        except FileNotFoundError:
            messagebox.showerror("Ошибка", "Файл отчетов не найден.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка при открытии файла отчетов: {e}")

    # Функция для создания отчетов
    def generate_reports(self):
        # Вызываем функцию создания отчетов из модуля sheet_report
        sheet_report.main()
        messagebox.showinfo("Создать отчеты", "Отчеты успешно созданы.")

    # Функция для просмотра таблицы Excel
    def view_excel_table(self):
        excel_window = tk.Toplevel(self)
        excel_window.title("Просмотр таблицы Excel")

        # Создаем виджет Treeview для отображения данных
        tree = ttk.Treeview(excel_window)

        # Определяем заголовки столбцов
        tree["columns"] = tuple(self.clubs_df.columns)
        for col in tree["columns"]:
            tree.heading(col, text=col)

        # Вставляем все данные из DataFrame в Treeview
        for index, row in self.clubs_df.iterrows():
            tree.insert("", tk.END, values=tuple(row))

        # Создаем полосу прокрутки для Treeview
        scrollbar = ttk.Scrollbar(excel_window, orient="vertical", command=tree.yview)
        scrollbar.pack(side="right", fill="y")
        tree.configure(yscrollcommand=scrollbar.set)

        # Размещаем виджет Treeview на окне
        tree.pack(fill="both", expand=True)

        # Добавляем текстовое поле и кнопку для фильтрации по club_id
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
        clubs_window = tk.Toplevel(self)
        clubs_window.title("View Graphs")
        clubs_window.geometry("500x500")

        # Фиолетовый цвет кнопок для графиков
        button_color = "#9400D3"

        self.view_graph_1_button = tk.Button(clubs_window, text="График 1", command=graph_reports.view_graph_1,
                                             bg=button_color, fg="white", padx=10, pady=5, font=("Times new roman", 14),
                                             width=self.button_width)
        self.view_graph_1_button.pack(pady=10)

        self.view_graph_2_button = tk.Button(clubs_window, text="График 2", command=graph_reports.view_graph_2,
                                             bg=button_color, fg="white", padx=10, pady=5, font=("Times new roman", 14),
                                             width=self.button_width)
        self.view_graph_2_button.pack(pady=10)

        self.view_graph_3_button = tk.Button(clubs_window, text="График 3", command=graph_reports.view_graph_3,
                                             bg=button_color, fg="white", padx=10, pady=5, font=("Times new roman", 14),
                                             width=self.button_width)
        self.view_graph_3_button.pack(pady=10)

        self.view_graph_4_button = tk.Button(clubs_window, text="График 4", command=graph_reports.view_graph_4,
                                             bg=button_color, fg="white", padx=10, pady=5, font=("Times new roman", 14),
                                             width=self.button_width)
        self.view_graph_4_button.pack(pady=10)

        self.view_graph_5_button = tk.Button(clubs_window, text="График 5", command=graph_reports.view_graph_5,
                                             bg=button_color, fg="white", padx=10, pady=5, font=("Times new roman", 14),
                                             width=self.button_width)
        self.view_graph_5_button.pack(pady=10)

        self.view_graph_6_button = tk.Button(clubs_window, text="График 6", command=graph_reports.view_graph_6,
                                             bg=button_color, fg="white", padx=10, pady=5, font=("Times new roman", 14),
                                             width=self.button_width)
        self.view_graph_6_button.pack(pady=10)

        self.view_graph_7_button = tk.Button(clubs_window, text="График 7", command=graph_reports.view_graph_7,
                                             bg=button_color, fg="white", padx=10, pady=5, font=("Times new roman", 14),
                                             width=self.button_width)
        self.view_graph_7_button.pack(pady=10)

    def add_club(self):
        # Добавление клуба в таблицу
        form_window = tk.Toplevel(self)
        form_window.title("Добавить клуб")

        label_club_id = tk.Label(form_window, text="ID клуба")
        label_club_id.pack(pady=10)

        self.entry_club_id = tk.Entry(form_window)
        self.entry_club_id.pack(pady=10)

        label_club_name = tk.Label(form_window, text="Название клуба")
        label_club_name.pack(pady=10)

        self.entry_club_name = tk.Entry(form_window)
        self.entry_club_name.pack(pady=10)

        label_club_position = tk.Label(form_window, text="Позиция клуба")
        label_club_position.pack(pady=10)

        self.entry_club_position = tk.Entry(form_window)
        self.entry_club_position.pack(pady=10)

        label_manager_name = tk.Label(form_window, text="Имя менеджера")
        label_manager_name.pack(pady=10)

        self.entry_manager_name = tk.Entry(form_window)
        self.entry_manager_name.pack(pady=10)

        label_club_formation = tk.Label(form_window, text="Стратегия клуба")
        label_club_formation.pack(pady=10)

        self.entry_club_formation = tk.Entry(form_window)
        self.entry_club_formation.pack(pady=10)

        self.view_graphs_button = tk.Button(form_window, text="Добавить клуб", command=self.success_added_club,
                                            bg="#909090",
                                            fg="white", padx=10, pady=5, font=("Times new roman", 14))
        self.view_graphs_button.pack(pady=10)

    def success_added_club(self):
        # Загружаем данные из файла
        clubs_normalized = pd.read_excel('C:/Users/Andrey/Desktop/work2/DataAnalized/data/new_normalized_data.xlsx',
                                         sheet_name='clubs_normalized')
        matches_normalized = pd.read_excel('C:/Users/Andrey/Desktop/work2/DataAnalized/data/new_normalized_data.xlsx',
                                           sheet_name='matches_normalized')
        club_managers = pd.read_excel('C:/Users/Andrey/Desktop/work2/DataAnalized/data/new_normalized_data.xlsx',
                                      sheet_name='club_managers')

        # Получаем данные из полей ввода
        club_id = self.entry_club_id.get()
        club_name = self.entry_club_name.get()
        club_position = self.entry_club_position.get()
        manager_name = self.entry_manager_name.get()
        club_formation = self.entry_club_formation.get()

        # Добавляем новую запись в DataFrame для clubs_normalized
        new_row_clubs = pd.DataFrame([[club_id, club_name, club_position, manager_name, club_formation]],
                                     columns=clubs_normalized.columns)
        clubs_normalized = clubs_normalized._append(new_row_clubs, ignore_index=True)

        # Сохраняем обновленные данные в файл
        with pd.ExcelWriter('C:/Users/Andrey/Desktop/work2/DataAnalized/data/new_normalized_data.xlsx',
                            engine='openpyxl') as writer:
            clubs_normalized.to_excel(writer, sheet_name='clubs_normalized', index=False)
            matches_normalized.to_excel(writer, sheet_name='matches_normalized', index=False)
            club_managers.to_excel(writer, sheet_name='club_managers', index=False)

        messagebox.showinfo("Добавить клуб", "Клуб успешно добавлен")

    def view_clubs(self):
        # Создание окна для просмотра таблицы клубов
        clubs_window = tk.Toplevel(self)
        clubs_window.title("Список клубов")

        # Создаем виджет Treeview
        tree = ttk.Treeview(clubs_window)

        # Определяем заголовки столбцов
        tree["columns"] = tuple(self.clubs_df.columns)
        for col in tree["columns"]:
            tree.heading(col, text=col)

        # Вставляем все данные из DataFrame при загрузке
        for index, row in self.clubs_df.iterrows():
            tree.insert("", tk.END, values=tuple(row))

        # Создаем полосу прокрутки
        scrollbar = ttk.Scrollbar(clubs_window, orient="vertical", command=tree.yview)
        scrollbar.pack(side="right", fill="y")
        tree.configure(yscrollcommand=scrollbar.set)

        # Размещаем виджет Treeview
        tree.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = Application()
    app.mainloop()