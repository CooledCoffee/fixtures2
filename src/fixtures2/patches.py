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
            self.addCleanup(self._safe_delete, obj, attr)
        else:
            self.addCleanup(setattr, obj, attr, old_value)
            
    def _safe_delete(self, obj, attribute):
        """Delete obj.attribute handling the case where its missing."""
        sentinel = object()
        if getattr(obj, attribute, sentinel) is not sentinel:
            delattr(obj, attribute)
            