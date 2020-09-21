from datetime import datetime
import unittest
from unittest.mock import MagicMock, patch

from lib.plan import Plan
from lib.service_type import ServiceType


class TestPlan(unittest.TestCase):

    def setUp(self) -> None:
        type_by_id_patch = patch("lib.plan.ServiceType.get_by_id")
        self.m_type_by_id = type_by_id_patch.start()
        self.addCleanup(type_by_id_patch.stop)

    def test_init_minimal(self):
        """Plan.__init__.minimal"""
        start = datetime(year=2020, month=9, day=20)
        st = ServiceType("The Gathering", type_id="001")
        plan = Plan(start, st, "123")

        self.assertEqual(plan.start, datetime(year=2020, month=9, day=20))
        self.assertEqual(plan.type, st)
        self.assertEqual(plan.id, "123")
        self.assertIsNone(plan.title)

    def test_init_full(self):
        """Plan.__init__.minimal"""
        start = datetime(year=2020, month=9, day=20)
        st = ServiceType("The Gathering", type_id="001")
        plan = Plan(start, st, "123", "A service")

        self.assertEqual(plan.start, datetime(year=2020, month=9, day=20))
        self.assertEqual(plan.type, st)
        self.assertEqual(plan.id, "123")
        self.assertEqual(plan.title, "A service")

    def test_str_title(self):
        """Plan.__str__.title"""
        start = datetime(year=2020, month=9, day=20)
        st = ServiceType("The Gathering", type_id="001")
        plan = Plan(start, st, "123", title="A service")

        self.assertEqual(str(plan), "2020-09-20 00:00:00 (A service)")

    def test_str_no_title(self):
        """Plan.__str__.no_title"""
        start = datetime(year=2020, month=9, day=20)
        st = ServiceType("The Gathering", type_id="001")
        plan = Plan(start, st, "123")

        self.assertEqual(str(plan), "2020-09-20 00:00:00")

    def test_repr(self):
        """Plan.__repr__"""
        start = datetime(year=2020, month=9, day=20)
        st = ServiceType("The Gathering", type_id="001")
        plan = Plan(start, st, "123")

        self.assertEqual(repr(plan), "2020-09-20 00:00:00")

    def test_eq_equal(self):
        """Plan.__eq__.equal"""
        start = datetime(year=2020, month=9, day=20)
        st = ServiceType("The Gathering", type_id="001")
        plan1 = Plan(start, st, "123")
        plan2 = Plan(start, st, "123")

        self.assertEqual(plan1, plan2)

    def test_eq_neq(self):
        """Plan.__eq__.neq"""
        start = datetime(year=2020, month=9, day=20)
        st = ServiceType("The Gathering", type_id="001")
        plan1 = Plan(start, st, "123")
        plan2 = Plan(start, st, "456")

        self.assertNotEqual(plan1, plan2)

    def test_hash(self):
        """Plan.__hash__"""
        start = datetime(year=2020, month=9, day=20)
        st = ServiceType("The Gathering", type_id="001")
        plan = Plan(start, st, "123")

        self.assertEqual(hash(plan), hash("123"))

    def test_get_from_json(self):
        """Plan.get_from_json"""
        json = {
            "attributes": {
                "sort_date": "2020-09-20T09:30:00Z",
                "title": "A service"
            },
            "relationships": {
                "service_type": {
                    "data": {
                        "id": "001"
                    }
                }
            },
            "id": "123456"
        }

        s_type = MagicMock()
        self.m_type_by_id.return_value = s_type

        plan = Plan.get_from_json(json)

        self.m_type_by_id.assert_called_with("001")

        self.assertEqual(plan.start, datetime(year=2020, month=9, day=20, hour=9, minute=30))
        self.assertEqual(plan.type, s_type)
        self.assertEqual(plan.id, "123456")
        self.assertEqual(plan.title, "A service")


if __name__ == '__main__':
    unittest.main()
