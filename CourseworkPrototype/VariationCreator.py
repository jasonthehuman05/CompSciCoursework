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
        self.root.title(f"New variation for {itemNumber}")
        self.DrawWidgets()
        #Calculate size to accomodate all variations
        self.root.geometry(f"400x100")

        self.root.mainloop()
        
    def DrawWidgets(self):
        self.variationIDLabel = tkinter.Label(self.root, text="ID")
        self.variationIDLabel.place(x=0, y=0)
        self.variationNameLabel = tkinter.Label(self.root, text="Name")
        self.variationNameLabel.place(x=0, y=25)
        self.variationCostLabel = tkinter.Label(self.root, text="Cost")
        self.variationCostLabel.place(x=0, y=50)
        self.variationStockLabel = tkinter.Label(self.root, text="Stock")
        self.variationStockLabel.place(x=0, y=75)

        self.variationIDEntry = tkinter.Entry(self.root)
        self.variationIDEntry.place(x=0, y=0)
        self.variationNameEntry = tkinter.Entry(self.root, text="Name")
        self.variationNameEntry.place(x=0, y=25)
        self.variationCostEntry = tkinter.Entry(self.root, text="Cost")
        self.variationCostEntry.place(x=0, y=50)
        self.variationStockEntry = tkinter.Entry(self.root, text="Stock")
        self.variationStockEntry.place(x=0, y=75)

    def Passer(self):
        pass
            