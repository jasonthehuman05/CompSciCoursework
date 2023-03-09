from staffViews.stockManager import RootWindow

#Creates instance of window from prototype. 
class StockManager:
	def __init__(self, db):
		mainWin = RootWindow.RootWindow(db)