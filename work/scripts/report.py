# -*- coding: utf-8 -*-
"""
Created on Sun May 15 20:04:57 2024

@author: Бабенко А.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Очищает данные, удаляя ведущие и завершающие пробелы и преобразуя строки к нижнему регистру.

    Parameters
    ----------
    data : pd.DataFrame
        Входной DataFrame, который нужно очистить.

    Returns
    -------
    pd.DataFrame
        Очищенный DataFrame.

    """
    if 'home_club_manager_name' in data.columns:
        data['home_club_manager_name'] = data['home_club_manager_name'].str.strip(
        ).str.lower()
    return data


def generate_text_reports(clubs_normalized: pd.DataFrame, matches_normalized: pd.DataFrame) -> dict:
    """
    Генерирует текстовые отчеты на основе предоставленных данных.

    Parameters
    ----------
    clubs_normalized : pd.DataFrame
        Данные о клубах.
    matches_normalized : pd.DataFrame
        Данные о матчах.

    Returns
    -------
    dict
        Словарь, где ключ - название отчета, значение - сводная таблица.
    """
    reports = {}

    try:
        def matches_per_club_report(matches_data: pd.DataFrame, clubs_data: pd.DataFrame) -> pd.DataFrame:
            """
            Отчет о количестве матчей, проведенных каждым клубом.

            Parameters
            ----------
            matches_data : pd.DataFrame
                Данные о матчах.
            clubs_data : pd.DataFrame
                Данные о клубах.

            Returns
            -------
            pd.DataFrame
                Сводная таблица.
            """
            try:
                # Объединяем данные о матчах с данными о клубах для получения названий клубов
                merged_data = matches_data.merge(clubs_data[['club_id', 'club_name']], left_on='home_club_id',
                                                 right_on='club_id', how='left')

                # Строим сводную таблицу
                pivot_table = pd.pivot_table(merged_data, index='club_name', columns='season', values='game_id',
                                             aggfunc='count', fill_value=0)

                return pivot_table
            except Exception as error:
                print(
                    f"Произошла ошибка при создании отчета 'matches_per_club_report': {error}")
                return pd.DataFrame()

        def matches_per_coach_report(matches_data: pd.DataFrame) -> pd.DataFrame:
            """
            Отчет о количестве матчей, проведенных каждым тренером.

            Parameters
            ----------
            matches_data : pd.DataFrame
                Данные о матчах.

            Returns
            -------
            pd.DataFrame
                Сводная таблица.
            """
            try:
                # Группируем данные о матчах по домашнему тренеру и считаем количество матчей
                matches_count_per_coach = matches_data.groupby('home_club_manager_name').size().reset_index(
                    name='matches_count')

                # Строим сводную таблицу
                pivot_table = pd.pivot_table(matches_count_per_coach, index='home_club_manager_name',
                                             values='matches_count', aggfunc='sum')

                return pivot_table
            except Exception as error:
                print(
                    f"Произошла ошибка при создании отчета 'matches_per_coach_report': {error}")
                return pd.DataFrame()

        def average_goals_per_match_report(matches_data: pd.DataFrame) -> pd.DataFrame:
            """
            Отчет о среднем количестве голов в матче.

            Parameters
            ----------
            matches_data : pd.DataFrame
                Данные о матчах.

            Returns
            -------
            pd.DataFrame
                Сводная таблица.
            """
            try:
                # Считаем среднее количество голов в матче
                avg_goals_per_match = matches_data[[
                    'home_club_goals', 'away_club_goals']].mean().mean()

                # Строим сводную таблицу
                pivot_table = pd.DataFrame(
                    {'Среднее количество голов в матче': [avg_goals_per_match]})

                return pivot_table
            except Exception as error:
                print(
                    f"Произошла ошибка при создании отчета 'average_goals_per_match_report': {error}")
                return pd.DataFrame()

        def matches_per_season_report(matches_data: pd.DataFrame) -> pd.DataFrame:
            """
            Отчет о количестве матчей в разные сезоны.

            Parameters
            ----------
            matches_data : pd.DataFrame
                Данные о матчах.

            Returns
            -------
            pd.DataFrame
                Сводная таблица.
            """
            try:
                # Группируем данные о матчах по сезону и считаем количество матчей
                matches_per_season = matches_data.groupby(
                    'season').size().reset_index(name='matches_count')

                # Строим сводную таблицу
                pivot_table = matches_per_season.set_index('season')

                return pivot_table
            except Exception as error:
                print(
                    f"Произошла ошибка при создании отчета 'matches_per_season_report': {error}")
                return pd.DataFrame()

        reports['Отчёт матчей по тренерам'] = (matches_per_club_report
                                               (matches_normalized, clubs_normalized))
        reports['Отчёт матчей по клубам'] = matches_per_coach_report(
            matches_normalized)
        reports['Отчёт среднее по голам'] = average_goals_per_match_report(
            matches_normalized)
        reports['Отчёт матчи по сезонам'] = matches_per_season_report(
            matches_normalized)

    except Exception as e:
        print(f"Произошла ошибка при генерации отчетов: {e}")

    return reports


def generate_graphical_reports():
    """
    Генерирует графические отчеты на основе предоставленных данных.

    Возвращает
    -------
    None
        Сохраняет графики в файлы и отображает их.

    """

    try:
        clubs_normalized = pd.read_excel('../data/new_normalized_data.xlsx',
                                         sheet_name='clubs_normalized')
        matches_normalized = pd.read_excel('../data/new_normalized_data.xlsx',
                                           sheet_name='matches_normalized')
        # club_managers = pd.read_excel('../data/new_normalized_data.xlsx',
        #                              sheet_name='club_managers')

        matches_count = matches_normalized.groupby(
            'home_club_id').size().reset_index(name='matches_count')
        matches_count = matches_count.merge(clubs_normalized[['club_id', 'club_name']],
                                            left_on='home_club_id', right_on='club_id')

        top_30_matches_count = matches_count.sort_values(
            by='matches_count', ascending=False).head(204)

        colors = sns.color_palette('Purples', n_colors=30)[
            ::-1]  # Выбор 30 цветов из палитры Purples

        # столбчатая гистограмма
        plt.figure(figsize=(12, 8))
        sns.barplot(x='club_name', y='matches_count', data=top_30_matches_count, hue='club_name', palette=colors,
                    legend=False)
        plt.xlabel('Название клуба', fontsize=12)
        plt.ylabel('Количество матчей', fontsize=12)
        plt.title('Топ-30 команд по количеству матчей', fontsize=14)
        plt.xticks(rotation=90, fontsize=10)
        plt.yticks(
            range(0, top_30_matches_count['matches_count'].max() + 1, 5))
        plt.tight_layout()
        plt.savefig('top_30_matches_per_club_bar plot.png')
        plt.show()

        # Подсчет количества побед для каждого тренера
        coach_wins = matches_normalized.groupby(
            'home_club_manager_name').size().reset_index(name='wins')

        # Выбор топ 20 тренеров с наибольшим количеством побед
        top_20_coaches = coach_wins.sort_values(
            by='wins', ascending=False).head(20)

        colors = sns.color_palette('Purples', n_colors=20)[::-1]

        # Категоризированная диаграмма
        plt.figure(figsize=(12, 8))  # Увеличиваем размер графика
        sns.barplot(x='home_club_manager_name', y='wins', data=top_20_coaches,
                    hue='home_club_manager_name', palette=colors,
                    saturation=1.5, legend=False)
        plt.xlabel('Имя тренера', fontsize=12)
        plt.ylabel('Количество побед', fontsize=12)
        plt.title('Топ-20 тренеров по количеству побед', fontsize=14)
        # Поворачиваем и смещаем подписи оси x
        plt.xticks(rotation=45, ha='right', fontsize=10)
        plt.yticks(fontsize=10)
        plt.tight_layout()
        plt.savefig('top_20_coaches_wins_bar plot.png')
        plt.show()

        # для категоризированной диаграммы "box-and-whiskers"
        quant_quail_data_box = matches_normalized[[
            'home_club_goals', 'competition_id']]
        colors = sns.color_palette('Purples', n_colors=29)[
            ::-1]  # Выбор 29 цветов из палитры Purples

        # категоризированная диаграмма "box-and-whiskers"
        plt.figure(figsize=(12, 8))
        sns.boxplot(data=quant_quail_data_box, x='competition_id', y='home_club_goals', hue='competition_id',
                    palette=colors, legend=False)
        plt.xlabel('ID соревнования', fontsize=13)
        plt.ylabel('Голы домашнего клуба', fontsize=13)
        plt.title('Категоризированная диаграмма “box-and-whiskers”', fontsize=15)
        plt.tight_layout()
        plt.savefig('categorized_boxplot.png')
        plt.show()

        quant_quant_quail_data = matches_normalized[[
            'home_club_goals', 'away_club_goals', 'competition_id']]

        # категоризированная диаграмма рассеивания
        plt.figure(figsize=(12, 8))
        sns.scatterplot(data=quant_quant_quail_data, x='home_club_goals', y='away_club_goals', hue='competition_id',
                        palette='viridis', s=100)
        plt.xlabel('Голы домашнего клуба', fontsize=13)
        plt.ylabel('Голы гостевого клуба', fontsize=13)
        plt.title('Категоризированная диаграмма рассеивания', fontsize=15)
        plt.legend(title='ID соревнования', fontsize=10)
        plt.tight_layout()
        plt.savefig('categorized_scatterplot.png')
        plt.show()

        # категоризированная гистограмма: распределение количества матчей по сезонам
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

        # рассчитаем позиции клубов на основе количества побед
        home_club_wins = (matches_normalized.groupby('home_club_id')['home_club_goals'].
                          count().reset_index(name='wins'))
        home_club_wins['club_position'] = home_club_wins['wins'].rank(
            ascending=False, method='min')

        # Объединим информацию о позициях клубов с данными о матчах
        matches_with_positions = matches_normalized.merge(home_club_wins[['home_club_id', 'club_position']],
                                                          left_on='home_club_id', right_on='home_club_id')

        # Построим диаграмму рассеивания
        plt.figure(figsize=(12, 8))
        sns.scatterplot(data=matches_with_positions, x='club_position', y='home_club_goals', hue='season',
                        palette='viridis', s=100)
        plt.xlabel('Позиция клуба', fontsize=13)
        plt.ylabel('Голы домашней команды', fontsize=13)
        plt.title(
            'Зависимость голов домашней команды от позиции клуба', fontsize=15)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.tight_layout()
        plt.savefig('home_goals_vs_club_position_scatterplot.png')
        plt.show()

        # Рассчитаем позиции клубов на основе количества побед
        away_club_wins = matches_normalized.groupby(
            'away_club_id')['away_club_goals'].count().reset_index(name='wins')
        away_club_wins['club_position'] = away_club_wins['wins'].rank(
            ascending=False, method='min')

        # Объединим информацию о позициях клубов с данными о матчах
        matches_with_positions_away = matches_normalized.merge(away_club_wins[['away_club_id', 'club_position']],
                                                               left_on='away_club_id', right_on='away_club_id')

        # График зависимости количества голов гостевой команды от позиции в таблице
        plt.figure(figsize=(12, 8))
        sns.scatterplot(data=matches_with_positions_away, x='club_position', y='away_club_goals', hue='season',
                        palette='viridis', s=100)
        plt.xlabel('Позиция в таблице', fontsize=13)
        plt.ylabel('Голы гостевой команды', fontsize=13)
        plt.title(
            'Зависимость количества голов гостевой команды от позиции в таблице', fontsize=15)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.tight_layout()
        plt.savefig('away_goals_vs_club_position_scatterplot.png')
        plt.show()

        # сгруппируем данные по типу формации и подсчитаем количество побед для каждой формации
        formation_wins = matches_normalized.merge(clubs_normalized[['club_id', 'club_formation']],
                                                  left_on='home_club_id',
                                                  right_on='club_id')
        formation_wins = formation_wins.groupby(
            'club_formation').size().reset_index(name='wins')
        formation_wins = formation_wins.sort_values(by='wins', ascending=False)

        # выберем топ-10 расстановок по победам
        top_10_formations = formation_wins.head(10)

        colors = sns.color_palette('Purples', n_colors=10)[
            ::-1]  # Выбор 10 цветов из палитры Purples

        # топ-10 расстановок по победам
        plt.figure(figsize=(12, 8))
        sns.barplot(x='club_formation', y='wins', data=top_10_formations, palette=colors, hue='club_formation',
                    legend=False)
        plt.xlabel('Тип формации клуба', fontsize=12)
        plt.ylabel('Количество побед', fontsize=12)
        plt.title('Топ-10 формаций клубов по количеству побед', fontsize=14)
        plt.xticks(rotation=45, ha='right', fontsize=10)
        plt.yticks(fontsize=10)
        plt.tight_layout()
        plt.savefig('top_10_formations_wins_bar plot_seaborn.png')
        plt.show()

        # диаграмма рассеивания количества голов домашней команды от голов гостевой команды
        plt.figure(figsize=(12, 8))
        sns.scatterplot(data=matches_normalized, x='home_club_goals', y='away_club_goals', hue='home_club_goals',
                        palette='viridis', s=100)
        plt.xlabel('Голы домашней команды', fontsize=13)
        plt.ylabel('Голы гостевой команды', fontsize=13)
        plt.title(
            'Зависимость количества голов домашней команды от голов гостевой команды', fontsize=15)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.tight_layout()
        plt.savefig('home_goals_vs_away_goals_scatterplot_seaborn.png')
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")


generate_graphical_reports()


def main():
    clubs_normalized = pd.read_excel('../data/new_normalized_data.xlsx',
                                     sheet_name='clubs_normalized')
    matches_normalized = pd.read_excel('../data/new_normalized_data.xlsx',
                                       sheet_name='matches_normalized')

    if not clubs_normalized.empty and not matches_normalized.empty:
        reports = generate_text_reports(clubs_normalized, matches_normalized)

        with pd.ExcelWriter('reports.xlsx', engine='openpyxl') as writer:
            for report_name, report_table in reports.items():
                report_table.to_excel(writer, sheet_name=report_name)

        print("Отчеты успешно записаны в файл Excel.")
    else:
        print("Не удалось загрузить данные для генерации отчетов.")


if __name__ == "__main__":
    main()
