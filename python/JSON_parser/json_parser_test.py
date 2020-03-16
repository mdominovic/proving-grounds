import unittest
import json_parser
import json
import os

class JsonParserTest(unittest.TestCase):

    def get_json_file(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_location = os.path.join(current_dir, 'sorted_comp_notcomp.json')
        with open(file_location, 'r') as f:
            json_file = json.load(f)

        return json_file

    def test_parse_json_equal(self):
        json_file = self.get_json_file()

        result = json_parser.parse_json()
        self.assertEqual(result, json.dumps(json_file))

    def test_parse_json_is_instance(self):
        json_file = self.get_json_file()

        result = json_parser.parse_json()
        self.assertIsInstance(result, str)

    def test_parse_json_is_not_none(self):
        json_file = self.get_json_file()

        result = json_parser.parse_json()
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
