# -*- coding: utf-8 -*-
from decorated.base.dict import Dict
from fixtures2.case import TestCase
from fixtures2.patches import PatchesFixture

foo = Dict(a=1)

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
        