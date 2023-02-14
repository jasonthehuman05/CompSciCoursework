import tkinter

class CustomerManager:
    def __init__(self, customerdb):
        #Public Vars
        self.customerdb = customerdb

        #Create Window
        self.root = tkinter.Toplevel()
        self.root.title("BuildrightDB Customer Manager")
        self.DrawWidgets()

    def DrawWidgets(self):
        #Customer List Box Container
        self.listBoxContainer = tkinter.Frame(self.root)
        self.listBoxContainer.grid(row=0,column=0)

        #Listbox and scrollbar
        self.listBox = tkinter.Listbox(self.listBoxContainer)
        self.listBox.pack(side="left", fill="y")
        self.lbScrollbar = tkinter.Scrollbar(self.listBoxContainer, orient="vertical")
        self.listBox.config(yscrollcommand=self.lbScrollbar.set)
        self.lbScrollbar.pack(side="right", fill="y")





