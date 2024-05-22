import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # ????????????????????


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Управление клубами и матчами")

        self.clubs_df = pd.read_excel('../../data/new_normalized_data.xlsx',
                                      sheet_name="clubs_normalized")
        self.matches_df = pd.read_excel('../../data/new_normalized_data.xlsx',
                                        sheet_name="matches_normalized")
        self.managers_df = pd.read_excel('../../data/new_normalized_data.xlsx',
                                         sheet_name="club_managers")

        # Кнопки для управления данными
        self.add_club_button = tk.Button(self, text="Добавить клуб", command=self.add_club, bg="#909090", fg="white",
                                         padx=10, pady=5, font=("Times new roman", 14))
        self.add_club_button.pack(pady=10)

        self.view_clubs_button = tk.Button(self, text="Просмотреть клубы", command=self.view_clubs, bg="#909090",
                                           fg="white", padx=10, pady=5, font=("Times new roman", 14))
        self.view_clubs_button.pack(pady=10)

        self.view_graphs_button = tk.Button(self, text="Посмотреть графики", command=self.open_view_graphs_window, bg="#909090",
                                            fg="white", padx=10, pady=5, font=("Times new roman", 14))
        self.view_graphs_button.pack(pady=10)

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

        self.view_graphs_button = tk.Button(form_window, text="Добавить клуб", command=self.success_added_club, bg="#909090",
                                            fg="white", padx=10, pady=5, font=("Times new roman", 14))
        self.view_graphs_button.pack(pady=10)

    def success_added_club(self):
        clubs_normalized = pd.read_excel('../../data/new_normalized_data.xlsx', sheet_name='clubs_normalized')
        
        club_id = self.entry_club_id.get()
        club_name = self.entry_club_name.get()
        club_position = self.entry_club_position.get()
        manager_name = self.entry_manager_name.get()
        club_formation = self.entry_club_formation.get()

        new_row = [club_id, club_name, club_position, manager_name, club_formation]
        clubs_normalized.loc[len(clubs_normalized)] = new_row

        clubs_normalized.to_excel('../../data/new_normalized_data.xlsx', sheet_name='clubs_normalized', index=False)

        messagebox.showinfo("Добавить клуб", "Клуб успешно добавлен")

    def view_clubs(self):
        # Отображение списка клубов в новом окне
        clubs_window = tk.Toplevel(self)
        clubs_window.title("Список клубов")

        clubs_listbox = tk.Listbox(clubs_window)
        for index, row in self.clubs_df.iterrows():
            clubs_listbox.insert(tk.END, f"{row['club_id']}: {row['club_name']}, {row['club_manager_name']}")
        clubs_listbox.pack(fill="both", expand=True, padx=10, pady=10)

    def open_view_graphs_window(self):
        # Отображение списка клубов в новом окне
        clubs_window = tk.Toplevel(self)
        clubs_window.title("Список отчётов")

        self.view_graph_1_button = tk.Button(clubs_window, text="Отчёт 1", command=self.view_graph_1, bg="#909090", fg="white",
                                         padx=10, pady=5, font=("Times new roman", 14))
        self.view_graph_1_button.pack(pady=10)

        self.view_graph_2_button = tk.Button(clubs_window, text="Отчёт 2", command=self.view_graph_2, bg="#909090", fg="white",
                                         padx=10, pady=5, font=("Times new roman", 14))
        self.view_graph_2_button.pack(pady=10)

        self.view_graph_3_button = tk.Button(clubs_window, text="Отчёт 3", command=self.view_graph_3, bg="#909090", fg="white",
                                         padx=10, pady=5, font=("Times new roman", 14))
        self.view_graph_3_button.pack(pady=10)

        self.view_graph_4_button = tk.Button(clubs_window, text="Отчёт 4", command=self.view_graph_4, bg="#909090", fg="white",
                                         padx=10, pady=5, font=("Times new roman", 14))
        self.view_graph_4_button.pack(pady=10)

        self.view_graph_5_button = tk.Button(clubs_window, text="Отчёт 5", command=self.view_graph_5, bg="#909090", fg="white",
                                         padx=10, pady=5, font=("Times new roman", 14))
        self.view_graph_5_button.pack(pady=10)

        self.view_graph_6_button = tk.Button(clubs_window, text="Отчёт 6", command=self.view_graph_6, bg="#909090", fg="white",
                                         padx=10, pady=5, font=("Times new roman", 14))
        self.view_graph_6_button.pack(pady=10)

        self.view_graph_7_button = tk.Button(clubs_window, text="Отчёт 7", command=self.view_graph_7, bg="#909090", fg="white",
                                         padx=10, pady=5, font=("Times new roman", 14))
        self.view_graph_7_button.pack(pady=10)

    def view_graph_1(self):
        clubs_normalized = pd.read_excel('../../data/new_normalized_data.xlsx',
                                         sheet_name='clubs_normalized')
        matches_normalized = pd.read_excel('../../data/new_normalized_data.xlsx',
                                           sheet_name='matches_normalized')
        club_managers = pd.read_excel('../../data/new_normalized_data.xlsx',
                                      sheet_name='club_managers')

        matches_count = matches_normalized.groupby('home_club_id').size().reset_index(name='matches_count')
        matches_count = matches_count.merge(clubs_normalized[['club_id', 'club_name']], left_on='home_club_id',
                                            right_on='club_id')

        top_30_matches_count = matches_count.sort_values(by='matches_count', ascending=False).head(204)

        colors = sns.color_palette('Purples', n_colors=30)[::-1]  # Выбор 30 цветов из палитры Purples

        # столбчатая гистограмма
        plt.figure(figsize=(12, 8))
        sns.barplot(x='club_name', y='matches_count', data=top_30_matches_count, hue='club_name', palette=colors,
                    legend=False)
        plt.xlabel('Название клуба', fontsize=12)
        plt.ylabel('Количество матчей', fontsize=12)
        plt.title('Топ-30 команд по количеству матчей', fontsize=14)
        plt.xticks(rotation=90, fontsize=10)
        plt.yticks(range(0, top_30_matches_count['matches_count'].max() + 1, 5))
        plt.tight_layout()
        plt.savefig('top_30_matches_per_club_barplot.png')
        plt.show()

    def view_graph_2(self):
        clubs_normalized = pd.read_excel('../../data/new_normalized_data.xlsx',
                                         sheet_name='clubs_normalized')
        matches_normalized = pd.read_excel('../../data/new_normalized_data.xlsx',
                                           sheet_name='matches_normalized')
        club_managers = pd.read_excel('../../data/new_normalized_data.xlsx',
                                      sheet_name='club_managers')

        matches_count = matches_normalized.groupby('home_club_id').size().reset_index(name='matches_count')
        matches_count = matches_count.merge(clubs_normalized[['club_id', 'club_name']], left_on='home_club_id',
                                            right_on='club_id')

        # группировка данных по тренерам и подсчет количества побед для каждого
        coach_wins = matches_normalized.groupby('home_club_manager_name').size().reset_index(name='wins')

        # выбор топ 20 тренеров с наибольшим количеством побед
        top_20_coaches = coach_wins.sort_values(by='wins', ascending=False).head(20)

        colors = sns.color_palette('Purples', n_colors=20)[::-1]  # Выбор 25 цветов из палитры Purples

        # построение категоризированной гистограммы
        plt.figure(figsize=(12, 8))
        sns.barplot(x='home_club_manager_name', y='wins', data=top_20_coaches, hue='home_club_manager_name',
                    palette=colors, saturation=1.5, legend=False)
        plt.xlabel('Имя тренера', fontsize=12)
        plt.ylabel('Количество побед', fontsize=12)
        plt.title('Топ 20 тренеров с наибольшим количеством побед', fontsize=14)
        plt.xticks(rotation=90, fontsize=10)
        plt.yticks(fontsize=10)
        plt.yticks(range(0, top_20_coaches['wins'].max() + 1, 2))
        plt.tight_layout()
        plt.savefig('top_20_coaches_wins_histogram_purple_gradient.png')
        plt.show()

    def view_graph_3(self):
        clubs_normalized = pd.read_excel('../../data/new_normalized_data.xlsx',
                                         sheet_name='clubs_normalized')
        matches_normalized = pd.read_excel('../../data/new_normalized_data.xlsx',
                                           sheet_name='matches_normalized')
        club_managers = pd.read_excel('../../data/new_normalized_data.xlsx',
                                      sheet_name='club_managers')

        matches_count = matches_normalized.groupby('home_club_id').size().reset_index(name='matches_count')
        matches_count = matches_count.merge(clubs_normalized[['club_id', 'club_name']], left_on='home_club_id',
                                            right_on='club_id')

        # для категоризированной диаграммы "box-and-whiskers"
        quant_qual_data_box = matches_normalized[['home_club_goals', 'competition_id']]
        colors = sns.color_palette('Purples', n_colors=29)[::-1]  # Выбор 29 цветов из палитры Purples

        # категоризированная диаграмма "box-and-whiskers"
        plt.figure(figsize=(12, 8))
        sns.boxplot(data=quant_qual_data_box, x='competition_id', y='home_club_goals', hue='competition_id',
                    palette=colors, legend=False)
        plt.xlabel('ID соревнования', fontsize=13)
        plt.ylabel('Голы домашнего клуба', fontsize=13)
        plt.title('Категоризированная диаграмма “box-and-whiskers”', fontsize=15)
        plt.tight_layout()
        plt.savefig('categorized_boxplot.png')
        plt.show()

    def view_graph_4(self):
        clubs_normalized = pd.read_excel('../../data/new_normalized_data.xlsx',
                                         sheet_name='clubs_normalized')
        matches_normalized = pd.read_excel('../../data/new_normalized_data.xlsx',
                                           sheet_name='matches_normalized')
        club_managers = pd.read_excel('../../data/new_normalized_data.xlsx',
                                      sheet_name='club_managers')

        matches_count = matches_normalized.groupby('home_club_id').size().reset_index(name='matches_count')
        matches_count = matches_count.merge(clubs_normalized[['club_id', 'club_name']], left_on='home_club_id',
                                            right_on='club_id')

        quant_quant_qual_data = matches_normalized[['home_club_goals', 'away_club_goals', 'competition_id']]

        # категоризированная диаграмма рассеивания
        plt.figure(figsize=(12, 8))
        sns.scatterplot(data=quant_quant_qual_data, x='home_club_goals', y='away_club_goals', hue='competition_id',
                        palette='viridis', s=100)
        plt.xlabel('Голы домашнего клуба', fontsize=13)
        plt.ylabel('Голы гостевого клуба', fontsize=13)
        plt.title('Категоризированная диаграмма рассеивания', fontsize=15)
        plt.legend(title='ID соревнования', fontsize=10)
        plt.tight_layout()
        plt.savefig('categorized_scatterplot.png')
        plt.show()

    def view_graph_5(self):
        clubs_normalized = pd.read_excel('../../data/new_normalized_data.xlsx',
                                         sheet_name='clubs_normalized')
        matches_normalized = pd.read_excel('../../data/new_normalized_data.xlsx',
                                           sheet_name='matches_normalized')
        club_managers = pd.read_excel('../../data/new_normalized_data.xlsx',
                                      sheet_name='club_managers')

        matches_count = matches_normalized.groupby('home_club_id').size().reset_index(name='matches_count')
        matches_count = matches_count.merge(clubs_normalized[['club_id', 'club_name']], left_on='home_club_id',
                                            right_on='club_id')

        # дополнительно????

        # Категоризированная гистограмма: распределение количества матчей по сезонам
        plt.figure(figsize=(12, 8))
        sns.histplot(data=matches_normalized, x='season', bins=10, kde=True)
        plt.xlabel('Сезон', fontsize=12)
        plt.ylabel('Частота', fontsize=12)
        plt.title('Распределение количества матчей по сезонам', fontsize=14)
        plt.xticks(rotation=45, fontsize=10)
        plt.yticks(fontsize=10)
        plt.tight_layout()
        plt.savefig('matches_per_season_histogram.png')
        plt.show()

    def view_graph_6(self):
        clubs_normalized = pd.read_excel('../../data/new_normalized_data.xlsx',
                                         sheet_name='clubs_normalized')
        matches_normalized = pd.read_excel('../../data/new_normalized_data.xlsx',
                                           sheet_name='matches_normalized')
        club_managers = pd.read_excel('../../data/new_normalized_data.xlsx',
                                      sheet_name='club_managers')

        matches_count = matches_normalized.groupby('home_club_id').size().reset_index(name='matches_count')
        matches_count = matches_count.merge(clubs_normalized[['club_id', 'club_name']], left_on='home_club_id',
                                            right_on='club_id')


        # Рассчитаем позиции клубов на основе количества побед
        home_club_wins = matches_normalized.groupby('home_club_id')['home_club_goals'].count().reset_index(name='wins')
        home_club_wins['club_position'] = home_club_wins['wins'].rank(ascending=False, method='min')

        # Объединим информацию о позициях клубов с данными о матчах
        matches_with_positions = matches_normalized.merge(home_club_wins[['home_club_id', 'club_position']],
                                                          left_on='home_club_id', right_on='home_club_id')

        # Построим диаграмму рассеивания
        plt.figure(figsize=(12, 8))
        sns.scatterplot(data=matches_with_positions, x='club_position', y='home_club_goals', hue='season',
                        palette='viridis', s=100)
        plt.xlabel('Позиция клуба', fontsize=13)
        plt.ylabel('Голы домашней команды', fontsize=13)
        plt.title('Зависимость голов домашней команды от позиции клуба', fontsize=15)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.tight_layout()
        plt.savefig('home_goals_vs_club_position_scatterplot.png')
        plt.show()

    def view_graph_7(self):
        clubs_normalized = pd.read_excel('../../data/new_normalized_data.xlsx',
                                         sheet_name='clubs_normalized')
        matches_normalized = pd.read_excel('../../data/new_normalized_data.xlsx',
                                           sheet_name='matches_normalized')
        club_managers = pd.read_excel('../../data/new_normalized_data.xlsx',
                                      sheet_name='club_managers')

        matches_count = matches_normalized.groupby('home_club_id').size().reset_index(name='matches_count')
        matches_count = matches_count.merge(clubs_normalized[['club_id', 'club_name']], left_on='home_club_id',
                                            right_on='club_id')

        # Рассчитаем позиции клубов на основе количества побед
        away_club_wins = matches_normalized.groupby('away_club_id')['away_club_goals'].count().reset_index(name='wins')
        away_club_wins['club_position'] = away_club_wins['wins'].rank(ascending=False, method='min')

        # Объединим информацию о позициях клубов с данными о матчах
        matches_with_positions_away = matches_normalized.merge(away_club_wins[['away_club_id', 'club_position']],
                                                               left_on='away_club_id', right_on='away_club_id')

        # График зависимости количества голов гостевой команды от позиции в таблице
        plt.figure(figsize=(12, 8))
        sns.scatterplot(data=matches_with_positions_away, x='club_position', y='away_club_goals', hue='season',
                        palette='viridis', s=100)
        plt.xlabel('Позиция в таблице', fontsize=13)
        plt.ylabel('Голы гостевой команды', fontsize=13)
        plt.title('Зависимость количества голов гостевой команды от позиции в таблице', fontsize=15)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.tight_layout()
        plt.savefig('away_goals_vs_club_position_scatterplot.png')
        plt.show()
       
    def view_graphs(self):
        clubs_normalized = pd.read_excel('../../data/new_normalized_data.xlsx',
                                         sheet_name='clubs_normalized')
        matches_normalized = pd.read_excel('../../data/new_normalized_data.xlsx',
                                           sheet_name='matches_normalized')
        club_managers = pd.read_excel('../../data/new_normalized_data.xlsx',
                                      sheet_name='club_managers')

        matches_count = matches_normalized.groupby('home_club_id').size().reset_index(name='matches_count')
        matches_count = matches_count.merge(clubs_normalized[['club_id', 'club_name']], left_on='home_club_id',
                                            right_on='club_id')

        top_30_matches_count = matches_count.sort_values(by='matches_count', ascending=False).head(204)

        colors = sns.color_palette('Purples', n_colors=30)[::-1]  # Выбор 30 цветов из палитры Purples

        # столбчатая гистограмма
        plt.figure(figsize=(12, 8))
        sns.barplot(x='club_name', y='matches_count', data=top_30_matches_count, hue='club_name', palette=colors,
                    legend=False)
        plt.xlabel('Название клуба', fontsize=12)
        plt.ylabel('Количество матчей', fontsize=12)
        plt.title('Топ-30 команд по количеству матчей', fontsize=14)
        plt.xticks(rotation=90, fontsize=10)
        plt.yticks(range(0, top_30_matches_count['matches_count'].max() + 1, 5))
        plt.tight_layout()
        plt.savefig('top_30_matches_per_club_barplot.png')
        plt.show()

        # группировка данных по тренерам и подсчет количества побед для каждого
        coach_wins = matches_normalized.groupby('home_club_manager_name').size().reset_index(name='wins')

        # выбор топ 20 тренеров с наибольшим количеством побед
        top_20_coaches = coach_wins.sort_values(by='wins', ascending=False).head(20)

        colors = sns.color_palette('Purples', n_colors=20)[::-1]  # Выбор 25 цветов из палитры Purples

        # построение категоризированной гистограммы
        plt.figure(figsize=(12, 8))
        sns.barplot(x='home_club_manager_name', y='wins', data=top_20_coaches, hue='home_club_manager_name',
                    palette=colors, saturation=1.5, legend=False)
        plt.xlabel('Имя тренера', fontsize=12)
        plt.ylabel('Количество побед', fontsize=12)
        plt.title('Топ 20 тренеров с наибольшим количеством побед', fontsize=14)
        plt.xticks(rotation=90, fontsize=10)
        plt.yticks(fontsize=10)
        plt.yticks(range(0, top_20_coaches['wins'].max() + 1, 2))
        plt.tight_layout()
        plt.savefig('top_20_coaches_wins_histogram_purple_gradient.png')
        plt.show()

        # для категоризированной диаграммы "box-and-whiskers"
        quant_qual_data_box = matches_normalized[['home_club_goals', 'competition_id']]
        colors = sns.color_palette('Purples', n_colors=29)[::-1]  # Выбор 29 цветов из палитры Purples

        # категоризированная диаграмма "box-and-whiskers"
        plt.figure(figsize=(12, 8))
        sns.boxplot(data=quant_qual_data_box, x='competition_id', y='home_club_goals', hue='competition_id',
                    palette=colors, legend=False)
        plt.xlabel('ID соревнования', fontsize=13)
        plt.ylabel('Голы домашнего клуба', fontsize=13)
        plt.title('Категоризированная диаграмма “box-and-whiskers”', fontsize=15)
        plt.tight_layout()
        plt.savefig('categorized_boxplot.png')
        plt.show()

        quant_quant_qual_data = matches_normalized[['home_club_goals', 'away_club_goals', 'competition_id']]

        # категоризированная диаграмма рассеивания
        plt.figure(figsize=(12, 8))
        sns.scatterplot(data=quant_quant_qual_data, x='home_club_goals', y='away_club_goals', hue='competition_id',
                        palette='viridis', s=100)
        plt.xlabel('Голы домашнего клуба', fontsize=13)
        plt.ylabel('Голы гостевого клуба', fontsize=13)
        plt.title('Категоризированная диаграмма рассеивания', fontsize=15)
        plt.legend(title='ID соревнования', fontsize=10)
        plt.tight_layout()
        plt.savefig('categorized_scatterplot.png')
        plt.show()

        # дополнительно????

        # Категоризированная гистограмма: распределение количества матчей по сезонам
        plt.figure(figsize=(12, 8))
        sns.histplot(data=matches_normalized, x='season', bins=10, kde=True)
        plt.xlabel('Сезон', fontsize=12)
        plt.ylabel('Частота', fontsize=12)
        plt.title('Распределение количества матчей по сезонам', fontsize=14)
        plt.xticks(rotation=45, fontsize=10)
        plt.yticks(fontsize=10)
        plt.tight_layout()
        plt.savefig('matches_per_season_histogram.png')
        plt.show()

        # Рассчитаем позиции клубов на основе количества побед
        home_club_wins = matches_normalized.groupby('home_club_id')['home_club_goals'].count().reset_index(name='wins')
        home_club_wins['club_position'] = home_club_wins['wins'].rank(ascending=False, method='min')

        # Объединим информацию о позициях клубов с данными о матчах
        matches_with_positions = matches_normalized.merge(home_club_wins[['home_club_id', 'club_position']],
                                                          left_on='home_club_id', right_on='home_club_id')

        # Построим диаграмму рассеивания
        plt.figure(figsize=(12, 8))
        sns.scatterplot(data=matches_with_positions, x='club_position', y='home_club_goals', hue='season',
                        palette='viridis', s=100)
        plt.xlabel('Позиция клуба', fontsize=13)
        plt.ylabel('Голы домашней команды', fontsize=13)
        plt.title('Зависимость голов домашней команды от позиции клуба', fontsize=15)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.tight_layout()
        plt.savefig('home_goals_vs_club_position_scatterplot.png')
        plt.show()

        # Рассчитаем позиции клубов на основе количества побед
        away_club_wins = matches_normalized.groupby('away_club_id')['away_club_goals'].count().reset_index(name='wins')
        away_club_wins['club_position'] = away_club_wins['wins'].rank(ascending=False, method='min')

        # Объединим информацию о позициях клубов с данными о матчах
        matches_with_positions_away = matches_normalized.merge(away_club_wins[['away_club_id', 'club_position']],
                                                               left_on='away_club_id', right_on='away_club_id')

        # График зависимости количества голов гостевой команды от позиции в таблице
        plt.figure(figsize=(12, 8))
        sns.scatterplot(data=matches_with_positions_away, x='club_position', y='away_club_goals', hue='season',
                        palette='viridis', s=100)
        plt.xlabel('Позиция в таблице', fontsize=13)
        plt.ylabel('Голы гостевой команды', fontsize=13)
        plt.title('Зависимость количества голов гостевой команды от позиции в таблице', fontsize=15)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.tight_layout()
        plt.savefig('away_goals_vs_club_position_scatterplot.png')
        plt.show()


if __name__ == "__main__":
    app = Application()
    app.mainloop()
