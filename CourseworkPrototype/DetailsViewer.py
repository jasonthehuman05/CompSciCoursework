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
        self.DrawWidgets()
        self.root.mainloop()
        
    def DrawWidgets(self):
        itemNameEntry = tkinter.Entry(self.root)
        itemNameLabel = tkinter.Label(self.root, text="Item Name")
        itemNameEntry.insert(0, self.item["productName"])
        itemNameEntry.place(x=75, y=0, width=300)
        itemNameLabel.place(x=0, y=0)
