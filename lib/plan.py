from datetime import datetime

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
