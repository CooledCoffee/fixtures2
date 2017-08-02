# -*- coding: utf-8 -*-
import sys

from six import StringIO

from fixtures2.patches import PatchesFixture

class StreamsFixture(PatchesFixture):
    @property
    def stdout(self):
        return sys.stdout.getvalue()
    
    @property
    def stderr(self):
        return sys.stderr.getvalue()
    
    def setUp(self):
        super(StreamsFixture, self).setUp()
        self.patch('sys.stdout', StringIO())
        self.patch('sys.stderr', StringIO())
        