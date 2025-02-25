from services.Auth import Auth

class AuthScreen:
    def __init__(self):
        auth = Auth()
        userName = input('user name: ')
        password = input('password: ')
        self.user = auth.sing_in(userName, password)
    
    def get_user(self):
        return self.user