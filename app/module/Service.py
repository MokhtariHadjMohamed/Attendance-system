from module.User import User
class Service(User):
    def __init__(self,id,name,state,username,passeword,adresse,nmrTelephone, empoloyee):
        super.__init__(name,state,username,passeword,adresse,nmrTelephone)
        self.empoloyee = empoloyee