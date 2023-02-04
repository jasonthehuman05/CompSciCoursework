import json

class CustomerDB:
    def __init__(self):
        #Vars for operation
        self.FILEPATH = "databases/customers.json"
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
        
        #Find the next customer id
        for customer in self.database:
            val = int(customer["CustomerID"])
            if val >= self.nextId: self.nextId = val + 1

    def AddCustomer(self, email:str, password:str, addrl1:str, addrl2:str, city:str, postcode:str, phoneNumber:str):
        #Create customer dictionary
        customer = {
            "CustomerID": str(self.nextId).zfill(6),
            "Email": email,
            "Password": password,
            "addressLine1": addrl1,
            "AddressLine2": addrl2,
            "City": city,
            "Postcode": postcode,
            "PhoneNumber": phoneNumber
        }
        #Add to json
        self.database.append(customer)
        self.SaveDatabase()
        self.nextId += 1

    def GetCustomer(self, customerID:str) -> dict:
        retval = None
        for customer in self.database:
            if customer["CustomerID"] == customerID:
                retval = customer
                break
        return retval

    def SaveCustomer(self, customerID:str, data:dict):
        for i in range(0, len(self.database)):
            if self.database[i]["CustomerID"] == customerID:
                self.database[i] = data
                break

    def DeleteCustomer(self, customerID:str):
        for i in range(0, len(self.database)):
            if self.database[i]["CustomerID"] == customerID:
                self.database.pop(i)
                break

    def LoginCustomer(self, userName:str, password:str) -> str:
        customerID = "000000" #ID 000000 will represent a failed login
        
        #Go through each customer
        for i in range(0, len(self.database)):
            if self.database[i]["Email"] == userName: #Email match?
                if self.database[i]["Password"] == password:#Password match?
                    customerID = self.database[i]["CustomerID"]#Declare correct id to return
        
        return customerID



