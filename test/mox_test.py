# -*- coding: utf-8 -*-
from fixtures2.case import TestCase
try:
    from fixtures2.mox import MoxFixture
    import time
    
    class MoxTest(TestCase):
        def setUp(self):
            super(MoxTest, self).setUp()
            self.mox = self.useFixture(MoxFixture())
            
        def test_mock(self):
            self.mox.mock(time, 'time')
            with self.mox.record():
                time.time().AndReturn(111)
            with self.mox.replay():
                result = time.time()
                self.assertEqual(111, result)
                
        def test_create_mock(self):
            mock = self.mox.create_mock()
            with self.mox.record():
                mock.foo().AndReturn('foo')
            with self.mox.replay():
                result = mock.foo()
                self.assertEqual('foo', result)
except ImportError:
    pass
