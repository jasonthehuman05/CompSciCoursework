import json

class CustomerDB:
    def __init__(self):
        #Vars for operation
        self.FILEPATH = "CourseworkMainProgramming/customers.json"
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

    def GetCustomer(self, customerID:str):
        pass

    def SaveCustomer(self, customerID:str, data:dict):
        pass

    def DeleteCustomer(self, customerID:str):
        pass

    def LoginCustomer(self, userName:str, password:str):
        pass



