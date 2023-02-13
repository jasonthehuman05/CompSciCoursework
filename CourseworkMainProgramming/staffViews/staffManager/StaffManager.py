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

    def AddStaff(self):
        pass

    def DisplayStaff(self):
        pass



