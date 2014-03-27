# -*- coding: utf-8 -*-
from fixtures2.case import TestCase
from fixtures2.patches import PatchesFixture
import sys

class PatchesTest(TestCase):
    def setUp(self):
        super(PatchesTest, self).setUp()
        self.patches = self.useFixture(PatchesFixture())
        
    def test(self):
        self.patches.patch('sys.argv', ['a', 'b', 'c'])
        self.assertEqual(['a', 'b', 'c'], sys.argv)
        