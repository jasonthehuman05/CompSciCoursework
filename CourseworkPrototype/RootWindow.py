import tkinter

class RootWindow:
    root = None
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("BuildrightDB Prototype: Inventory Manager")
        self.DrawWidgets()
        self.root.geometry("600x400")
        self.root.mainloop()
    def DrawWidgets(self):
        #CreateButton
        self.createButton = tkinter.Button(self.root, text="ADD INVENTORY", command= lambda:self.AddInventory())
        self.createButton.pack()
        self.createButton.place(x=8, y=8, height=32, relwidth=0.25, anchor="nw")

        #InventoryFrame
        self.inventoryFrame = tkinter.Frame(self.root)
        self.inventoryFrame.configure(background='black')
        self.inventoryFrame.pack()
        self.inventoryFrame.place(x=8, y=48, width = 584, height=300, anchor="nw")
    def AddInventory(self):
        pass





