import unittest

from lib.service_type import ServiceType


class TestServiceType(unittest.TestCase):

    def test_init_minimal(self):
        """ServiceType.__init__.minimal"""
        st = ServiceType("Traditional")

        self.assertEqual(st.name, "Traditional")
        self.assertIsNone(st._id)
        self.assertIsNone(st.frequency)

    def test_init_full(self):
        """ServiceType.__init__.full"""
        st = ServiceType("Traditional", type_id="123456", frequency="Weekly")

        self.assertEqual(st.name, "Traditional")
        self.assertEqual(st._id, "123456")
        self.assertEqual(st.frequency, "Weekly")

    def test_str(self):
        """ServiceType.__str__"""
        st = ServiceType("Traditional")

        self.assertEqual(str(st), "Traditional")

    def test_repr(self):
        """ServiceType.__repr__"""
        st = ServiceType("Traditional")

        self.assertEqual(repr(st), "Traditional")

    def test_eq_equal(self):
        """ServiceType.__eq__.equal"""
        st1 = ServiceType("Traditional", type_id="12345")
        st2 = ServiceType("Traditional", type_id="12345")

        self.assertEqual(st1, st2)

    def test_eq_neq(self):
        """ServiceType.__eq__.neq"""
        st1 = ServiceType("Traditional", type_id="12345")
        st2 = ServiceType("Traditional", type_id="54321")

        self.assertNotEqual(st1, st2)


if __name__ == '__main__':
    unittest.main()
