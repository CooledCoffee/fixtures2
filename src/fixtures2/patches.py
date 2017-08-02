# -*- coding: utf-8 -*-
from fixtures._fixtures.monkeypatch import MonkeyPatch
from fixtures.fixture import Fixture

class PatchesFixture(Fixture):
    def patch(self, path, value):
        self.useFixture(MonkeyPatch(path, new_value=value))
        
    def patch_object(self, obj, attr, value):
        sentinel = object()
        old_value = getattr(obj, attr, sentinel)
        if value is MonkeyPatch.delete:
            if old_value is not sentinel:
                delattr(obj, attr)
        else:
            setattr(obj, attr, value)
        if old_value is sentinel:
            self.addCleanup(_safe_delete, obj, attr)
        else:
            self.addCleanup(setattr, obj, attr, old_value)
            
def _safe_delete(obj, attr):
    if hasattr(obj, attr):
        delattr(obj, attr)
