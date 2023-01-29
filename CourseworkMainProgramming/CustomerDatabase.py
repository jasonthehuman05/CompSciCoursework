import json

class CustomerDB:
    def __init__(self):
        self.database = []

    def SaveDatabase(self):
        pass

    def LoadDatabase(self):
        pass

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



