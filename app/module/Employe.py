from module.User import User
class Employe(User):
    def __init__(self,id,name,state,username,passeword,adresse,nmrTelephone,prenom,timein,timeout
                 ,salaire,typeUser,image,fingerPrinte, service):
        super().__init__(id, name,state,username,passeword,adresse,nmrTelephone)
        self.prenom=prenom
        self.timein=timein
        self.timeout=timeout
        self.salaire=salaire
        self.typeUser=typeUser
        self.image=image
        self.fingerPrinte=fingerPrinte
        self.service = service