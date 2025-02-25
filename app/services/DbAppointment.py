from services.Connection import Connection
from module.Appointment import Appointment
import sqlite3

class DbAppointment: 
    def __init__(self):
        self.conn = Connection().getConnection()
        
    def getAllItem ():
        sql = f'select * from appointment;'
        c = self.conn.cursor()
        c.execute(sql)
        ret =  c.fetchall()
        for row in ret:
            return row

    def getItemWithID(appointment_id):
        sql = f'select * from appointment where id = "{appointment_id}";'
        c = self.conn.cursor()
        c.execute(sql)
        ret =  c.fetchall()
        for row in ret:
            return row
        
    def insertItem(self, appointment:Appointment):
        sql = f'''insert into appointment (id_service,id_user,checkin,chekout,date_appointment) 
        values ({appointment.service.id}, {appointment.employe.id}, "{appointment.checkin}",
        "{appointment.checkout}", "{appointment.date}");'''
        c = self.conn.cursor()
        c.execute(sql)
        self.conn.commit()
        self.conn.close()
        
    def updateItem(self, appointment:Appointment):
        sql = f'''UPDATE appointment SET id_service = {appointment.service.id}, id_user = {appointment.employe.id}, 
        checkin = "{appointment.checkin}", checkout = "{appointment.checkout}", date_appointment = "{appointment.date}" 
        WHERE id = {appointment.Id};'''
        c = self.conn.cursor()
        c.execute(sql)
        self.conn.commit()
        self.conn.close()
        
    def deleteItem(appointment:Appointment):
        sql = f'DELETE FROM appointment WHERE id = {appointment.Id};'
        c = self.conn.cursor()
        c.execute(sql)
        self.conn.commit()
        self.conn.close()
        
    def getItemWithIDUserAndDate(self, user_id, date):
        sql = f'select * from appointment where id_user = "{user_id}" and date_appointment = "{date}";'
        c = self.conn.cursor()
        c.execute(sql)
        ret =  c.fetchall()
        for row in ret:
            return row

    def getAllPresentDate(self, date):
        sql = f'select * from appointment where date_appointment = "{date}";'
        c = self.conn.cursor()
        c.execute(sql)
        ret =  c.fetchall()
        for row in ret:
            return row

    def getAllPaste(self, date):
        sql = f'SELECT * from user as u, appointment as ap where ap.date_appointment = "{date}" and ap.id_user != u.id;'
        c = self.conn.cursor()
        c.execute(sql)
        ret =  c.fetchall()
        for row in ret:
            return row