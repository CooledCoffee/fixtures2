# -*- coding: utf-8 -*-
from fixtures2.case import TestCase
try:
    from fixtures2.mox import MoxFixture, StoreArg
    import os
    
    class MoxTest(TestCase):
        def setUp(self):
            super(MoxTest, self).setUp()
            self.mox = self.useFixture(MoxFixture())
            
        def test_mock(self):
            self.mox.mock('os.path.exists')
            with self.mox.record():
                os.path.exists('/tmp/abc').AndReturn(True)
            with self.mox.replay():
                result = os.path.exists('/tmp/abc')
                self.assertTrue(result)
                
        def test_create_mock(self):
            mock = self.mox.create_mock()
            with self.mox.record():
                mock.foo().AndReturn('foo')
            with self.mox.replay():
                result = mock.foo()
                self.assertEqual('foo', result)
                
        def test_store_arg(self):
            self.mox.mock('os.path.exists')
            arg = StoreArg()
            with self.mox.record():
                os.path.exists(arg).AndReturn(True)
            with self.mox.replay():
                os.path.exists('/tmp/abc')
                self.assertEqual('/tmp/abc', arg.get())
except ImportError:
    pass
