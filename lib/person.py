from lib.planning_center import PlanningCenter


class Person:
    """
    Class representation of a Person in Planning Center
    """

    def __init__(self, person_id: int, name: str):
        self.name = name
        self.id = person_id

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{self.name} {self.id}'

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    @staticmethod
    def get_from_json(json: dict):
        person_id = json["id"]
        name = json["attributes"]["full_name"]

        return Person(person_id, name)

    @staticmethod
    def get_all(page=0, per_page=100):
        """Get all people in Planning Center"""
        people = []
        offset = page * per_page
        people_json = PlanningCenter.PCO.get(f"/services/v2/people?per_page={per_page}&offset={offset}")["data"]

        for person_json in people_json:
            people.append(Person.get_from_json(person_json))

        if len(people) == per_page:
            # Might be more - paginate!
            people += Person.get_all(page+1, per_page=per_page)

        return people
