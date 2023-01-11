import json

class StockDatabase():
    database = dict()
    tagIndex = dict()
    titleIndex = dict()

    def __init__(self): #Runs when an object is made
        self.LoadFile()
        self.IndexDatabaseTags()
        self.IndexDatabaseTitles()

    def LoadFile(self):
        #Ensure all the lists are clear
        self.database = dict()
        self.tagIndex = dict()
        self.titleIndex = dict()

        #Load JSON File
        with open("CourseworkPrototype/stockdb.json") as file:
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
                if tag in self.tagIndex:
                    #Tag is already stored, add the index to the dict
                    self.tagIndex[tag.lower()].append(index)
                else:
                    self.tagIndex[tag.lower()] = [index]
        
    def IndexDatabaseTitles(self):
        #Ensure the tag index is empty
        self.titleIndex = dict()

        #Iterate through each item in stock
        for index in range(len(self.database["items"])):
            for tag in self.database["items"][index]["productName"].split(" "):
                tag = ''.join(c for c in tag if c.isalnum())
                if tag in self.titleIndex:
                    #Tag is already stored, add the index to the dict
                    self.titleIndex[tag.lower()].append(index)
                else:
                    self.titleIndex[tag.lower()] = [index]
    
    def SearchForItem(self, query:str) -> list:
        #Separate query into its separate terms
        searchTerms = query.split(" ")
        
        hits = []

        #For each search term, find matches.
        for term in searchTerms:
            
            term = (''.join(c for c in term if c.isalnum())).lower()
            #Check title index
            if term in self.tagIndex:
                #If it matches, get the indexes stored under the tag
                positions = self.tagIndex[term]
                for position in positions:
                    #Add as a hit
                    hits.append(position)

            #Check title index
            if term in self.titleIndex:
                #If it matches, get the indexes stored under the tag
                positions = self.titleIndex[term]
                for position in positions:
                    #Add as a hit
                    hits.append(position)

        #Order the values in the hits list by their popularity.
        #This takes the list, counts how many times the value appears, and reorders it using this count
        #It's reversed so the most popular items are first, and then the popularity descends
        prioritisedResults = sorted(hits, key=lambda x: hits.count(x), reverse=True)

        #Get only the unique options.
        uniqueResults = []
        for index in prioritisedResults:
            if uniqueResults.count(index) != 0: continue
            else: uniqueResults.append(index)

        print(uniqueResults)
        
        return uniqueResults

    def GetItemByProductNumber(self, prodNum:str):
        item = None

        for i in range(len(self.database["items"])):
            if self.database["items"][i]["productNumber"] == prodNum:
                item = self.database["items"][i]
        
        return item

    def GetVariation(self, itemNumber:str):
        inumComponents = itemNumber.split(":")

        prodNum = inumComponents[0]
        varNum = inumComponents[1]

        item = self.GetItemByProductNumber(prodNum)

        variation = None

        if item != None:
            for var in item["variations"]:
                if var["variationID"] == varNum:
                    variation = var
            
        return variation
        
