import StockDatabase
import MainMenu
'''
╔═══════════════════════╗
║Application Entry Point║
╚═══════════════════════╝
'''

db = StockDatabase.StockDatabase()
print(db.tagIndex)
print(db.titleIndex)
mm = MainMenu.MainMenu(db)
