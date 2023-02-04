from databases import StockDatabase, CustomerDatabase, StaffDatabase, BasketDatabase
import MainMenu
'''
╔═══════════════════════╗
║Application Entry Point║
╚═══════════════════════╝
'''

#Create Database Instances
db = StockDatabase.StockDatabase()
customerdb = CustomerDatabase.CustomerDB()
staffdb = StaffDatabase.StaffDB()
bdb = BasketDatabase.BasketDatabase()

cl = MainMenu.MainMenu(db,customerdb,staffdb,bdb)