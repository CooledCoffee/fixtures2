# -*- coding: utf-8 -*-
from fixtures.testcase import TestWithFixtures

class TestCase(TestWithFixtures):
    def assertBetween(self, value, lower_bound, upper_bound, inclusive=True):
        if inclusive:
            success = value >= lower_bound and value <= upper_bound
        else:
            success = value > lower_bound and value < upper_bound
        if not success:
            msg = 'Value "%s" is not between "%s" and "%s".' % (value, lower_bound, upper_bound)
            raise self.failureException(msg)
    
    def useFixture(self, fixture):
        super(TestCase, self).useFixture(fixture)
        return fixture
    