# -*- coding: utf-8 -*-
"""
Created on Sun May 15 20:04:57 2024

@author: Свистунов А.
"""
import pandas as pd
import os


def load_data(file_path, sheet_name):
    """
    Загружает данные из файла Excel в объект DataFrame.

    Параметры:
        file_path (str): Путь к файлу Excel.
        sheet_name (str): Название листа, из которого следует загрузить данные.

    Возвращает:
        pandas.DataFrame: DataFrame с загруженными данными из указанного листа файла Excel.
    """
    return pd.read_excel(file_path, sheet_name=sheet_name)


def save_data(file_path, **dataframes):
    """
    Сохраняет несколько DataFrame в один Excel-файл.

    Параметры:
        file_path (str): Путь к файлу Excel.
        **dataframes: Набор именованных аргументов, где ключ - название листа, а значение - DataFrame.

    Выход:
        None
    """
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        for sheet_name, df in dataframes.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)


def open_file(file_path):
    """
    Открывает файл с помощью приложения по умолчанию в системе.

    Параметры:
        file_path (str): Путь к файлу, который нужно открыть.

    Выход:
        None
    """
    try:
        os.startfile(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {file_path}")
    except Exception as e:
        raise Exception(f"Произошла ошибка при открытии файла: {e}")
