import tkinter

class StaffEditor:
    def __init__(self, staffdb, id:str):
        #Public vars
        self.staffdb = staffdb
        self.id = id
        self.staff = self.staffdb.GetStaff(id)
        #Build Window
        self.root = tkinter.Toplevel()
        self.root.title("BuildrightDB Staff Editor")
        self.root.geometry("180x100")
        self.DrawWidgets()
        self.DisplayData()
        self.root.mainloop()

    def DrawWidgets(self):
        #Entry Labels
        idLabel = tkinter.Label(self.root, text="ID")
        loginLabel = tkinter.Label(self.root, text="Login")
        passwordLabel = tkinter.Label(self.root, text="Password")

        #entries
        self.idEntry = tkinter.Entry(self.root)
        self.loginEntry = tkinter.Entry(self.root)
        self.passwordEntry = tkinter.Entry(self.root)

        #Save Button
        self.saveButton = tkinter.Button(self.root, text="Save Changes", command=lambda:self.SaveChanges())

        #Put into grid
        idLabel.grid(row=0,column=0)
        loginLabel.grid(row=1,column=0)
        passwordLabel.grid(row=2,column=0)
        
        self.idEntry.grid(row=0,column=1)
        self.loginEntry.grid(row=1,column=1)
        self.passwordEntry.grid(row=2,column=1)

        self.saveButton.grid(row=3,column=1)

    def DisplayData(self):
        self.idEntry.insert(0,self.staff["StaffID"]) 
        self.loginEntry.insert(0,self.staff["Login"]) 
        self.passwordEntry.insert(0,self.staff["Password"]) 

    def SaveChanges(self):
        data = {
            "StaffID": self.idEntry.get(),
            "Login": self.loginEntry.get(),
            "Password": self.passwordEntry.get()
        }
        self.staffdb.SaveStaff(self.id, data)