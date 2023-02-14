import tkinter

class StaffCreator:
    def __init__(self, staffdb):
        #Public vars
        self.staffdb = staffdb
        self.id = id
        self.staff = self.staffdb.GetStaff(id)
        #Build Window
        self.root = tkinter.Toplevel()
        self.root.title("BuildrightDB Staff Creator")
        self.root.geometry("180x100")
        self.DrawWidgets()
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
        self.saveButton = tkinter.Button(self.root, text="Add Staff Member", command=lambda:self.AddStaff())

        #Put into grid
        loginLabel.grid(row=0,column=0)
        passwordLabel.grid(row=1,column=0)
        
        self.loginEntry.grid(row=0,column=1)
        self.passwordEntry.grid(row=1,column=1)

        self.saveButton.grid(row=2,column=1)

    def AddStaff(self):
        self.staffdb.AddStaff(self.loginEntry.get(),self.passwordEntry.get())
        self.root.quit()
        self.root.destroy()