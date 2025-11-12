# TP06 - Nombres Premiers
print("____Nombres Premiers v3____")

from math import sqrt # Racine carré

def est_un_nombre_premier(un_nombre):
    un_nombre = int(un_nombre) # Doit être un entier
    if un_nombre % (DEUX := 2) == 0:
        return (un_nombre == DEUX)
    for diviseur in range(DEUX + 1, int(sqrt(un_nombre)) + 1, DEUX): # Optimisation
        if un_nombre % diviseur == 0:
            return False
    return True

# Affiche un nombre avec un espace comme séparateur de milliers
afficher_nombre = lambda nombre: format(nombre,'_').replace('_',' ')

le_nombre = 1
compteur = 0
# Étape n°1
print("Liste des", limite := 1000, "premiers nombres premiers :")
while compteur < limite:
    le_nombre += 1
    if est_un_nombre_premier(le_nombre):
        compteur += 1
        print(" • n°", afficher_nombre(compteur), ":", afficher_nombre(le_nombre))
    if compteur == limite: # Étape n°2
        limite = int(input("Indiquer une nouvelle limite pour continuer : "))

print("_________________________Fin du programme")
