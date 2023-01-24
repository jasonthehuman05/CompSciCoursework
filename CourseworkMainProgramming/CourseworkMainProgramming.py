import StockDatabase
import MainMenu
'''
╔═══════════════════════╗
║Application Entry Point║
╚═══════════════════════╝
'''

db = StockDatabase.StockDatabase()

mm = MainMenu.MainMenu(db)
