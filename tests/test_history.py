import unittest
import os
import json


class TestHistory(unittest.TestCase):
    def test_file_exists(self):
        self.assertTrue(os.path.isfile(os.path.expanduser('~') + "/.alpsh/alpsh_history.json"))

    def test_validate_clean_json(self):
        with open(os.path.expanduser('~') + "/.alpsh/alpsh_history.json") as file:
            json_object = json.load(file)
            self.assertEqual(json_object, {'history': []})


if __name__ == '__main__':
    unittest.main()
