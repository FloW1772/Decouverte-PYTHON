class Chat:
    def __init__(self, nom):
        self.nom = nom

    def afficher_nom(self):
        return self.nom

tom = Chat('Tom')

print(tom.afficher_nom())
print(Chat.afficher_nom(tom))