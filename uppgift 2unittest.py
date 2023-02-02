





import unittest
import json
from Objectstore import ObjectStore


class ObjectStoreTestCase(unittest.TestCase):
    def setUp(self):
        self.file_path = "test.json"
        self.obj = ObjectStore(self.file_path)

    def test_add_record(self):
        self.obj.AddRecord("name", "John")
        self.assertEqual(self.obj.searchValue("name"), "John")
    
    def test_add_dict(self):
        dict_data = {"age": 30, "city": "New York"}
        self.obj.AddDict(dict_data)
        self.assertEqual(self.obj.searchValue("age"), 30)
        self.assertEqual(self.obj.searchValue("city"), "New York")
    
    def test_search_value(self):
        self.assertIsNone(self.obj.searchValue("not_exist"))
    
    def test_view_saved_records(self):
        self.obj.viewSavedRecords()
    
    def test_save_data_to_file(self):
        self.obj.saveDataToFile()
        with open(self.file_path, "r") as f:
            data = json.load(f)
            self.assertDictEqual(data, self.obj.__records)

if __name__ == "__main__":
    unittest.main()
