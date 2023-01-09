import json
class StockDatabase():
    database = dict()
    tagIndex = dict()
    titleIndex = dict()

    def __init__(self):
        #Load the json file as a string
        with open("stockdb.json") as file:
            dbjson = file.read()
            #parse the file
            self.database = json.loads(dbjson)