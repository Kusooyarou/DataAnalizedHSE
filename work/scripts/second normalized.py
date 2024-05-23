import pandas as pd

data = {
    'game_id': [4103526, 4103555, 4103557, 4103602, 4103622, 4103683, 4103685, 4103738, 4103745, 4104307, 4109307, 4109338, 4109411, 4109470],
    'competition_id': ['IT1', 'IT1', 'IT1', 'IT1', 'IT1', 'IT1', 'IT1', 'IT1', 'IT1', 'UKR1', 'PO1', 'PO1', 'PO1', 'PO1'],
    'season': [2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023],
    'round': ['6. Matchday', '9. Matchday', '9. Matchday', '14. Matchday', '16. Matchday', '22. Matchday', '22. Matchday', '27. Matchday', '28. Matchday', '1. Matchday', '4. Matchday', '7. Matchday', '15. Matchday', '25. Matchday'],
    'date': ['2023-09-27', '2023-10-21', '2023-10-22', '2023-12-03', '2023-12-18', '2024-01-26', '2024-01-28', '2024-03-02', '2024-03-09', '2023-07-30', '2023-09-02', '2023-09-30', '2023-12-28', '2024-03-09'],
    'home_club_id': [276, 276, 12, 430, 800, 1390, 252, 2919, 252, 338, 3268, 2503, 2431, 2420],
    'away_club_id': [800, 6195, 2919, 380, 380, 416, 1005, 12, 2919, 61825, 2425, 3329, 8024, 3329],
    'home_club_goals': [0, 1, 1, 3, 4, 1, 2, 1, 2, 4, 1, 2, 1, 1],
    'away_club_goals': [1, 3, 0, 0, 1, 2, 1, 4, 3, 1, 1, 2, 4, 0],
    'home_club_position': [14, 16, 7, 6, 7, 18, 11, 11, 12, 1, 9, 4, 11, 5],
    'away_club_position': [4, 4, 11, 20, 20, 10, 14, 5, 10, 16, 11, 7, 10, 10],
    'home_club_manager_name': ['Marco Baroni', 'Marco Baroni', 'JosГ© Mourinho', 'Vincenzo Italiano', 'Gian Piero Gasperini', 'Claudio Ranieri', 'Alberto Gilardino', 'Raffaele Palladino', 'Alberto Gilardino', 'Mircea Lucescu', 'Filipe Martins', 'Petit', 'SГ©rgio Vieira', 'ГЃlvaro Pacheco'],
    'away_club_manager_name': ['Gian Piero Gasperini', 'Rudi Garcia', 'Raffaele Palladino', 'Filippo Inzaghi', 'Filippo Inzaghi', 'Ivan Juric', 'Roberto D\'Aversa', 'Daniele De Rossi', 'Raffaele Palladino', 'Volodymyr Sharan', 'LuГ­s Freire', 'JoГЈo Pedro Sousa', 'Daniel Sousa', 'JoГЈo Pedro Sousa'],
    'stadium': ['Marcantonio Bentegodi', 'Marcantonio Bentegodi', 'Olimpico di Roma', 'Artemio Franchi', 'Gewiss Stadium', 'Unipol Domus', 'Luigi Ferraris', 'U-Power Stadium - Brianteo', 'Luigi Ferraris', 'Valeriy Lobanovsky Stadion', 'EstГЎdio Nacional do Jamor', 'EstГЎdio do Bessa SГ©culo XXI', 'EstГЎdio JosГ© Gomes', 'EstГЎdio D. Afonso Henriques'],
    'attendance': [15936, 20549, 62022, 26286, 14264, 16196, 32152, 14188, None, 3267, 7809, None, 4352, None],
    'referee': ['Federico Dionisi', 'Rosario Abisso', 'Giovanni Ayroldi', 'Paride Tremolada', 'Ermanno Feliciani', 'Andrea Colombo', 'Luca Pairetto', 'Marco Piccinini', 'Ermanno Feliciani', 'Maksym Kozyryatskyi', 'David Silva', 'Gustavo Correia', 'JoГЈo Pinheiro', 'Iancu Vasilica'],
    'url': [
        'https://www.transfermarkt.co.uk/hellas-verona_atalanta-bc/index/spielbericht/4103526', 'https://www.transfermarkt.co.uk/hellas-verona_ssc-napoli/index/spielbericht/4103555', 'https://www.transfermarkt.co.uk/as-roma_ac-monza/index/spielbericht/4103557', 'https://www.transfermarkt.co.uk/acf-fiorentina_us-salernitana-1919/index/spielbericht/4103602', 'https://www.transfermarkt.co.uk/atalanta-bc_us-salernitana-1919/index/spielbericht/4103622', 'https://www.transfermarkt.co.uk/cagliari-calcio_torino-fc/index/spielbericht/4103683', 'https://www.transfermarkt.co.uk/genoa-cfc_us-lecce/index/spielbericht/4103685', 'https://www.transfermarkt.co.uk/ac-monza_as-roma/index/spielbericht/4103738', 'https://www.transfermarkt.co.uk/genoa-cfc_ac-monza/index/spielbericht/4103745', 'https://www.transfermarkt.co.uk/dynamo-kyiv_fk-minaj/index/spielbericht/4104307', 'https://www.transfermarkt.co.uk/casa-pia-ac_rio-ave-fc/index/spielbericht/4109307', 'https://www.transfermarkt.co.uk/boavista-fc_fc-famalicao/index/spielbericht/4109338', 'https://www.transfermarkt.co.uk/cf-estrela-amadora-sad_fc-arouca/index/spielbericht/4109411', 'https://www.transfermarkt.co.uk/vitoria-guimaraes-sc_fc-famalicao/index/spielbericht/4109470'
    ],
    'home_club_formation': [
        'Starting Line-up: 3-4-2-1', 'Starting Line-up: 3-5-2 flat', 'Starting Line-up: 3-5-2 flat', 'Starting Line-up: 4-2-3-1', 'Starting Line-up: 3-4-1-2', 'Starting Line-up: 3-4-2-1', 'Starting Line-up: 3-5-2 flat', 'Starting Line-up: 4-2-3-1', 'Starting Line-up: 3-5-2 flat', 'Starting Line-up: 4-2-3-1', 'Starting Line-up: 3-4-3', 'Starting Line-up: 4-3-3 Attacking', 'Starting Line-up: 3-4-2-1', 'Starting Line-up: 3-4-3'
    ],
    'away_club_formation': [
        'Starting Line-up: 3-4-2-1', 'Starting Line-up: 4-3-3 Attacking', 'Starting Line-up: 3-4-2-1', 'Starting Line-up: 3-4-2-1', 'Starting Line-up: 4-2-3-1', 'Starting Line-up: 3-4-1-2', 'Starting Line-up: 4-3-3 Attacking', 'Starting Line-up: 4-3-3 Attacking', 'Starting Line-up: 4-2-3-1', 'Starting Line-up: 5-4-1', 'Starting Line-up: 3-4-3', 'Starting Line-up: 4-4-2 double 6', 'Starting Line-up: 4-3-3 Attacking', 'Starting Line-up: 3-4-3'
    ],
    'home_club_name': [
        'Verona Hellas Football Club', 'Verona Hellas Football Club', 'Associazione Sportiva Roma', 'Associazione Calcio Fiorentina', 'Atalanta Bergamasca Calcio S.p.a.', 'Cagliari Calcio', 'Genoa Cricket and Football Club', 'Associazione Calcio Monza', 'Genoa Cricket and Football Club', 'Futbolniy Klub Dynamo Kyiv', 'Casa Pia AtlГ©tico Clube', 'Boavista Futebol Clube', 'Club Football Estrela da Amadora', 'VitГіria Sport Clube'
    ],
    'away_club_name': [
        'Atalanta Bergamasca Calcio S.p.a.', 'SocietГ  Sportiva Calcio Napoli', 'Associazione Calcio Monza', 'U.S. Salernitana 1919 S.r.l.', 'U.S. Salernitana 1919 S.r.l.', 'Torino Calcio', 'Unione Sportiva Lecce', 'Associazione Sportiva Roma', 'Associazione Calcio Monza', 'FK Minaj', 'Rio Ave Futebol Clube', 'Futebol Clube de FamalicГЈo', 'Futebol Clube de Arouca', 'Futebol Clube de FamalicГЈo'
    ],
    'aggregate': ['0:1', '1:3', '1:0', '3:0', '4:1', '1:2', '2:1', '1:4', '2:3', '4:1', '1:1', '2:2', '1:4', '1:0'],
    'competition_type': [
        'domestic_league', 'domestic_league', 'domestic_league', 'domestic_league', 'domestic_league', 'domestic_league', 'domestic_league', 'domestic_league', 'domestic_league', 'domestic_league', 'domestic_league', 'domestic_league', 'domestic_league', 'domestic_league'
    ]
}

clubs_data = {
    'club_id': data['home_club_id'] + data['away_club_id'],
    'club_name': data['home_club_name'] + data['away_club_name'],
    'club_position': data['home_club_position'] + data['away_club_position'],
    'club_manager_name': data['home_club_manager_name'] + data['away_club_manager_name'],
    'club_formation': data['home_club_formation'] + data['away_club_formation']
}

matches_data = {
    'game_id': data['game_id'],
    'competition_id': data['competition_id'],
    'season': data['season'],
    'round': data['round'],
    'date': data['date'],
    'home_club_id': data['home_club_id'],
    'away_club_id': data['away_club_id'],
    'home_club_goals': data['home_club_goals'],
    'away_club_goals': data['away_club_goals'],
    'stadium': data['stadium'],
    'attendance': data['attendance'],
    'referee': data['referee'],
    'url': data['url'],
    'aggregate': data['aggregate'],
    'competition_type': data['competition_type']
}


clubs_df = pd.DataFrame(clubs_data)
matches_df = pd.DataFrame(matches_data)


print("Таблица clubs_df:")
print(clubs_df)
print("\nТаблица matches_df:")
print(matches_df)
clubs_df.to_excel('clubs_data.xlsx', index=False)
matches_df.to_excel('matches_data.xlsx', index=False)