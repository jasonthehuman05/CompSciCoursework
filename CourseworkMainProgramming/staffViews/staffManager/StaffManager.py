import tkinter

class StaffManager:
    def __init__(self, staffdb):
        #Public vars
        self.staffdb = staffdb

        #Build Window
        self.root = tkinter.Toplevel()
        self.root.title("BuildrightDB Staff Manager")
        self.root.geometry("500x400")
        self.DrawWidgets()
        self.root.mainloop()

    def DrawWidgets(self):
        self.addStaffButton = tkinter.Button(self.root, text="Add New Staff", command=lambda:self.AddStaff())
        self.addStaffButton.place(x=0,y=0,width=100,height=24)
        self.DisplayStaff()

    def AddStaff(self):
        pass

    def DisplayStaff(self):
        pos = 28
        for i in self.staffdb.database:
            idLabel = tkinter.Label(self.root, text=i["StaffID"])
            idLabel.place(x=0,y=pos,width=50,height=32)

            nameLabel = tkinter.Label(self.root, text=i["Login"])
            nameLabel.place(x=50,y=pos,width=100,height=32)

            idLabel = tkinter.Button(self.root, text="Delete")
            idLabel.place(x=150,y=pos,width=50,height=32)

            pos += 40



