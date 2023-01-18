import tkinter
import StockDatabase
import VariationCreator

class ItemCreator:
    item = dict()
    
    def __init__(self, db:StockDatabase.StockDatabase):
        self.db = db
        #Main Window
        self.root = tkinter.Tk()
        self.root.title("New Item")
        self.DrawWidgets()

        self.root.geometry(f"300x200")

        self.root.mainloop()
        
    def DrawWidgets(self):
        #Item Name Widgets
        self.nameLabel = tkinter.Label(self.root, text="Item Name")
        self.nameEntry = tkinter.Entry(self.root)
        self.nameLabel.place(x=0,y=0,width=75)
        self.nameEntry.place(x=75,y=0,width=225)

        #Item Tags Widgets
        self.tagsLabel = tkinter.Label(self.root, text="Item Tags")
        self.tagsHelpLabel = tkinter.Label(self.root, text="Separate with a comma (eg. tag1, tag2)")
        self.tagsEntry = tkinter.Entry(self.root)
        self.tagsLabel.place(x=0,y=25,width=75)
        self.tagsHelpLabel.place(x=75,y=50)
        self.tagsEntry.place(x=75,y=25,width=225)

    
    def Passer(self):
        pass