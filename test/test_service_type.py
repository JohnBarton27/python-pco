import unittest
from unittest.mock import MagicMock, patch

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

    def test_hash(self):
        """ServiceType.__hash__"""
        st = ServiceType("Traditional", type_id="12345")

        self.assertEqual(hash(st), hash("12345"))

    @patch("lib.service_type.ServiceType.get_by_name")
    def test_id_populated(self, m_get_by_name):
        """ServiceType.id.populated"""
        st = ServiceType("Traditional", type_id="12345")

        self.assertEqual(st.id, "12345")
        m_get_by_name.assert_not_called()

    @patch("lib.service_type.ServiceType.get_by_name")
    def test_id_unpopulated(self, m_get_by_name):
        """ServiceType.id.unpopulated"""
        st = ServiceType("Traditional")
        st_from_rest = MagicMock()
        st_from_rest._id = "12345"

        m_get_by_name.return_value = st_from_rest

        self.assertEqual(st.id, "12345")
        m_get_by_name.assert_called_with("Traditional")

    @patch("lib.service_type.ServiceType.get_all")
    def test_get_by_name_found(self, m_get_all):
        """ServiceType.get_by_name.found"""
        st1 = ServiceType("Traditional", type_id="001")
        st2 = ServiceType("Gathering", type_id="002")
        st3 = ServiceType("Special Event", type_id="003")

        m_get_all.return_value = [st1, st2, st3]

        st = ServiceType.get_by_name("Gathering")
        self.assertEqual(st, st2)

    @patch("lib.service_type.ServiceType.get_all")
    def test_get_by_name_not_found(self, m_get_all):
        """ServiceType.get_by_name.not_found"""
        st1 = ServiceType("Traditional", type_id="001")
        st2 = ServiceType("Gathering", type_id="002")
        st3 = ServiceType("Special Event", type_id="003")

        m_get_all.return_value = [st1, st2, st3]

        st = ServiceType.get_by_name("Other")
        self.assertIsNone(st)


if __name__ == '__main__':
    unittest.main()
