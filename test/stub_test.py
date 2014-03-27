# -*- coding: utf-8 -*-
from fixtures2.case import TestCase
from fixtures2.stub import StubFixture
import sys

class StubTest(TestCase):
    def setUp(self):
        super(StubTest, self).setUp()
        self.stub = self.useFixture(StubFixture())
        
    def test(self):
        self.stub.stub(sys, 'argv', ['a', 'b', 'c'])
        self.assertEqual(['a', 'b', 'c'], sys.argv)
        