from datetime import datetime

from lib.item import Item
from lib.planning_center import PlanningCenter
from lib.service_type import ServiceType


class Plan:

    def __init__(self, start: datetime,
                 plan_type: ServiceType,
                 plan_id: str,
                 title: str = None):
        self.start = start
        self.type = plan_type
        self.id = plan_id
        self.title = title

    def __str__(self):
        if self.title:
            return "{} ({})".format(self.start, self.title)
        else:
            return "{}".format(self.start)

    def __repr__(self):
        return "{}".format(self.start)

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def get_items(self):
        items_json = PlanningCenter.PCO.get("/services/v2/service_types/{}/plans/{}/items".format(self.type.id, self.id))
        items = []
        for item_json in items_json["data"]:
            items.append(Item.get_from_json(item_json))

        return items

    @staticmethod
    def get_from_json(json: dict):
        start_str = json["attributes"]["sort_date"]
        start = datetime.strptime(start_str, "%Y-%m-%dT%H:%M:%SZ")

        service_type_id = json["relationships"]["service_type"]["data"]["id"]
        service_type = ServiceType.get_by_id(service_type_id)

        plan_id = json["id"]
        title = json["attributes"]["title"]

        return Plan(start, service_type, plan_id, title=title)
