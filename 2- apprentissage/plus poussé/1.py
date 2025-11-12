class Chat:
    def __init__(self, nom):
        self._nom = nom

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