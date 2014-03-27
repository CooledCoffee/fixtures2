# -*- coding: utf-8 -*-
from fixtures2.case import TestCase
from fixtures2.streams import StreamsFixture
import sys

class StreamsTest(TestCase):
    def setUp(self):
        super(StreamsTest, self).setUp()
        self.streams = self.useFixture(StreamsFixture())
        
    def test(self):
        print('aaa')
        sys.stderr.write('bbb\n')
        self.assertEqual('aaa\n', self.streams.stdout)
        self.assertEqual('bbb\n', self.streams.stderr)
        