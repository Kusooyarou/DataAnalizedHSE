import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

output_folder = 'outputs'
os.makedirs(output_folder, exist_ok=True)


def view_graph_1():
    clubs_normalized = pd.read_excel("C:/Users/Andrey/Desktop/work2/DataAnalized/data/new_normalized_data.xlsx",
                                     sheet_name='clubs_normalized')
    matches_normalized = pd.read_excel("C:/Users/Andrey/Desktop/work2/DataAnalized/data/new_normalized_data.xlsx",
                                       sheet_name='matches_normalized')

    matches_count = matches_normalized.groupby('home_club_id').size().reset_index(name='matches_count')
    matches_count = matches_count.merge(clubs_normalized[['club_id', 'club_name']], left_on='home_club_id',
                                        right_on='club_id')

    top_30_matches_count = matches_count.sort_values(by='matches_count', ascending=False).head(204)
    colors = sns.color_palette('Purples', n_colors=30)[::-1]

    plt.figure(figsize=(12, 8))
    sns.barplot(x='club_name', y='matches_count', data=top_30_matches_count, hue='club_name', palette=colors,
                legend=False)
    plt.xlabel('Название клуба', fontsize=12)
    plt.ylabel('Количество матчей', fontsize=12)
    plt.title('Топ-30 команд по количеству матчей', fontsize=14)
    plt.xticks(rotation=90, fontsize=10)
    plt.yticks(range(0, top_30_matches_count['matches_count'].max() + 1, 5))
    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, 'top_30_matches_per_club_barplot.png'))
    plt.show()


def view_graph_2():
    matches_normalized = pd.read_excel("C:/Users/Andrey/Desktop/work2/DataAnalized/data/new_normalized_data.xlsx",
                                       sheet_name='matches_normalized')

    coach_wins = matches_normalized.groupby('home_club_manager_name').size().reset_index(name='wins')
    top_20_coaches = coach_wins.sort_values(by='wins', ascending=False).head(20)
    colors = sns.color_palette('Purples', n_colors=20)[::-1]

    plt.figure(figsize=(12, 8))
    sns.barplot(x='home_club_manager_name', y='wins', data=top_20_coaches, hue='home_club_manager_name', palette=colors,
                legend=False)
    plt.xlabel('Имя тренера', fontsize=12)
    plt.ylabel('Количество побед', fontsize=12)
    plt.title('Топ 20 тренеров с наибольшим количеством побед', fontsize=14)
    plt.xticks(rotation=90, fontsize=10)
    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, 'top_20_coaches_wins_histogram_purple_gradient.png'))
    plt.show()


def view_graph_3():
    matches_normalized = pd.read_excel("C:/Users/Andrey/Desktop/work2/DataAnalized/data/new_normalized_data.xlsx",
                                       sheet_name='matches_normalized')

    quant_qual_data_box = matches_normalized[['home_club_goals', 'competition_id']]
    colors = sns.color_palette('Purples', n_colors=29)[::-1]

    plt.figure(figsize=(12, 8))
    sns.boxplot(data=quant_qual_data_box, x='competition_id', y='home_club_goals', palette=colors, showfliers=False, legend=False, hue='competition_id')
    plt.xlabel('ID соревнования', fontsize=13)
    plt.ylabel('Голы домашнего клуба', fontsize=13)
    plt.title('Категоризированная диаграмма “box-and-whiskers”', fontsize=15)
    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, 'categorized_boxplot.png'))
    plt.show()


def view_graph_4():
    matches_normalized = pd.read_excel("C:/Users/Andrey/Desktop/work2/DataAnalized/data/new_normalized_data.xlsx",
                                       sheet_name='matches_normalized')

    quant_quant_qual_data = matches_normalized[['home_club_goals', 'away_club_goals', 'competition_id']]

    plt.figure(figsize=(12, 8))
    sns.scatterplot(data=quant_quant_qual_data, x='home_club_goals', y='away_club_goals', hue='competition_id',
                    palette='viridis', s=100)
    plt.xlabel('Голы домашнего клуба', fontsize=13)
    plt.ylabel('Голы гостевого клуба', fontsize=13)
    plt.title('Категоризированная диаграмма рассеивания', fontsize=15)
    plt.legend(title='ID соревнования', fontsize=10)
    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, 'categorized_scatterplot.png'))
    plt.show()


def view_graph_5():
    matches_normalized = pd.read_excel("C:/Users/Andrey/Desktop/work2/DataAnalized/data/new_normalized_data.xlsx",
                                       sheet_name='matches_normalized')

    plt.figure(figsize=(12, 8))
    sns.histplot(data=matches_normalized, x='season', bins=10, kde=True)
    plt.xlabel('Сезон', fontsize=12)
    plt.ylabel('Частота', fontsize=12)
    plt.title('Распределение количества матчей по сезонам', fontsize=14)
    plt.xticks(rotation=45, fontsize=10)
    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, 'matches_per_season_histogram.png'))
    plt.show()


def view_graph_6():
    matches_normalized = pd.read_excel("C:/Users/Andrey/Desktop/work2/DataAnalized/data/new_normalized_data.xlsx",
                                       sheet_name='matches_normalized')

    home_club_wins = matches_normalized.groupby('home_club_id')['home_club_goals'].count().reset_index(name='wins')
    home_club_wins['club_position'] = home_club_wins['wins'].rank(ascending=False, method='min')

    matches_with_positions = matches_normalized.merge(home_club_wins[['home_club_id', 'club_position']],
                                                      left_on='home_club_id', right_on='home_club_id')

    plt.figure(figsize=(12, 8))
    sns.scatterplot(data=matches_with_positions, x='club_position', y='home_club_goals', hue='season',
                    palette='viridis', s=100)
    plt.xlabel('Позиция клуба', fontsize=13)
    plt.ylabel('Голы домашней команды', fontsize=13)
    plt.title('Зависимость голов домашней команды от позиции клуба', fontsize=15)
    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, 'home_goals_vs_club_position_scatterplot.png'))
    plt.show()


def view_graph_7():
    clubs_normalized = pd.read_excel("C:/Users/Andrey/Desktop/work2/DataAnalized/data/new_normalized_data.xlsx",
                                     sheet_name='clubs_normalized')
    matches_normalized = pd.read_excel("C:/Users/Andrey/Desktop/work2/DataAnalized/data/new_normalized_data.xlsx",
                                       sheet_name='matches_normalized')
    club_managers = pd.read_excel("C:/Users/Andrey/Desktop/work2/DataAnalized/data/new_normalized_data.xlsx",
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
