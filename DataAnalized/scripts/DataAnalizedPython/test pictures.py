import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных
matches_normalized = pd.read_excel('C:/Users/Andrey/Desktop/new_normalized_data.xlsx', sheet_name='matches_normalized')

# Построение диаграммы рассеивания
plt.figure(figsize=(12, 8))
plt.scatter(matches_normalized['home_club_goals'], matches_normalized['away_club_goals'], c='blue', alpha=0.5)
plt.xlabel('Голы домашней команды', fontsize=13)
plt.ylabel('Голы гостевой команды', fontsize=13)
plt.title('Зависимость количества голов домашней команды от голов гостевой команды', fontsize=15)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.savefig('home_goals_vs_away_goals_scatterplot.png')
plt.show()