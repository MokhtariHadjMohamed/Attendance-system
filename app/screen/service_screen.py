from services.DbUser import DbUser
from services.DbService import DbService
from services.DbAppointment import DbAppointment
from module.Appointment import Appointment
from module.Employe import Employe
from datetime import datetime

class ServiceScreen:
    def __init__(self, service):
        userId =input("employe Id:")
        user = DbUser().getItemWithID(userId)
        service = DbService().getItemWithID(user[13])
        if user != None:
            now = datetime.now()
            if now.hour >= 8 and now.hour <= 12:
                dbAppointment = DbAppointment()
                appointment = dbAppointment.getItemWithIDUserAndDate(user[0], now.date)
                if appointment != None:
                    print("update")
                else:
                    formatted_time = now.strftime("%H:%M:%S")
                    appointment = Appointment(id=None, checkOut=None, checkIn=formatted_time, date= now.date, service=service, employe=Employe(*user,service=service))
                    dbAppointment.insertItem(appointment)
                    print('create')
            elif now.hour >= 13 and now.hour <= 16:
                dbAppointment = DbAppointment()
                appointment = dbAppointment.getItemWithIDUserAndDate(user[0], now.date)
                if appointment != None:
                    print("update")
                else:
                    formatted_time = now.strftime("%H:%M:%S")
                    appointment = Appointment(id=None, checkOut=None, checkIn=formatted_time, date= now.date, service=service, employe=Employe(*user,service=service))
                    dbAppointment.insertItem(appointment)
                    print('create')
        else:
            print("user not valide")