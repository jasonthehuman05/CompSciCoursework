#This is the startfile
from staffViews.stockManager import RootWindow

class StockManager:
	def __init__(self, db):
		mainWin = RootWindow.RootWindow(db)