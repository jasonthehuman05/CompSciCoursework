import tkinter
from staffViews.stockManager import DetailsViewer

class SearchWindow:
    def __init__(self, db):
        self.db = db
        self.root = tkinter.Tk()
        #self.root.geometry("200x215")
        self.DrawWidgets()

        self.root.mainloop()

    def DrawWidgets(self):        
        #Search Bar
        self.searchEntry = tkinter.Entry(self.root)
        self.searchEntry.grid(row=0,column=0,sticky="nesw")

        #Search Button
        self.searchButton = tkinter.Button(self.root, text="Search", command=lambda:self.RunSearch())
        self.searchButton.grid(row=0,column=1,sticky="nesw")

        #Customer List Box Container
        self.listBoxContainer = tkinter.Frame(self.root)
        self.listBoxContainer.grid(row=1,column=0,columnspan=2)

        #Listbox and scrollbar
        self.listBox = tkinter.Listbox(self.listBoxContainer, width=50, height=18)
        self.listBox.pack(side="left", fill="y")
        self.lbScrollbar = tkinter.Scrollbar(self.listBoxContainer, orient="vertical")
        self.listBox.config(yscrollcommand=self.lbScrollbar.set)
        self.lbScrollbar.pack(side="right", fill="y")

        #Open Button
        self.openDetailsButton = tkinter.Button(self.root, text="Open Details", command=lambda:self.OpenItem(),bg="#aaaaaa")
        self.openDetailsButton.grid(column=0,row=2,columnspan=2,sticky="nesw",)

    def RunSearch(self):
        #Get search results from db
        results = self.db.SearchForItem(self.searchEntry.get())

        #Clear box
        self.listBox.delete(0,tkinter.END)

        #Add each item to the dropdown
        for i in results:
            #i is an index in the database
            itemObj = self.db.database["items"][i]
            item = f'{itemObj["productNumber"]} :: {itemObj["productName"]}'
            self.listBox.insert("end", item)

    def OpenItem(self):
        itemNumber = self.listBox.get(self.listBox.curselection()[0]).split(" :: ")[0] #Get ID from the selected item
        dv = DetailsViewer.DetailsViewer(self.db, itemNumber, self.root)




