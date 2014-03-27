# -*- coding: utf-8 -*-
from fixtures.fixture import Fixture

class StubFixture(Fixture):
    def stub(self, obj, attr, value):
        old = getattr(obj, attr)
        setattr(obj, attr, value)
        self.addCleanup(lambda: setattr(obj, attr, old))
        