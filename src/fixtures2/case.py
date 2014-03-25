# -*- coding: utf-8 -*-
from fixtures.testcase import TestWithFixtures

class TestCase(TestWithFixtures):
    def useFixture(self, fixture):
        super(TestCase, self).useFixture(fixture)
        return fixture
    