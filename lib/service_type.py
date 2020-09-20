from lib.planning_center import PlanningCenter


class ServiceType:

    def __init__(self, name: str, type_id: str = None, frequency: str = None):
        self.name = name
        self._id = type_id
        self.frequency = frequency

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.id == other.id

    @property
    def id(self):
        if self._id:
            return self._id

        full_type = ServiceType.get_by_name(self.name)
        self._id = full_type.id
        return self._id

    @staticmethod
    def get_by_name(name: str):
        all_types = ServiceType.get_all()
        for service_type in all_types:
            if service_type.name == name:
                return service_type

        return None

    @staticmethod
    def get_all():
        output = PlanningCenter.PCO.get('/services/v2/service_types')
        type_jsons = output["data"]
        types = []

        for type_json in type_jsons:
            types.append(ServiceType.get_from_json(type_json))

        return types

    @staticmethod
    def get_from_json(json: dict):
        type_id = json["id"]
        name = json["attributes"]["name"]
        frequency = json["attributes"]["frequency"]

        return ServiceType(name, type_id=type_id, frequency=frequency)
