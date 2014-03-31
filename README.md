Introduction
============

Fixtures2 is an extension of the fixtures test framework.

Installation
============

pip install fixtures2

Examples
========

Patches
-------

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
	        
Streams
-------

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
	        
Date & DateTime
---------------

	from datetime import date, datetime
	from fixtures2.case import TestCase
	from fixtures2.datetime import DateTimeFixture, DateFixture
	
	def date_today():
	    return date.today()
	
	def datetime_now():
	    return datetime.now()
	
	def datetime_today():
	    return datetime.today()
	
	class DateTest(TestCase):
	    def setUp(self):
	        super(DateTest, self).setUp()
	        self.useFixture(DateFixture('datetime_test.date', date(2000, 1, 1)))
	        
	    def test(self):
	        result = date_today()
	        self.assertEqual(date(2000, 1, 1), result)
	
	class DateTimeTest(TestCase):
	    def setUp(self):
	        super(DateTimeTest, self).setUp()
	        self.useFixture(DateTimeFixture('datetime_test.datetime', datetime(2000, 1, 1, 12, 0, 0)))
	        
	    def test_now(self):
	        result = datetime_now()
	        self.assertEqual(datetime(2000, 1, 1, 12, 0, 0), result)
	        
	    def test_today(self):
	        result = datetime_today()
	        self.assertEqual(date(2000, 1, 1), result)
        
Mox
---

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

Author
======

Mengchen LEE: <a href="https://plus.google.com/117704742936410336204" target="_blank">Google Plus</a>, <a href="https://cn.linkedin.com/pub/mengchen-lee/30/8/23a" target="_blank">LinkedIn</a>
