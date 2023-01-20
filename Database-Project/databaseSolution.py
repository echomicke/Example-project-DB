import json

class ObjectStore:    
    file_path = ""

    def saveData(self , dict_data):
        jsonData = json.dumps(dict_data)

        db_file = open(self.file_path, "a")
        record = str(jsonData) + "\n"
        db_file.write(record)
        db_file.close()


    def fetchData(self):
        saved_data = {}

        db_file = open(self.file_path)
        for record in db_file:
            saved_data.update(json.loads(record))
        db_file.close()

        return saved_data 
