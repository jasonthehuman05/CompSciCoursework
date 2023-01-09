import json
class StockDatabase():
    database = dict()
    tagIndex = dict()
    titleIndex = dict()

    def __init__(self): #Runs when an object is made
        self.LoadFile()

    def LoadFile(self):
        #Ensure all the lists are clear
        self.database = dict()
        self.tagIndex = dict()
        self.titleIndex = dict()

        #Load JSON File
        with open("stockdb.json") as file:
            dbjson = file.read()
            #parse the file
            self.database = json.loads(dbjson)

    def IndexDatabaseTags(self):
        #Ensure the tag index is empty
        self.tagIndex = dict()

        #Iterate through each item in stock
        for index in range(len(self.database["items"])):
            for tag in self.database["items"][index]["productTags"]:
                #TODO: CHECK TAGS, ADD INDEX