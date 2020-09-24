from datetime import timedelta


class Item:

    def __init__(self, title: str, item_type: str, item_id: str, length: timedelta):
        self.title = title
        self.type = item_type
        self.id = item_id
        self.length = length

    def __str__(self):
        return "[{}] {} ({})".format(self.type, self.title, self.length)

    def __repr__(self):
        return "[{}] {} ({})".format(self.type, self.title, self.length)

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    @staticmethod
    def get_from_json(json: dict):
        title = json["attributes"]["title"]
        item_type = json["attributes"]["item_type"]
        item_id = json["id"]
        length_seconds = json["attributes"]["length"]

        return Item(title, item_type, item_id, timedelta(seconds=length_seconds))
