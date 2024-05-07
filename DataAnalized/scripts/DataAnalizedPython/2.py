import pandas as pd

# Загрузка данных из Excel файла
df_football = pd.read_excel('C:/Users/Andrey/Desktop/final.xlsx', sheet_name='football data')
df_clubs = pd.read_excel('C:/Users/Andrey/Desktop/final.xlsx', sheet_name='clubs')
df_matches = pd.read_excel('C:/Users/Andrey/Desktop/final.xlsx', sheet_name='matches')
df_clubs = df_clubs.drop_duplicates(subset=['club_id'])

# Шаг 1: Создание уникальных идентификаторов для каждой таблицы
df_football['game_id'] = df_football['game_id'].astype(str)
df_football['match_id'] = 'M' + df_football['game_id']
df_clubs['club_id'] = df_clubs['club_id'].astype(str)
df_matches['match_id'] = df_matches['game_id'].astype(str)

# Шаг 2: Разделение данных о матчах на домашние и гостевые клубы
df_matches['home_team'] = df_matches['home_club_id'].map(df_clubs.set_index('club_id')['club_name'])
df_matches['away_team'] = df_matches['away_club_id'].map(df_clubs.set_index('club_id')['club_name'])

# Шаг 3: Установка связей между таблицами
df_football = df_football.merge(df_matches[['match_id', 'home_team', 'away_team', 'stadium', 'attendance', 'referee', 'url', 'aggregate', 'competition_type']], on='match_id', how='left')

# Шаг 4: Удаление избыточных столбцов
df_football.drop(['home_club_id', 'away_club_id'], axis=1, inplace=True)

# Шаг 5: Сохранение данных в новый файл Excel
df_football.to_excel('output_file.xlsx', index=False)
