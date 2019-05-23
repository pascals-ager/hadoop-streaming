import io
import unittest
import unittest.mock as mock
from mapreduce import Mapper


class MapperTest(unittest.TestCase):
    def setUp(self):
        mock_file = io.StringIO('foo\tbar\nfoo\tbaz\n')
        self.separator = "\t"
        self.mapper = Mapper(self.separator, mock_file)
        self.expected = io.StringIO('foo\tbar\nbar\tfoo\nfoo\tbaz\nbaz\tfoo\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_map_task(self, mock_stdout):
        self.mapper.map_task()
        self.assertEqual(mock_stdout.getvalue(), self.expected.getvalue())

    def tearDown(self):
        self.mapper = None