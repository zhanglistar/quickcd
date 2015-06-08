import unittest
from monitor import MonitorDirectory
from collections import defaultdict


class MonitorDicectoryTest(unittest.TestCase):

    def test_add_single_dir(self):
        empty_dict = defaultdict(set)
        monitor = MonitorDirectory(empty_dict)


if __name__ == '__main__':
    unittest.main()