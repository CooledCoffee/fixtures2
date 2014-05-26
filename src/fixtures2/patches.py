# -*- coding: utf-8 -*-
from fixtures._fixtures.monkeypatch import MonkeyPatch
from fixtures.fixture import Fixture

class PatchesFixture(Fixture):
    def patch(self, path, value=None):
        self.useFixture(MonkeyPatch(path, new_value=value))
        