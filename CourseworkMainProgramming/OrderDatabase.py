import json

class OrderDatabase:
    def __init__(self):
        #Vars for operation
        self.FILEPATH = "orders.json"
        self.database = []
        self.nextId = 0

        self.LoadDatabase()

    def SaveDatabase(self):
        jsonString = json.dumps(self.database)
        with open(self.FILEPATH, "w+") as file:
            file.write(jsonString)


    def LoadDatabase(self):
        with open(self.FILEPATH, "r") as file:
            self.database = json.loads(file.read())
        
        #Find the next staff id
        for staff in self.database:
            val = int(staff["StaffID"])
            if val >= self.nextId: self.nextId = val + 1

    def AddOrder(self, customerID:str, basket:list):
        #Create order dictionary
        order = {
            "OrderID": str(self.nextId).zfill(6),
            "CustomerID": customerID,
            "Items": basket
        }
        #Add to json
        self.database.append(order)
        self.SaveDatabase()
        self.nextId += 1

    def GetOrder(self, orderID:str) -> dict:
        retval = None
        for order in self.database:
            if order["OrderID"] == orderID:
                retval = order
                break
        return retval

    def SaveOrder(self, OrderID:str, data:dict):
        for i in range(0, len(self.database)):
            if self.database[i]["OrderID"] == OrderID:
                self.database[i] = data
                break

    def DeleteOrder(self, OrderID:str):
        for i in range(0, len(self.database)):
            if self.database[i]["OrderID"] == OrderID:
                self.database.pop(i)
                break



