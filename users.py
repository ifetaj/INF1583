
class Utilisateur:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def set_name(self, nom):
        self.name=nom 

    def set_id(self, ident):
        self.id = ident

    def affichage(self):
        print("Le nom est {}, et l'identificateur {}".format(self.name, self.id))

users  = Utilisateur("kaola", 123)
print(users.name)
users.affichage()