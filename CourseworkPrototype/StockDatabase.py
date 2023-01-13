import json

class StockDatabase():
    database = dict()
    tagIndex = dict()
    titleIndex = dict()
    dbFilePath = "stockdb.json"
    nextProductNumber = 0

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
        with open(self.dbFilePath) as file:
            dbjson = file.read()
            #parse the file
            self.database = json.loads(dbjson)
        
        #Find the next product number
        for item in self.database["items"]:
            if int(item["productNumber"]) > self.nextProductNumber:
                self.nextProductNumber = int(item["productNumber"])
        

    def WriteDatabase(self):
        jsonString = json.dumps(self.database)
        with open(self.dbFilePath, "w") as file:
            file.write(jsonString)

    def IndexDatabaseTags(self):
        #Ensure the tag index is empty
        self.tagIndex = dict()

        #Iterate through each item in stock
        for index in range(len(self.database["items"])):
            for tag in self.database["items"][index]["productTags"]:
                tag = tag.lower()
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
                tag = tag.lower()
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
        #search db for prod number
        for i in range(len(self.database["items"])):
            if self.database["items"][i]["productNumber"] == prodNum:
                item = self.database["items"][i]
        
        return item

    def GetVariation(self, itemNumber:str):
        #split product and variation numbers
        inumComponents = itemNumber.split(":")

        prodNum = inumComponents[0]
        varNum = inumComponents[1]

        #Get item
        item = self.GetItemByProductNumber(prodNum)

        variation = None

        #Find variation
        if item != None:
            for var in item["variations"]:
                if var["variationID"] == varNum:
                    variation = var
            
        return variation
        
    def CreateItem(self, prodName:str, tags:list, variations:list):
        #Create Dict Entry
        newItem = {
            "productNumber": str(self.nextProductNumber).zfill(6), #This creates a string using the next product number that's padded to length 6
            "productName": prodName,
            "productTags": tags,
            "variations": variations
        }
        self.database["items"].append(newItem) #Add new item to JSON

        self.WriteDatabase() #Store database
        
        #Rebuild Index
        self.IndexDatabaseTags()
        self.IndexDatabaseTitles()

    def UpdateItem(self, productNumber:str, editedItem:dict):
        found = False

        #Find the specified item
        for i in range(len(self.database["items"])):
            if self.database["items"][i]["productNumber"] == productNumber:
                #switch item for new version
                self.database["items"][i] = editedItem
                found = True

        #Throw error if item isn't found
        if not found:
            raise Exception(f"Unable to find product with ID {productNumber}")
        else:
            #Save and update tags
            self.WriteDatabase()
            self.IndexDatabaseTags()
            self.IndexDatabaseTitles()
