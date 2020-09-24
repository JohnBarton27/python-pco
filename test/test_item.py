from datetime import timedelta
import unittest

from lib.item import Item


class TestItem(unittest.TestCase):

    def test_init(self):
        """Item.__init__"""
        item = Item("A Song", "song", "123456", timedelta(minutes=2))

        self.assertEqual(item.title, "A Song")
        self.assertEqual(item.type, "song")
        self.assertEqual(item.id, "123456")
        self.assertEqual(item.length, timedelta(minutes=2))

    def test_str(self):
        """Item.__str__"""
        item = Item("A Song", "song", "123456", timedelta(minutes=2))

        self.assertEqual(str(item), "[song] A Song (0:02:00)")

    def test_repr(self):
        """Item.__repr__"""
        item = Item("A Song", "song", "123456", timedelta(minutes=2))

        self.assertEqual(repr(item), "[song] A Song (0:02:00)")

    def test_eq_equal(self):
        """Item.__eq__.equal"""
        item1 = Item("A Song", "song", "123456", timedelta(minutes=2))
        item2 = Item("A Song", "song", "123456", timedelta(minutes=2))

        self.assertEqual(item1, item2)

    def test_eq_neq(self):
        """Item.__eq__.neq"""
        item1 = Item("A Song", "song", "123456", timedelta(minutes=2))
        item2 = Item("A Song", "song", "654321", timedelta(minutes=2))

        self.assertNotEqual(item1, item2)

    def test_hash(self):
        """Item.__hash__"""
        item = Item("A Song", "song", "123456", timedelta(minutes=2))

        self.assertEqual(hash(item), hash("123456"))

    def test_get_from_json(self):
        """Item.get_from_json"""
        json = {
            "attributes": {
                "title": "A sermon",
                "item_type": "item",
                "length": 120
            },
            "id": "123456"
        }

        item = Item.get_from_json(json)

        self.assertEqual(item.title, "A sermon")
        self.assertEqual(item.type, "item")
        self.assertEqual(item.length, timedelta(minutes=2))
        self.assertEqual(item.id, "123456")


if __name__ == '__main__':
    unittest.main()
