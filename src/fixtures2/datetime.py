# -*- coding: utf-8 -*-
from __future__ import absolute_import
from datetime import date, datetime
from fixtures._fixtures.monkeypatch import MonkeyPatch

class DateFixture(MonkeyPatch):
    def __init__(self, path, today):
        class FixedDateTime(date):
            @staticmethod
            def today():
                return today
        super(DateFixture, self).__init__(path, FixedDateTime)

class DateTimeFixture(MonkeyPatch):
    def __init__(self, path, now):
        class FixedDateTime(datetime):
            @staticmethod
            def now():
                return now
            
            @staticmethod
            def today():
                return now.date()
        super(DateTimeFixture, self).__init__(path, FixedDateTime)
