import pandas as pd

clubs_df = pd.read_excel('C:/Users/Andrey/Desktop/normalized_2_form.xlsx', sheet_name='clubs')
matches_df = pd.read_excel('C:/Users/Andrey/Desktop/normalized_2_form.xlsx', sheet_name='matches')

club_managers_df = clubs_df[['club_id', 'club_manager_name']].drop_duplicates().reset_index(drop=True)

matches_df = matches_df.drop(['stadium', 'attendance', 'referee', 'url', 'aggregate', 'competition_type'], axis=1)

matches_df = matches_df.merge(club_managers_df, left_on='home_club_id', right_on='club_id', how='left') \
    .rename(columns={'club_manager_name': 'home_club_manager_name'}) \
    .drop('club_id', axis=1)

matches_df = matches_df.merge(club_managers_df, left_on='away_club_id', right_on='club_id', how='left') \
    .rename(columns={'club_manager_name': 'away_club_manager_name'}) \
    .drop('club_id', axis=1)

with pd.ExcelWriter('normalized_data.xlsx') as writer:
    clubs_df.to_excel(writer, sheet_name='clubs_normalized', index=False)
    matches_df.to_excel(writer, sheet_name='matches_normalized', index=False)
    club_managers_df.to_excel(writer, sheet_name='club_managers', index=False)
