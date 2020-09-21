from datetime import datetime
import unittest

from lib.plan import Plan
from lib.service_type import ServiceType


class TestPlan(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
