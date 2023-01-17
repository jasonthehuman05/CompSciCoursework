import tkinter
import StockDatabase

class VariationCreator:
    item = dict()
    
    def __init__(self, db:StockDatabase.StockDatabase, itemNumber:str):
        self.item = db.GetItemByProductNumber(itemNumber)
        self.db = db
        self.itemNumber = itemNumber
        #Main Window
        self.root = tkinter.Tk()
        self.root.title(itemNumber)
        self.DrawWidgets()
        #Calculate size to accomodate all variations
        self.root.geometry(f"200x100")

        self.root.mainloop()
        
    def DrawWidgets(self):
        pass

    def Passer(self):
        pass
            