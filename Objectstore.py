
import unittest
import os
import json
from DBSolution import ObjectStore 

class ObjectStoreTestCase(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_file.json"
        self.obj = ObjectStore(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_init(self):
        self.assertEqual(self.obj.__file_path, self.test_file)
        self.assertEqual(self.obj.__records, {})

    def test_fetchAllData(self):
        with open(self.test_file, "w") as f:
            f.write('{"key1": "value1", "key2": "value2"}')

        self.obj._fetchAllData()
        self.assertEqual(self.obj.__records, {"key1": "value1", "key2": "value2"})

    def test_viewSavedRecords(self):
        self.obj.__records = {"key1": "value1", "key2": "value2"}
        self.assertEqual(self.obj.viewSavedRecords(), None)

    def test_AddRecord(self):
        self.obj.AddRecord("key1", "value1")
        self.assertEqual(self.obj.__records, {"key1": "value1"})

    def test_AddDict(self):
        self.obj.AddDict({"key1": "value1", "key2": "value2"})
        self.assertEqual(self.obj.__records, {"key1": "value1", "key2": "value2"})

    def test_searchValue(self):
        self.obj.__records = {"key1": "value1", "key2": "value2"}
        self.assertEqual(self.obj.searchValue("key1"), "value1")
        self.assertEqual(self.obj.searchValue("key3"), None)

    def test_saveDataToFile(self):
        self.obj.__records = {"key1": "value1", "key2": "value2"}
        self.obj.saveDataToFile()

        with open(self.test_file, "r") as f:
            data = f.read()
        self.assertEqual(json.loads(data), {"key1": "value1", "key2": "value2"})

if __name__ == '__main__':
    unittest.main()

