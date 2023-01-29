from __future__ import annotations #To fix circular import issue
import tkinter
import StockDatabase
import MainMenu

class ProductDetails:
    def __init__(self, db:StockDatabase.StockDatabase, mainScreen:MainMenu.MainMenu, productNumber:str):
        #Public variables
        self.db = db
        self.mainScreen = mainScreen
        self.productNumber = productNumber

        #Find item
        self.item = self.db.GetItemByProductNumber(self.productNumber)

        #Create Window
        self.root = tkinter.Toplevel()
        self.root.title(f"Product Details: {productNumber}")
        self.root.geometry("1920x1080")
        self.root.attributes('-fullscreen', True) #Makes the window appear in fullscreen mode.
        self.DrawWidgets()
        self.root.mainloop()

    def DrawWidgets(self):
        self.productNumberLabel = tkinter.Label(self.root, text=self.item["productName"], font = "default 72 normal")
        self.productNumberLabel.place(x=0,y=0,height=48)



