# -*- coding: utf-8 -*-
"""
Created on Sun May 9 22:04:57 2024

@author: Свистунов А.
"""
import tkinter as tk


def apply_filter(tree, club_id, clubs_df):
    """
    Применяет фильтр к данным и обновляет отображение дерева.

    Аргументы:
        tree (ttk. Treeview): Виджет Treeview, который отображает данные.
        club_id (str): Значение club_id для фильтрации данных.
        clubs_df (pandas.DataFrame): DataFrame, содержащий данные о клубах.

    Действия:
        Очищает текущее содержимое дерева и вставляет только те строки, которые
        соответствуют указанному club_id.
    """
    # Очищаем дерево перед применением фильтра
    tree.delete(*tree.get_children())

    # Применяем фильтр по club_id
    filtered_data = clubs_df.loc[clubs_df['club_id'] == int(club_id)]

    # Вставляем только отфильтрованные данные в дерево
    for index, row in filtered_data.iterrows():
        tree.insert("", tk.END, values=tuple(row))


def reset_filter(tree, entry_filter, clubs_df):
    """
    Сбрасывает фильтр и возвращает полное отображение данных в дереве.

    Аргументы:
        tree (ttk. Treeview): Виджет Treeview, который отображает данные.
        Entry_filter (tk. Entry): Поле ввода для значения club_id.
        Clubs_df (pandas. DataFrame): DataFrame, содержащий данные о клубах.

    Действия:
        Очищает поле ввода, очищает текущее содержимое дерева и вставляет
        все строки из DataFrame обратно в дерево.
    """
    # Очищаем поле ввода для фильтрации
    entry_filter.delete(0, tk.END)

    # Очищаем дерево
    tree.delete(*tree.get_children())

    # Вставляем все данные из DataFrame при загрузке
    for index, row in clubs_df.iterrows():
        tree.insert("", tk.END, values=tuple(row))
