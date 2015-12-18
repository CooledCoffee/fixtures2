# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from fixtures2.case import TestCase
import time

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
            
class AssertAlmostNowTest(TestCase):
    def test_datetime(self):
        self.assertAlmostNow(datetime.now() - timedelta(seconds=5))
        self.assertAlmostNow(datetime.now() + timedelta(seconds=5))
        with self.assertRaises(AssertionError):
            self.assertAlmostNow(datetime.now() - timedelta(seconds=20))
        with self.assertRaises(AssertionError):
            self.assertAlmostNow(datetime.now() + timedelta(seconds=20))
        
    def test_number(self):
        self.assertAlmostNow(time.time() - 5)
        self.assertAlmostNow(time.time() + 5)
        with self.assertRaises(AssertionError):
            self.assertAlmostNow(time.time() - 20)
        with self.assertRaises(AssertionError):
            self.assertAlmostNow(time.time() + 20)
            
    def test_delta(self):
        self.assertAlmostNow(datetime.now() - timedelta(seconds=20), delta=timedelta(seconds=30))
        self.assertAlmostNow(datetime.now() - timedelta(seconds=20), delta=30)
        