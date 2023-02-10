import tkinter

class VariationCreator:
    item = dict()
    
    def __init__(self, db, itemNumber:str, parentWin):
        self.parent = parentWin
        self.item = db.GetItemByProductNumber(itemNumber)
        self.db = db
        self.itemNumber = itemNumber
        #Main Window
        self.root = tkinter.Tk()
        self.root.title(f"New variation for {itemNumber}")
        self.DrawWidgets()
        #Calculate size to accomodate all variations
        self.root.geometry(f"200x125")
        self.root.resizable(False, False)
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
        self.variationIDEntry.place(x=50, y=0, width=150)
        self.variationNameEntry = tkinter.Entry(self.root)
        self.variationNameEntry.place(x=50, y=25, width=150)
        self.variationCostEntry = tkinter.Entry(self.root)
        self.variationCostEntry.place(x=50, y=50, width=150)
        self.variationStockEntry = tkinter.Entry(self.root)
        self.variationStockEntry.place(x=50, y=75, width=150)

        self.saveButton = tkinter.Button(self.root, text="SAVE CHANGES", command=lambda:self.AddVariationToItem(), bg="green")
        self.saveButton.place(x=0,y=100,height=25,width=200)

    def AddVariationToItem(self):
        #Build variaiton and add to item
        self.item["variations"].append({
            "variationID": self.variationIDEntry.get(),
            "variationName": self.variationNameEntry.get(),
            "variationCost": float(self.variationCostEntry.get()),
            "stockLevel": float(self.variationStockEntry.get())
        })

        #Update item in DB
        self.db.UpdateItem(self.itemNumber, self.item)

        #Destroy Windows
        self.root.destroy()
        self.parent.destroy()

    def Passer(self):
        pass
            