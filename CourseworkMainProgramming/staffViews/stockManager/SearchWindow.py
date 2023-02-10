import tkinter

class SearchWindow:
    def __init__(self, db):
        self.db = db
        self.root = tkinter.Tk()
        self.root.geometry("200x200")
        self.DrawWidgets()

        self.root.mainloop()

    def DrawWidgets(self):
        #Make searchbox
        self.searchBox = tkinter.Entry(self.root)
        self.searchBox.place(x=0,y=0,width=150,height=25)

        #Search button
        self.searchButton = tkinter.Button(self.root, text="Search", command=lambda:self.RunSearch())
        self.searchButton.place(x=150,y=0,width=50,height=25)

        #ListBox of items from search
        self.listbox = tkinter.Listbox(self.root)
        self.listbox.place(x=0,y=32,width=200,height=175)

    def RunSearch(self):
        #Get search results from db
        results = self.db.SearchForItem(self.searchBox.get())
        print(results)

        for i in results:
            #i is an index in the database
            itemObj = self.db.database["items"][i]
            item = f'{itemObj["productNumber"]} :: {itemObj["productName"]}'
            self.listbox.insert("end", item)






