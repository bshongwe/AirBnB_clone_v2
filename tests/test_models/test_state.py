#!/usr/bin/python3
"""Unittests for models/state.py"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Unittests for testing instantiation of the State class"""

    def __init__(self, *args, **kwargs):
        """Initialise object state"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Test name3 for string"""
        new = self.value()
        self.assertEqual(type(new.name), str)
