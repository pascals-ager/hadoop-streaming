import io
import unittest
import unittest.mock as mock
from mapreduce import Reducer


class MapperTest(unittest.TestCase):
    def setUp(self):
        mock_file = io.StringIO('foo\tbar\nfoo\tbaz\tfizz\n')
        self.separator = "\t"
        self.reducer = Reducer(self.separator, mock_file)
        self.expected = io.StringIO('foo\tbar\tbaz\tfizz\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_reducer_task(self, mock_stdout):
        self.reducer.reduce_task()
        self.assertEqual(mock_stdout.getvalue(), self.expected.getvalue())

    def tearDown(self):
        self.reducer = None