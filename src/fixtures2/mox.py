# -*- coding: utf-8 -*-
from __future__ import absolute_import
from fixtures.fixture import Fixture
try:
    from mox import Comparator
    import mox
    
    class MoxFixture(Fixture):
        def setUp(self):
            super(MoxFixture, self).setUp()
            self._mox = mox.Mox()
            self.addCleanup(lambda: self._mox.ResetAll())
            self.addCleanup(lambda: self._mox.UnsetStubs())
            
        def create_mock(self, cls=None):
            return self._mox.CreateMockAnything() if cls is None else self._mox.CreateMock(cls)
        
        def mock(self, path):
            obj, attr = _split(path)
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
        
    class StoreArg(Comparator):
        '''
        >>> arg = StoreArg()
        >>> arg.equals(1)
        True
        >>> arg.get()
        1
        '''
        def __init__(self):
            self._arg = None
            
        def equals(self, rhs):
            self._arg = rhs
            return True
        
        def get(self):
            return self._arg
        
    def _split(path):
        location, attr = path.rsplit('.', 1)
        try:
            __import__(location, {}, {})
        except ImportError:
            pass
        components = location.split('.')
        current = __import__(components[0], {}, {})
        for component in components[1:]:
            current = getattr(current, component)
        return current, attr
        
except ImportError:
    pass
