import json

class BasketDatabase:
    def __init__(self):
        #Vars for operation
        self.FILEPATH = "basket.json"
        self.database = dict()
        self.nextId = 0

        self.LoadDatabase()

    def SaveDatabase(self):
        with open(self.FILEPATH, "w+") as file:
            jsonstring = json.dumps(self.database)
            file.write(jsonstring)


    def LoadDatabase(self):
        with open(self.FILEPATH, "r") as file:
            self.database = json.loads(file.read())

    def AddToBasket(self, customerID:str, productIDWithVariation:str):
        #Check if the basket exists
        keys = list(self.database.keys())
        #If it exists, add item
        print(self.database.keys())
        if customerID in keys:
            #Check if this variation is already an item in the customers' basket
            done = False
            for i in range(0, len(self.database[customerID])):
                if self.database[customerID][i]["ProductID"] == productIDWithVariation:
                    self.database[customerID][i]["Count"] += 1
                    done = True
                    break
            if not done:
                self.database[customerID].append({
                "ProductID": productIDWithVariation,
                "Count": 1
            })
        #if it doesn't exist, create basket for customer and add
        else:
            self.database[customerID] = [{
                "ProductID": productIDWithVariation,
                "Count": 1
            }]

        #Store database
        self.SaveDatabase()

    def GetBasket(self, customerID:str) -> dict:
        return self.database[customerID]

    def RemoveFromBasket(self, BasketID:str):
        pass




