import tkinter
from staffViews.stockManager import VariationCreator

class DetailsViewer:
    item = dict()
    
    def __init__(self, db, itemNumber:str, parent):
        self.item = db.GetItemByProductNumber(itemNumber)
        self.db = db
        self.parent = parent
        self.itemNumber = itemNumber
        #Main Window
        self.root = tkinter.TopLevel()
        self.root.title(itemNumber)
        self.root.resizable(False, False)
        self.DrawWidgets()

        #Calculate size to accomodate all variations
        winSize = 125 + len(self.item['variations'])*25
        self.root.geometry(f"400x{winSize}")

        self.root.mainloop()
        
    def DrawWidgets(self):
        #Save Button
        saveButton = tkinter.Button(self.root, text="SAVE", command=lambda: self.SaveChanges())
        saveButton.place(x=0,y=0,width=150,height=25)

        #NewVariation Button
        nvButton = tkinter.Button(self.root, text="ADD VARIATION", command=lambda: self.AddVariation())
        nvButton.place(x=150,y=0,width=150,height=25)

        #Delete Button
        nvButton = tkinter.Button(self.root, text="DELETE ITEM", command=lambda: self.DeleteItem(), bg="red")
        nvButton.place(x=300,y=0,width=100,height=25)

        #Item Name
        self.itemNameEntry = tkinter.Entry(self.root)
        self.itemNameLabel = tkinter.Label(self.root, text="Item Name")
        self.itemNameEntry.insert(0, self.item["productName"])
        self.itemNameEntry.place(x=75, y=25, width=300)
        self.itemNameLabel.place(x=0, y=25)

        #Tags
        self.itemTagEntry = tkinter.Entry(self.root)
        self.itemTagLabel = tkinter.Label(self.root, text="Item Tags")

        tags = ""
        for tag in self.item["productTags"]:
            tags += f"{tag}, "
        tags = tags[:-2] #removes ", " from tag string

        self.itemTagEntry.insert(0, tags)
        self.itemTagEntry.place(x=75, y=50, width=300)
        self.itemTagLabel.place(x=0, y=50)

        #Variations
        self.itemVariationsHeaderLabel = tkinter.Label(self.root, text="Item Variations")
        self.itemVariationsHeaderLabel.place(x=0, y=75)
        self.DrawVariations()

    def DrawVariations(self):
        #Make header labels
        self.variationIDLabel = tkinter.Label(self.root, text="ID")
        self.variationIDLabel.place(x=0, y=100)
        self.variationNameLabel = tkinter.Label(self.root, text="Name")
        self.variationNameLabel.place(x=50, y=100)
        self.variationCostLabel = tkinter.Label(self.root, text="Cost")
        self.variationCostLabel.place(x=300, y=100)
        self.variationStockLabel = tkinter.Label(self.root, text="Stock")
        self.variationStockLabel.place(x=350, y=100)
        
        #Get Variations
        variations = self.item["variations"]
        
        yPos = 125 #start at y=125, since there are other labels to accomodate above
        
        #everything needed to put things into lists
        varNum = 0
        self.variationIDEntry = []
        self.variationNameEntry = []
        self.variationCostEntry = []
        self.variationStockEntry =  []

        for variation in variations:
            #For each variation, display the information
            self.variationIDEntry.append(tkinter.Entry(self.root))
            self.variationIDEntry[varNum].insert(0, variation["variationID"])
            self.variationIDEntry[varNum].place(x=0, y=yPos, width = 45)
            
            self.variationNameEntry.append(tkinter.Entry(self.root))
            self.variationNameEntry[varNum].insert(0, variation["variationName"])
            self.variationNameEntry[varNum].place(x=50, y=yPos, width = 245)
            
            self.variationCostEntry.append(tkinter.Entry(self.root))
            self.variationCostEntry[varNum].insert(0, variation["variationCost"])
            self.variationCostEntry[varNum].place(x=300, y=yPos, width = 45)
            
            self.variationStockEntry.append(tkinter.Entry(self.root))
            self.variationStockEntry[varNum].insert(0, variation["stockLevel"])
            self.variationStockEntry[varNum].place(x=350, y=yPos, width = 45)
            yPos+=25
            varNum+=1

    def Passer(self):
        pass

    def SaveChanges(self):
        #Parse Tags
        tags = self.itemTagEntry.get().split(", ")
        for i in range(0, len(tags)):
            tags[i] = ''.join(c for c in tags[i] if c.isalnum())

        #parse varitions
        variations = []
        for i in range(0, len(self.variationIDEntry)): #Go through each item and save the variation
            variation={
                "variationID": self.variationIDEntry[i].get(),
                "variationName":self.variationNameEntry[i].get(),
                "variationCost": float(self.variationCostEntry[i].get()),
                "stockLevel": float(self.variationStockEntry[i].get())
            }
            variations.append(variation)

        item = {
          "productNumber": str(self.item["productNumber"]),
          "productName": self.itemNameEntry.get(),
          "productTags": tags,
          "variations": variations
        }
        
        self.db.UpdateItem(self.itemNumber, item)
        
        
        try: self.parent.Refresh()
        except: pass
     
    def AddVariation(self):
        vc = VariationCreator.VariationCreator(self.db, self.itemNumber, self.root)

    def DeleteItem(self):
        self.db.DeleteItem(self.itemNumber)
        self.parent.Refresh()
        self.root.destroy() #Remove Window