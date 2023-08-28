from mongo_conection import *
class Element :
    def __init__(self, element_lu) :
        self.nom = element_lu["nom"]
        self.prenom = element_lu["prénom"]
    
    def set_discipline(self, discipline):
        self.discipline = discipline
    
    def set_titre(self,titre):
        self.titre = titre

    def to_json(self):
        element_json = {"nom":self.nom, "prénom":self.prenom, "titre":self.titre}
        return element_json

def set_user(login, passwd):
    bdd = MongoAccess.connexion()
    
    print(f'bdd={bdd}')
    if bdd is not None:
        
        bdd.insertOne({'name':login,'password':passwd})
        MongoAccess.deconnexion()
        return 
    else:
        print("ereur de conection")
        MongoAccess.deconnexion()

        
def get_user(login, passwd):
    bdd = MongoAccess.connexion()
    
    print(f'bdd={bdd}')
    if bdd is not None:
        user = bdd.find_one({'username': login, 'password': passwd})
        MongoAccess.deconnexion()
        return user
    else:
        print("ereur de conection")