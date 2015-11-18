# -*- coding: utf-8 -*-
from fixtures2.case import TestCase
from fixtures2.patches import PatchesFixture

class Foo(object):
    def __init__(self):
        self.a = 1
foo = Foo()

class PatchTest(TestCase):
    def test(self):
        patches = self.useFixture(PatchesFixture())
        patches.patch('patches_test.foo.a', 2)
        self.assertEqual(2, foo.a)
        
class PatchObjectTest(TestCase):
    def test(self):
        patches = self.useFixture(PatchesFixture())
        patches.patch_object(foo, 'a', 2)
        self.assertEqual(2, foo.a)
        