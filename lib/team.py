from lib.planning_center import PlanningCenter


class Team:

    def __init__(self, name: str, team_id: str):
        self.name = name
        self.id = team_id

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{self.name} ({self.id})'

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    @staticmethod
    def get_from_json(json: dict):
        name = json['attributes']['name']
        team_id = json['id']

        return Team(name, team_id)

    @staticmethod
    def get_all():
        teams = []
        teams_json = PlanningCenter.PCO.get('/services/v2/teams')['data']

        for team_json in teams_json:
            teams.append(Team.get_from_json(team_json))

        return teams
