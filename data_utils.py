import re


def sanitize_map_name(string):
    regex = re.compile('[^a-zA-Z]')
    return regex.sub('', string)


def rectify_team_data(team_loadouts, team_a, team_b):
    for map_round in team_loadouts:
        print(map_round)
        print(team_loadouts.get(map_round))
    return []
