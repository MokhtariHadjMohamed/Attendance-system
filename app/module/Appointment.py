from module.Employe import Employe
from module.Service import Service
class Appointment:
    def __init__(self, id, checkIn, checkOut, date, service:Service, employe:Employe):
        self.id = id
        self.checkIn= checkIn
        self.checkOut=checkOut
        self.date = date
        self.service = service
        self.employe = employe