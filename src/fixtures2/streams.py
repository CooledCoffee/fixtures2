# -*- coding: utf-8 -*-
from fixtures2.patches import PatchesFixture
import sys
try:
    from StringIO import StringIO  # @UnusedImport
except:
    from io import StringIO  # @Reimport

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
        