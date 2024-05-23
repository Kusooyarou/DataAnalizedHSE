import tkinter as tk

def apply_filter(tree, club_id, clubs_df):
    # Очищаем дерево перед применением фильтра
    tree.delete(*tree.get_children())

    # Применяем фильтр по club_id
    filtered_data = clubs_df.loc[clubs_df['club_id'] == int(club_id)]

    # Вставляем только отфильтрованные данные в дерево
    for index, row in filtered_data.iterrows():
        tree.insert("", tk.END, values=tuple(row))

def reset_filter(tree, entry_filter, clubs_df):
    # Очищаем поле ввода для фильтрации
    entry_filter.delete(0, tk.END)

    # Очищаем дерево
    tree.delete(*tree.get_children())

    # Вставляем все данные из DataFrame при загрузке
    for index, row in clubs_df.iterrows():
        tree.insert("", tk.END, values=tuple(row))
