from services.DbAppointment import DbAppointment
from datetime import datetime
from module.Employe import Employe
from services.DbUser import DbUser

class EmployerScreen :
    def __init__(self):
        print("1-show all prisent")
        print("2-show all apsent")
        print("3-add new employer")
        print("4-add new service")
        a = input("choose:")
        if a == "1":
            now = datetime.now()
            appointment=DbAppointment().getAllPresentDate(now.date)
            print(appointment)
        elif a =="2":
            now = datetime.now()
            appointment=DbAppointment().getAllPaste(now.date)
            print(appointment)
        elif a =="3":
            print("Add new employer:")
            name = input('name:')
            prenom = input('prenom:')
            state = input('state:')
            username = input('username:')
            passeword = input('password:')
            adresse = input('adresse:')
            nmrTelephone = input('nmrTelephone:')
            timein = input ('timein:')
            timeout = input('timeout:')
            salaire = input('salaire')
            typeUser = input('typeUser:')
            image = input('image:')
            fingerPrinte = input('fingerPrinte:')
            service = input('service:')
            employe = Employe(id=None,name=name,state=state,username=username,passeword=passeword,adresse=adresse,
                              nmrTelephone=nmrTelephone,prenom=prenom,timein=timein,timeout=timein,salaire=salaire
                              ,typeUser=typeUser,image=image,fingerPrinte=fingerPrinte,service=service)
            DbUser().insertItem(user)
        elif a =="4":
            print("4-add new service")


