# -*- coding: utf-8 -*-
from fixtures2 import fixutil
from fixtures2.case import TestCase

class GenerateRaiseFuncTest(TestCase):
    def test(self):
        func = fixutil.generate_raise_func(NotImplementedError())
        with self.assertRaises(NotImplementedError):
            func(1, b=2)
            