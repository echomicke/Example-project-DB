import json

file_path = ""

def fetchData():
    saved_data = {}
    
    db_file = open(file_path)
    for record in db_file:
        saved_data.update(json.loads(record))
    db_file.close()

    return saved_data
