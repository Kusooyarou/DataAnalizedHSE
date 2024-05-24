import pandas as pd
import os


def load_data(file_path, sheet_name):
    """Загрузить данные из файла Excel в DataFrame."""
    return pd.read_excel(file_path, sheet_name=sheet_name)


def save_data(file_path, **dataframes):
    """Сохранить несколько DataFrame в один Excel-файл."""
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        for sheet_name, df in dataframes.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)


def open_file(file_path):
    """Открыть файл с помощью приложения по умолчанию в системе."""
    try:
        os.startfile(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {file_path}")
    except Exception as e:
        raise Exception(f"Произошла ошибка при открытии файла: {e}")
