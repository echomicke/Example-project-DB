import json

class ObjectStore:
    """
    A class that allows to store and fetch data from a file in json format
    """

    file_path = ""

    def saveData(self , dict_data):
        """
        Save data to a file in json format
        :param dict_data: data to be saved in the file
        """
        jsonData = json.dumps(dict_data)

        db_file = open(self.file_path, "a")
        record = str(jsonData) + "\n"
        db_file.write(record)
        db_file.close()

    def fetchData(self):
        """
        Fetch data from a file in json format
        :return: the data stored in the file
        """
        saved_data = {}

        db_file = open(self.file_path)
        for record in db_file:
            saved_data.update(json.loads(record))
        db_file.close()

        return saved_data
