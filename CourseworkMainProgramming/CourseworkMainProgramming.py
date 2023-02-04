from databases import StockDatabase, CustomerDatabase, StaffDatabase, BasketDatabase
import MainCustomerScreen, CustomerLoginWindow
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

cl = CustomerLoginWindow.CustomerLoginWindow(db,customerdb, bdb)