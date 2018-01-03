import unittest
from alpsh import shell


class TestInit(unittest.TestCase):
    def test_init(self):
        shell.init()


if __name__ == '__main__':
    unittest.main()
