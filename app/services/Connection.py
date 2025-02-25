import sqlite3

class Connection:
    
    def __init__(self):
        self.connection = sqlite3.connect('./Db.sqlite')
        
    def getConnection(self):
        return self.connection