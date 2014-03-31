# -*- coding: UTF-8 -*-
from fixtures2.case import TestCase
from fixtures2.datetime import DateFixture, DateTimeFixture
from fixtures2.patches import PatchesFixture
from fixtures2.streams import StreamsFixture

TestCase = TestCase
DateFixture = DateFixture
DateTimeFixture = DateTimeFixture
PatchesFixture = PatchesFixture
StreamsFixture = StreamsFixture

try:
    from fixtures2.mox import MoxFixture
    MoxFixture = MoxFixture
except ImportError:
    pass
