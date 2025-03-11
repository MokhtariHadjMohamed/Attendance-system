from services.Connection import Connection
from module.Service import Service
import sqlite3

class DbService: 
    def __init__(self):
        self.conn = Connection().getConnection()
        
    def getAllItem (self):
        sql = f'select * from service;'
        c = self.conn.cursor()
        c.execute(sql)
        ret =  c.fetchall()
        return ret

    def getItemWithID(self, service_id):
        sql = f'select * from service where id = "{service_id}";'
        c = self.conn.cursor()
        c.execute(sql)
        ret =  c.fetchall()
        for row in ret:
            return row
        
    def insertItem(self,service:Service):
        sql = f'''insert into service (name,state,username,password,adresse,numtelephon) 
        values ("{service.name}", "{service.state}", "{service.username}", "{service.passeword}",
        "{service.adresse}", "{service.nmrTelephone}");'''
        c = self.conn.cursor()
        c.execute(sql)
        self.conn.commit()
        self.conn.close()
        
    def updateItem(service:Service):
        sql = f'''UPDATE service SET name = "{service.name}", state = "{service.state}",
        username = "{service.username}", passeword = "{service.passeword}", 
        adresse = "{service.adresse}", nmrTelephone = "{service.nmrTelephone}",
        WHERE id = {service.id};'''
        c = self.conn.cursor()
        c.execute(sql)
        self.conn.commit()
        self.conn.close()
        
    def deleteItem(service:Service):
        sql = f'DELETE FROM service WHERE id = {service.id};'
        c = self.conn.cursor()
        c.execute(sql)
        self.conn.commit()
        self.conn.close()