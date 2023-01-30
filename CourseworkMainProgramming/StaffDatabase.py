import json

class StaffDB:
    def __init__(self):
        #Vars for operation
        self.FILEPATH = "CourseworkMainProgramming/staff.json"
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

    def AddStaff(self, login:str, password:str):
        #Create staff dictionary
        staff = {
            "StaffID": str(self.nextId).zfill(6),
            "Login": login,
            "Password": password
        }
        #Add to json
        self.database.append(staff)
        self.SaveDatabase()
        self.nextId += 1

    def GetStaff(self, staffID:str) -> dict:
        retval = None
        for staff in self.database:
            if staff["StaffID"] == staffID:
                retval = staff
                break
        return retval

    def SaveStaff(self, StaffID:str, data:dict):
        for i in range(0, len(self.database)):
            if self.database[i]["StaffID"] == StaffID:
                self.database[i] = data
                break

    def DeleteStaff(self, StaffID:str):
        for i in range(0, len(self.database)):
            if self.database[i]["StaffID"] == StaffID:
                self.database.pop(i)
                break

    def LoginStaff(self, userName:str, password:str) -> str:
        StaffID = "000000" #ID 000000 will represent a failed login
        
        #Go through each staff member
        for i in range(0, len(self.database)):
            if self.database[i]["Login"] == userName: #Email match?
                if self.database[i]["Password"] == password:#Password match?
                    StaffID = self.database[i]["StaffID"]#Declare correct id to return
        
        return StaffID



