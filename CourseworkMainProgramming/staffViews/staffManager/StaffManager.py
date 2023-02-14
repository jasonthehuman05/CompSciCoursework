import tkinter
from staffViews.staffManager import StaffEditor, StaffCreator

class StaffManager:
    def __init__(self, staffdb):
        #Public vars
        self.staffdb = staffdb

        #Build Window
        self.root = tkinter.Toplevel()
        self.root.title("BuildrightDB Staff Manager")
        self.root.geometry("350x800")
        self.root.protocol("WM_DELETE_WINDOW", self.HandleClose) #Captures the close event to close it properly
        self.DrawWidgets()
        self.root.mainloop()

    def DrawWidgets(self):
        self.addStaffButton = tkinter.Button(self.root, text="Add New Staff", command=lambda:self.AddStaff())
        self.addStaffButton.place(x=0,y=0,width=350,height=24)
        self.DisplayStaff()

    def AddStaff(self):
        #Open staff creator
        sc = StaffCreator.StaffCreator(self.staffdb)
        pass

    def DeleteStaff(self, id:str):
        self.staffdb.DeleteStaff(id) #Deletes staff from database

    def EditStaff(self, id:str):
        #Open edit window
        se = StaffEditor.StaffEditor(self.staffdb,id)
        pass
    
    def DisplayStaff(self):
        pos = 28
        for i in self.staffdb.database:
            # id and name labels
            idLabel = tkinter.Label(self.root, text=i["StaffID"])
            idLabel.place(x=0,y=pos,width=50,height=32)

            nameLabel = tkinter.Label(self.root, text=i["Login"])
            nameLabel.place(x=50,y=pos,width=100,height=32)

            #Delete and edit buttons: lambda passes through ID
            deleteButton = tkinter.Button(self.root, text="Delete", command=lambda id=i["StaffID"]: self.DeleteStaff(id))
            deleteButton.place(x=250,y=pos,width=100,height=32)

            editButton = tkinter.Button(self.root, text="Edit", command=lambda id=i["StaffID"]: self.EditStaff(id))
            editButton.place(x=150,y=pos,width=100,height=32)

            pos += 40

    def HandleClose(self):
        #print("Closing!")
        self.root.quit()
        self.root.destroy()



