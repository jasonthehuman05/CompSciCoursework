import json

class BasketDatabase:
    def __init__(self):
        #Vars for operation
        self.FILEPATH = "basket.json"
        self.database = []
        self.nextId = 0

        #self.LoadDatabase()

    def SaveDatabase(self):
        with open(self.FILEPATH, "w+") as file:
            jsonstring = json.dumps(self.database)
            file.write(jsonstring)


    def LoadDatabase(self):
        with open(self.FILEPATH, "r") as file:
            self.database = json.loads(file.read())

    def AddToBasket(self, customerID:str, productIDWithVariation:str):
        #Check if the basket exists
        #if it exists, add to basket
        #if it doesn't exist, create basket and add
        pass

    def GetBasket(self, customerID:str) -> dict:
        return self.database[customerID]

    def RemoveFromBasket(self, BasketID:str):
        pass




