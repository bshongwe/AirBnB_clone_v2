#!/usr/bin/python3
"""Unittests for models/city.py"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import pycodestyle


class test_City(test_basemodel):
    """Unittests for testing instantiation of the City class"""

    def __init__(self, *args, **kwargs):
        """Initialise object state"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Test object for string"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Test name for string"""
        new = self.value()
        self.assertEqual(type(new.name), str)


class Test_PEP8(unittest.TestCase):
    """Test User"""

    def test_pep8_user(self):
        """Test PEP8 style"""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestCity(unittest.TestCase):
    """This will test the city class X"""

    @classmethod
    def setUpClass(cls):
        """Set up for test"""
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def teardown(cls):
        """At the end of the test this will tear it down"""
        del cls.city

    def tearDown(self):
        """Teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_City(self):
        """Tests PEP8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_City(self):
        """Checking for Docstrings"""
        self.assertIsNotNone(City.__doc__)

    def test_attributes_City(self):
        """Chekcing if City has attributes"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_is_subclass_City(self):
        """Test if City is subclass of Basemodel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attribute_types_City(self):
        """Test attribute type for City"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_save_City(self):
        """Test if the save works"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_City(self):
        """Test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
