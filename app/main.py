from screen import auth_screen
from screen.service_screen import ServiceScreen
from screen.employer_screen import EmployerScreen

auth = auth_screen.AuthScreen()
user = auth.get_user()

while True:
    if user !=None:
        if len(user) == 7:
            ServiceScreen(user)
        elif len(user) > 7:
            typeuser = user[10]
            if typeuser == "arh":
                EmployerScreen()
            elif typeuser =="inf":
                EmployerScreen()
            else:
                print("emloye")
    else:
        print('no user')