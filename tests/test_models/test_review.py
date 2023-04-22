#!/usr/bin/python3
"""Unit tests for Review class"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Review class tester"""

    def __init__(self, *args, **kwargs):
        """Initialize review model """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """test it has place id and it is string """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """test user ID is of type string """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """test review has text and text is string type"""
        new = self.value()
        self.assertEqual(type(new.text), str)
