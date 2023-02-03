from datetime import datetime

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

    def __hash__(self):
        return hash(self.id)

    @property
    def id(self):
        if self._id:
            return self._id

        full_type = ServiceType.get_by_name(self.name)
        self._id = full_type._id
        return self._id

    def get_next_plan(self):
        from lib.plan import Plan
        now = datetime.now()
        from datetime import timedelta
        now = now - timedelta(days=1)

        prev_plan = None
        plans = PlanningCenter.PCO.iterate(
            "/services/v2/service_types/{}/plans?order=-sort_date".format(self.id))
        while True:
            plan = Plan.get_from_json(next(plans)["data"])
            if plan.start < now:
                return prev_plan

            prev_plan = plan

    @staticmethod
    def get_by_id(type_id: str):
        all_types = ServiceType.get_all()
        for service_type in all_types:
            if service_type.id == type_id:
                return service_type

        return None

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
