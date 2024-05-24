# -*- coding: utf-8 -*-
"""
Created on Sun May 15 20:04:57 2024

@author: Бабенко А.
"""
import pandas as pd
import os


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
        data['home_club_manager_name'] = data['home_club_manager_name'].str.strip().str.lower()
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
                print(f"Произошла ошибка при создании отчета 'matches_per_club_report': {error}")
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
                print(f"Произошла ошибка при создании отчета 'matches_per_coach_report': {error}")
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
                avg_goals_per_match = matches_data[['home_club_goals', 'away_club_goals']].mean().mean()

                # Строим сводную таблицу
                pivot_table = pd.DataFrame({'Среднее количество голов в матче': [avg_goals_per_match]})

                return pivot_table
            except Exception as error:
                print(f"Произошла ошибка при создании отчета 'average_goals_per_match_report': {error}")
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
                matches_per_season = matches_data.groupby('season').size().reset_index(name='matches_count')

                # Строим сводную таблицу
                pivot_table = matches_per_season.set_index('season')

                return pivot_table
            except Exception as error:
                print(f"Произошла ошибка при создании отчета 'matches_per_season_report': {error}")
                return pd.DataFrame()

        reports['Отчёт матчей по тренерам'] = (matches_per_club_report
                                               (matches_normalized, clubs_normalized))
        reports['Отчёт матчей по клубам'] = matches_per_coach_report(matches_normalized)
        reports['Отчёт среднее по голам'] = average_goals_per_match_report(matches_normalized)
        reports['Отчёт матчи по сезонам'] = matches_per_season_report(matches_normalized)

    except Exception as e:
        print(f"Произошла ошибка при генерации отчетов: {e}")

    return reports


def main():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    data_file_path = os.path.join(base_dir, "..", "data", "new_normalized_data.xlsx")
    clubs_normalized = pd.read_excel(data_file_path,
                                     sheet_name='clubs_normalized')
    matches_normalized = pd.read_excel(data_file_path,
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
