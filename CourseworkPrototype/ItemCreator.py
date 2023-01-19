import tkinter
import StockDatabase
import VariationCreator
import RootWindow

class ItemCreator:
    item = dict()
    
    def __init__(self, db:StockDatabase.StockDatabase, parent):
        self.db = db
        self.parent = parent
        #Main Window
        self.root = tkinter.Tk()
        self.root.resizable(False, False)
        self.root.title("New Item")
        self.DrawWidgets()

        self.root.geometry(f"300x225")

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

        #Variation Creator
        self.variationNoticeLabel = tkinter.Label(self.root, text="Add your first variation", foreground="red")
        self.variationNameLabel = tkinter.Label(self.root, text="Variation Name")
        self.variationCostLabel = tkinter.Label(self.root, text="Variation Cost")
        self.variationStockLabel = tkinter.Label(self.root, text="Variation Stock")
        
        self.variationNameEntry = tkinter.Entry(self.root)
        self.variationCostEntry = tkinter.Entry(self.root)
        self.variationStockEntry = tkinter.Entry(self.root)

        self.variationNoticeLabel.place(x=0,y=75)
        self.variationNameLabel.place(x=0,y=100)
        self.variationCostLabel.place(x=0,y=125)
        self.variationStockLabel.place(x=0,y=150)
        
        self.variationNameEntry.place(x=100,y=100)
        self.variationCostEntry.place(x=100,y=125)
        self.variationStockEntry.place(x=100,y=150)

        #Save Button
        self.addItemButton = tkinter.Button(self.root, text="ADD ITEM", bg="lime", command=lambda:self.AddNewItem())
        self.addItemButton.place(x=0,y=175,width=300,height=50)

    def AddNewItem(self):
        #Turn tags string into individual tags
        tags = self.tagsEntry.get().split(",")
        for i in range(0, len(tags)):
            tags[i] = (''.join(c for c in tags[i] if c.isalnum())).lower()

        #Create variation dict
        variation = [{
            "variationID": "1",
            "variationName": self.variationNameEntry.get(),
            "variationCost": self.variationCostEntry.get(),
            "stockLevel": self.variationCostEntry.get()
        }]

        self.db.CreateItem(self.nameEntry.get(), tags, variation)

        self.root.destroy()
        self.parent.Refresh()

    def Passer(self):
        pass