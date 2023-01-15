import tkinter
import StockDatabase

class DetailsViewer:
    item = dict()
    
    def __init__(self, db:StockDatabase.StockDatabase, itemNumber:str):
        self.item = db.GetItemByProductNumber(itemNumber)
        
        #Main Window
        self.root = tkinter.Tk()
        self.root.geometry("400x200")
        self.root.title(itemNumber)
        self.root.mainloop()
        
    def DrawWidgets(self):
        pass