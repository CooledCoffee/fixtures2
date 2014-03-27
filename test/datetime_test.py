# -*- coding: utf-8 -*-
from datetime import date, datetime
from fixtures2.case import TestCase
from fixtures2.datetime import DateTimeFixture, DateFixture

def date_today():
    return date.today()

def datetime_now():
    return datetime.now()

def datetime_today():
    return datetime.today()

class DateFixtureTest(TestCase):
    def setUp(self):
        super(DateFixtureTest, self).setUp()
        self.useFixture(DateFixture('datetime_test.date', date(2000, 1, 1)))
        
    def test(self):
        result = date_today()
        self.assertEqual(date(2000, 1, 1), result)

class DateTimeFixtureTest(TestCase):
    def setUp(self):
        super(DateTimeFixtureTest, self).setUp()
        self.useFixture(DateTimeFixture('datetime_test.datetime', datetime(2000, 1, 1, 12, 0, 0)))
        
    def test_now(self):
        result = datetime_now()
        self.assertEqual(datetime(2000, 1, 1, 12, 0, 0), result)
        
    def test_today(self):
        result = datetime_today()
        self.assertEqual(date(2000, 1, 1), result)
        