import StockDatabase, CustomerDatabase, StaffDatabase
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

#mm = MainCustomerScreen.MainCustomerScreen(db)
cl = CustomerLoginWindow.CustomerLoginWindow()