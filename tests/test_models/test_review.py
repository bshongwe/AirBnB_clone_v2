#!/usr/bin/python3
"""Unittests for models/review.py"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Unittests for testing instantiation of the Review class"""

    def __init__(self, *args, **kwargs):
        """Initialise object state"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Test place_id for string"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """Test user_id for string"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Test text for string"""
        new = self.value()
        self.assertEqual(type(new.text), str)
