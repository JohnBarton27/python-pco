class TeamMember:

    def __init__(self, name: str, status: str, position: str):
        self.name = name
        self.status = status
        self.position = position

    def __str__(self):
        return f'{self.name} ({self.position}) | {self.status}'

    def __repr__(self):
        return str(self)

    @staticmethod
    def get_from_json(json: dict):
        name = json['attributes']['name']
        status = json['attributes']['status']
        position = json['attributes']['team_position_name']

        return TeamMember(name, status, position)
