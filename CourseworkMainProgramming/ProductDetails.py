import tkinter
import StockDatabase
import MainMenu

class my_class:
    def __init__(self, db:StockDatabase.StockDatabase, mainScreen:MainMenu.MainMenu, productNumber:str):
        self.db = db
        self.mainScreen = mainScreen

        self.root = tkinter.Toplevel()
        self.root.title("Product Details")

        self.root.mainloop()




