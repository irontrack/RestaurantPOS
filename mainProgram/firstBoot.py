from dataBase import posDatabase
from dataFields import user
# this is a one time use program to make and initialize the pos database with it's first
# admin user and menu items

db = posDatabase()
admin = user("jesse","harper",5558675309,True)
db.addNewUser(admin)