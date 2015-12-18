# -*- coding: utf-8 -*-
from __future__ import absolute_import
from datetime import datetime, timedelta
from fixtures.testcase import TestWithFixtures

class TestCase(TestWithFixtures):
    def assertAlmostNow(self, time, delta=timedelta(seconds=10)):
        if isinstance(time, (int, float)):
            time = datetime.fromtimestamp(time)
        if isinstance(delta, (int, float)):
            delta = timedelta(seconds=delta)
        if abs(datetime.now() - time) > delta:
            msg = '"%s" is not almost now' % (time.strftime('%Y-%m-%d %H:%M:%S'))
            raise self.failureException(msg)
        
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
    