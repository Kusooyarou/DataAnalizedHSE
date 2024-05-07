import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

clubs_normalized = pd.read_excel('C:/Users/Andrey/Desktop/work/data/new_normalized_data.xlsx',
                                 sheet_name='clubs_normalized')
matches_normalized = pd.read_excel('C:/Users/Andrey/Desktop/work/data/new_normalized_data.xlsx',
                                   sheet_name='matches_normalized')
club_managers = pd.read_excel('C:/Users/Andrey/Desktop/work/data/new_normalized_data.xlsx',
                              sheet_name='club_managers')

matches_count = matches_normalized.groupby('home_club_id').size().reset_index(name='matches_count')
matches_count = matches_count.merge(clubs_normalized[['club_id', 'club_name']],
                                    left_on='home_club_id', right_on='club_id')

top_30_matches_count = matches_count.sort_values(by='matches_count', ascending=False).head(204)

colors = sns.color_palette('Purples', n_colors=30)[::-1]  # Выбор 30 цветов из палитры Purples

# столбчатая гистограмма
plt.figure(figsize=(12, 8))
sns.barplot(x='club_name', y='matches_count', data=top_30_matches_count, hue='club_name', palette=colors, legend=False)
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

colors = sns.color_palette('Purples', n_colors=20)[::-1]  # Выбор 20 цветов из палитры Purples

# построение категоризированной гистограммы
plt.figure(figsize=(12, 8))
sns.barplot(x='home_club_manager_name', y='wins', data=top_20_coaches, hue='home_club_manager_name', palette=colors,
            saturation=1.5, legend=False)
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

# сгруппируем данные по типу формации и подсчитаем количество побед для каждой формации
formation_wins = matches_normalized.merge(clubs_normalized[['club_id', 'club_formation']], left_on='home_club_id',
                                          right_on='club_id')
formation_wins = formation_wins.groupby('club_formation').size().reset_index(name='wins')
formation_wins = formation_wins.sort_values(by='wins', ascending=False)

# выберем топ-10 расстановок по победам
top_10_formations = formation_wins.head(10)

colors = sns.color_palette('Purples', n_colors=10)[::-1]  # Выбор 10 цветов из палитры Purples

# топ-10 расстановок по победам
plt.figure(figsize=(12, 8))
sns.barplot(x='club_formation', y='wins', data=top_10_formations, palette=colors, hue='club_formation', legend=False)
plt.xlabel('Тип формации клуба', fontsize=12)
plt.ylabel('Количество побед', fontsize=12)
plt.title('Топ-10 формаций клубов по количеству побед', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.savefig('top_10_formations_wins_barplot_seaborn.png')
plt.show()

# диаграмма рассеивания количества голов домашней команды от голов гостевой команды
plt.figure(figsize=(12, 8))
sns.scatterplot(data=matches_normalized, x='home_club_goals', y='away_club_goals', palette='viridis', s=100)
plt.xlabel('Голы домашней команды', fontsize=13)
plt.ylabel('Голы гостевой команды', fontsize=13)
plt.title('Зависимость количества голов домашней команды от голов гостевой команды', fontsize=15)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.savefig('home_goals_vs_away_goals_scatterplot_seaborn.png')
plt.show()