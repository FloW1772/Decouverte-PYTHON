class Chat:
    def __init__(self, nom = 'anonyme'):
        self.nom = nom
        print("initialisation de l'instance")

    def __new__(cls, nom='anonyme'):
        print("création de l'instance")
        return super().__new__(cls) # Il est essentiel de retourner une nouvelle instance

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom (self, nom):
        self._nom = nom

    @nom.deleter
    def nom(self):
        self._nom = "anonyme"

tom = Chat("Tom")

print(tom.nom)

tom.nom = 'félix'
print(tom.nom)

del tom.nom
print(tom.nom)