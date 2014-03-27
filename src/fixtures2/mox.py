# -*- coding: utf-8 -*-
from __future__ import absolute_import
from fixtures.fixture import Fixture
try:
    import mox
    
    class MoxFixture(Fixture):
        def setUp(self):
            super(MoxFixture, self).setUp()
            self._mox = mox.Mox()
            self.addCleanup(lambda: self._mox.ResetAll())
            self.addCleanup(lambda: self._mox.UnsetStubs())
            
        def create_mock(self, cls=None):
            return self._mox.CreateMockAnything() if cls is None else self._mox.CreateMock(cls)
        
        def mock(self, obj, attr):
            self._mox.StubOutWithMock(obj, attr)
            
        def record(self):
            class _Record(object):
                def __enter__(self):
                    return self
                
                def __exit__(self, *args):
                    pass
            return _Record()
            
        def replay(self):
            _mox = self._mox
            class _Replay(object):
                def __enter__(self):
                    _mox.ReplayAll()
                    return self
                
                def __exit__(self, error_type, error_value, traceback):
                    if error_value is None:
                        _mox.VerifyAll()
            return _Replay()
except ImportError:
    pass
