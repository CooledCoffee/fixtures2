# -*- coding: utf-8 -*-
from fixtures2.stub import StubFixture
import sys
try:
    from StringIO import StringIO  # @UnusedImport
except:
    from io import StringIO  # @Reimport

class StreamsFixture(StubFixture):
    @property
    def stdout(self):
        return sys.stdout.getvalue()
    
    @property
    def stderr(self):
        return sys.stderr.getvalue()
    
    def setUp(self):
        super(StreamsFixture, self).setUp()
        self.stub(sys, 'stdout', StringIO())
        self.stub(sys, 'stderr', StringIO())
        