import tkinter
from databases import CustomerDatabase

class OrderManager:
    def __init__(self, cdb:CustomerDatabase.CustomerDB):
        #Public Vars

        #Make Window
        self.root = tkinter.Toplevel()
        self.root.title("BuildrightDB Orders")
        self.root.geometry("500x300")
        
        self.DrawWidgets()
        self.root.mainloop()

            
    def DrawWidgets(self):
        #Orders Container
        self.orderContainer = tkinter.Frame(self.root)
        
        #Details Container
        self.detailsContainer = tkinter.Frame(self.root)