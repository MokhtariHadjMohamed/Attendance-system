from services.Connection import Connection
from module.Employe import Employe
import sqlite3

class DbUser: 
    def __init__(self):
        self.conn = Connection().getConnection()
        
    def getAllItem (self):
        sql = f'select * from user;'
        c = self.conn.cursor()
        c.execute(sql)
        ret =  c.fetchall()
        return ret

    def getItemWithID(self, user_id):
        sql = f'select * from user where id = {user_id};'
        c = self.conn.cursor()
        c.execute(sql)
        ret =  c.fetchall()
        for row in ret:
            return row
        
    def insertItem(self, employe:Employe):
        sql = f'''insert into user (name,state,username,password,nmr_telephone,prenom,timein
                ,timeout,typeUser,image,fingerPrinte, id_service) 
        values ("{employe.name}", "{employe.state}", "{employe.username}", "{employe.passeword}",
         "{employe.nmrTelephone}", "{employe.prenom}", "{employe.timein}"
        , "{employe.timeout}", "{employe.typeUser}", "{employe.image}", "{employe.fingerPrinte}"
        , "{employe.service.id}");'''
        c = self.conn.cursor()
        c.execute(sql)
        self.conn.commit()
        self.conn.close()
        
    def updateItem(employe:Employe):
        sql = f'''UPDATE user SET name = "{employe.name}", state = "{employe.state}",
        username = "{employe.username}", passeword = "{employe.passeword}", 
        adresse = "{employe.adresse}", nmrTelephone = "{employe.nmrTelephone}",
        prenom = "{employe.prenom}", timein = "{employe.timein}", 
        timeout = "{employe.timeout}", typeUser = "{employe.typeUser}",
        image = "{employe.image}", fingerPrinte = "{employe.fingerPrinte}", 
        service = "{employe.service}",
        WHERE id = {employe.id};'''
        c = self.conn.cursor()
        c.execute(sql)
        self.conn.commit()
        self.conn.close()
        
    def deleteItem(employe:Employe):
        sql = f'DELETE FROM user WHERE id = {employe.id};'
        c = self.conn.cursor()
        c.execute(sql)
        self.conn.commit()
        self.conn.close()