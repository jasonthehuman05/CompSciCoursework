#This is the startfile
import StockDatabase
import RootWindow

db = StockDatabase.StockDatabase()

mainWin = RootWindow.RootWindow(db)