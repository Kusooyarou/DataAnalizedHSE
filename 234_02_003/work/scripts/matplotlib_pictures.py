# -*- coding: utf-8 -*-
"""
Created on Sun May 15 20:04:57 2024

@author: Бабенко А. Осинцев К.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os


def load_and_process_data():
    """
    Загружает и обрабатывает данные из файла Excel.

    Параметры:
        file_path (str): Путь к файлу Excel.

    Возвращает:
        pandas.DataFrame: DataFrame с данными о клубах.
        pandas.DataFrame: DataFrame с данными о матчах.
        pandas.DataFrame: DataFrame с данными о менеджерах клубов.
    """
    base_dir = os.path.abspath(os.path.dirname(__file__))
    data_file_path = os.path.join(
        base_dir, "..", "data", "new_normalized_data.xlsx")

    clubs_normalized = pd.read_excel(
        data_file_path, sheet_name='clubs_normalized')
    matches_normalized = pd.read_excel(
        data_file_path, sheet_name='matches_normalized')
    club_managers = pd.read_excel(data_file_path, sheet_name='club_managers')

    return clubs_normalized, matches_normalized, club_managers


# График топ-30 команд по количеству матчей
def plot_top_30_matches_per_club(clubs_normalized, matches_normalized):
    """
    График топ-30 команд по количеству матчей.

    Параметры:
        clubs_normalized (pandas.DataFrame): DataFrame с данными о клубах.
        matches_normalized (pandas.DataFrame): DataFrame с данными о матчах.

    Возвращает:
        None
    """
    matches_count = matches_normalized.groupby(
        'home_club_id').size().reset_index(name='matches_count')
    matches_count = matches_count.merge(clubs_normalized[['club_id', 'club_name']], left_on='home_club_id',
                                        right_on='club_id')
    top_30_matches_count = matches_count.sort_values(
        by='matches_count', ascending=False).head(204)

    plt.figure(figsize=(12, 8))
    plt.bar(top_30_matches_count['club_name'],
            top_30_matches_count['matches_count'], color='purple')
    plt.xlabel('Название клуба', fontsize=12)
    plt.ylabel('Количество матчей', fontsize=12)
    plt.title('Топ-30 команд по количеству матчей', fontsize=14)
    plt.xticks(rotation=90, fontsize=10)
    plt.tight_layout()
    plt.savefig('top_30_matches_per_club_barplot.png')
    plt.show()


# График топ-20 тренеров с наибольшим количеством побед
def plot_top_20_coaches_wins(matches_normalized):
    """
    График топ-20 тренеров с наибольшим количеством побед.

    Параметры:
        matches_normalized (pandas.DataFrame): DataFrame с данными о матчах.

    Возвращает:
        None
    """
    coach_wins = matches_normalized.groupby(
        'home_club_manager_name').size().reset_index(name='wins')
    top_20_coaches = coach_wins.sort_values(
        by='wins', ascending=False).head(20)

    plt.figure(figsize=(12, 8))
    plt.bar(top_20_coaches['home_club_manager_name'],
            top_20_coaches['wins'], color='purple')
    plt.xlabel('Имя тренера', fontsize=12)
    plt.ylabel('Количество побед', fontsize=12)
    plt.title('Топ 20 тренеров с наибольшим количеством побед', fontsize=14)
    plt.xticks(rotation=90, fontsize=10)
    plt.tight_layout()
    plt.savefig('top_20_coaches_wins_histogram_purple.png')
    plt.show()


# Категоризированная диаграмма "box-and-whiskers"
def plot_categorized_boxplot(matches_normalized):
    """
    Категоризированная диаграмма "box-and-whiskers".

    Параметры:
        matches_normalized (pandas.DataFrame): DataFrame с данными о матчах.

    Возвращает:
        None
    """
    quant_qual_data_box = matches_normalized[[
        'home_club_goals', 'competition_id']]

    plt.figure(figsize=(12, 8))
    plt.boxplot([quant_qual_data_box[quant_qual_data_box['competition_id'] == i]['home_club_goals'] for i in
                 quant_qual_data_box['competition_id'].unique()], patch_artist=True)
    plt.xlabel('ID соревнования', fontsize=13)
    plt.ylabel('Голы домашнего клуба', fontsize=13)
    plt.title('Категоризированная диаграмма “box-and-whiskers”', fontsize=15)
    plt.tight_layout()
    plt.savefig('categorized_boxplot.png')
    plt.show()


# Категоризированная диаграмма рассеивания
def plot_categorized_scatterplot(matches_normalized):
    """
    Категоризированная диаграмма рассеивания.

    Параметры:
        matches_normalized (pandas.DataFrame): DataFrame с данными о матчах.

    Возвращает:
        None
    """
    quant_quant_qual_data = matches_normalized[[
        'home_club_goals', 'away_club_goals', 'competition_id']]

    plt.figure(figsize=(12, 8))
    for competition_id in quant_quant_qual_data['competition_id'].unique():
        data = quant_quant_qual_data[quant_quant_qual_data['competition_id']
                                     == competition_id]
        plt.scatter(data['home_club_goals'], data['away_club_goals'],
                    label=f'Competition ID {competition_id}', s=100)
    plt.xlabel('Голы домашнего клуба', fontsize=13)
    plt.ylabel('Голы гостевого клуба', fontsize=13)
    plt.title('Категоризированная диаграмма рассеивания', fontsize=15)
    plt.legend(title='ID соревнования', fontsize=10)
    plt.tight_layout()
    plt.savefig('categorized_scatterplot.png')
    plt.show()


# Распределение количества матчей по сезонам
def plot_matches_per_season(matches_normalized):
    """
    Распределение количества матчей по сезонам.

    Параметры:
        matches_normalized (pandas.DataFrame): DataFrame с данными о матчах.

    Возвращает:
        None
    """
    matches_per_season = matches_normalized['season'].value_counts(
    ).sort_index()

    plt.figure(figsize=(12, 8))
    plt.bar(matches_per_season.index, matches_per_season.values, color='purple')
    plt.xlabel('Сезон', fontsize=12)
    plt.ylabel('Частота', fontsize=12)
    plt.title('Распределение количества матчей по сезонам', fontsize=14)
    plt.xticks(rotation=45, fontsize=10)
    plt.tight_layout()
    plt.savefig('matches_per_season_histogram.png')
    plt.show()


# Зависимость голов домашней команды от позиции клуба
def plot_home_goals_vs_club_position(matches_normalized):
    """
    Зависимость голов домашней команды от позиции клуба.

    Параметры:
        matches_normalized (pandas.DataFrame): DataFrame с данными о матчах.

    Возвращает:
        None
    """
    home_club_wins = matches_normalized.groupby(
        'home_club_id')['home_club_goals'].count().reset_index(name='wins')
    home_club_wins['club_position'] = home_club_wins['wins'].rank(
        ascending=False, method='min')
    matches_with_positions = matches_normalized.merge(home_club_wins[['home_club_id', 'club_position']],
                                                      left_on='home_club_id', right_on='home_club_id')

    plt.figure(figsize=(12, 8))
    plt.scatter(matches_with_positions['club_position'], matches_with_positions['home_club_goals'],
                c=matches_with_positions['season'], cmap='viridis', s=100)
    plt.xlabel('Позиция клуба', fontsize=13)
    plt.ylabel('Голы домашней команды', fontsize=13)
    plt.title('Зависимость голов домашней команды от позиции клуба', fontsize=15)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.colorbar(label='Сезон')
    plt.tight_layout()
    plt.savefig('home_goals_vs_club_position_scatterplot.png')
    plt.show()


# Зависимость голов гостевой команды от позиции в таблице
def plot_away_goals_vs_club_position(matches_normalized):
    """
    Зависимость голов гостевой команды от позиции в таблице.

    Параметры:
        matches_normalized (pandas.DataFrame): DataFrame с данными о матчах.

    Возвращает:
        None
    """
    away_club_wins = matches_normalized.groupby(
        'away_club_id')['away_club_goals'].count().reset_index(name='wins')
    away_club_wins['club_position'] = away_club_wins['wins'].rank(
        ascending=False, method='min')
    matches_with_positions_away = matches_normalized.merge(away_club_wins[['away_club_id', 'club_position']],
                                                           left_on='away_club_id', right_on='away_club_id')
    plt.figure(figsize=(12, 8))
    plt.scatter(matches_with_positions_away['club_position'], matches_with_positions_away['away_club_goals'],
                c=matches_with_positions_away['season'], cmap='viridis', s=100)
    plt.xlabel('Позиция в таблице', fontsize=13)
    plt.ylabel('Голы гостевой команды', fontsize=13)
    plt.title(
        'Зависимость количества голов гостевой команды от позиции в таблице', fontsize=15)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.colorbar(label='Сезон')
    plt.tight_layout()
    plt.savefig('away_goals_vs_club_position_scatterplot.png')
    plt.show()


# Топ-10 расстановок клубов по количеству побед
def plot_top_10_formations_wins(matches_normalized, clubs_normalized):
    """
    Топ-10 расстановок клубов по количеству побед.

    Параметры:
        matches_normalized (pandas.DataFrame): DataFrame с данными о матчах.
        clubs_normalized (pandas.DataFrame): DataFrame с данными о клубах.

    Возвращает:
        None
    """
    # Сгруппировать данные по типу формации и подсчитать количество побед для каждой формации
    formation_wins = matches_normalized.merge(clubs_normalized[['club_id', 'club_formation']], left_on='home_club_id',
                                              right_on='club_id')
    formation_wins = formation_wins.groupby(
        'club_formation').size().reset_index(name='wins')
    formation_wins = formation_wins.sort_values(by='wins', ascending=False)

    # Выбрать топ-10 расстановок по победам
    top_10_formations = formation_wins.head(10)

    plt.figure(figsize=(12, 8))
    plt.bar(top_10_formations['club_formation'],
            top_10_formations['wins'], color='purple')
    plt.xlabel('Тип формации клуба', fontsize=13)
    plt.ylabel('Количество побед', fontsize=13)
    plt.title('Топ-10 расстановок клубов по количеству побед', fontsize=14)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()
    plt.savefig('top_10_formations_wins_barplot.png')
    plt.show()


# Диаграмма рассеивания: Зависимость количества голов домашней команды от голов гостевой команды
def plot_home_goals_vs_away_goals_scatterplot(matches_normalized):
    """
    Диаграмма рассеивания: Зависимость количества голов домашней команды от голов гостевой команды.

    Параметры:
        matches_normalized (pandas.DataFrame): DataFrame с данными о матчах.

    Возвращает:
        None
    """
    plt.figure(figsize=(12, 8))
    plt.scatter(matches_normalized['home_club_goals'],
                matches_normalized['away_club_goals'], c='blue', alpha=0.5)
    plt.xlabel('Голы домашней команды', fontsize=13)
    plt.ylabel('Голы гостевой команды', fontsize=13)
    plt.title(
        'Зависимость количества голов домашней команды от голов гостевой команды', fontsize=15)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()
    plt.savefig('home_goals_vs_away_goals_scatterplot.png')
    plt.show()


base_dir = os.path.abspath(os.path.dirname(__file__))
data_file_path = os.path.join(
    base_dir, "..", "data", "new_normalized_data.xlsx")
# Загрузка и обработка данных
clubs_normalized, matches_normalized, club_managers = load_and_process_data()

# Графики
plot_top_30_matches_per_club(clubs_normalized, matches_normalized)
plot_top_20_coaches_wins(matches_normalized)
plot_categorized_boxplot(matches_normalized)
plot_categorized_scatterplot(matches_normalized)
plot_matches_per_season(matches_normalized)
plot_home_goals_vs_club_position(matches_normalized)
plot_away_goals_vs_club_position(matches_normalized)
plot_top_10_formations_wins(matches_normalized, clubs_normalized)
plot_home_goals_vs_away_goals_scatterplot(matches_normalized)
