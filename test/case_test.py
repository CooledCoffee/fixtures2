# -*- coding: utf-8 -*-
from fixtures2.case import TestCase

class AssertBetweenTest(TestCase):
    def test_basic(self):
        self.assertBetween(5, 0, 10)
        with self.assertRaises(AssertionError):
            self.assertBetween(15, 0, 10)
            
    def test_inclusive(self):
        self.assertBetween(0, 0, 10)
        self.assertBetween(10, 0, 10)
            
    def test_exclusive(self):
        with self.assertRaises(AssertionError):
            self.assertBetween(0, 0, 10, inclusive=False)
        with self.assertRaises(AssertionError):
            self.assertBetween(10, 0, 10, inclusive=False)
            