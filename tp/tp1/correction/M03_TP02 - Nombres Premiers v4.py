# TP06 - Nombres Premiers
print("____Nombres Premiers v4____")

def est_un_nombre_premier_v1(un_nombre):
    un_nombre = int(un_nombre) # Doit être un entier
    for diviseur in range(un_nombre):
        if diviseur < 2: continue
        if un_nombre % diviseur == 0:
            return False
    return True

def est_un_nombre_premier_v2(un_nombre):
    un_nombre = int(un_nombre) # Doit être un entier
    if un_nombre % (DEUX := 2) == 0:  # Optimisation : Tester la parité du nombre
        return (un_nombre == DEUX)
    for diviseur in range(DEUX + 1, un_nombre, DEUX):  # Optimisation : De 3 jusqu'au Nombre (exclu) avec un pas de 2
        if un_nombre % diviseur == 0:
            return False
    return True

from math import sqrt # Racine carré
def est_un_nombre_premier_v3(un_nombre):
    un_nombre = int(un_nombre) # Doit être un entier
    if un_nombre % (DEUX := 2) == 0:
        return (un_nombre == DEUX)
    for diviseur in range(DEUX + 1, int(sqrt(un_nombre)) + 1, DEUX): # Optimisation
        if un_nombre % diviseur == 0:
            return False
    return True

# Affiche un nombre avec un espace comme séparateur de milliers
afficher_nombre = lambda nombre: format(nombre,'_').replace('_',' ')

# Chronomètre
from time import time, localtime, sleep
CHRONOMETRE, CHRONO_PATTERN = [], "\t • %s"
def init_chrono(message="Chronomètre: Reset"):
    CHRONOMETRE.clear()
    print(CHRONO_PATTERN % message)

def top_chrono(message="Top Chrono..."):
    CHRONOMETRE.append(time())
    print(CHRONO_PATTERN % message)

def stop_chrono(message="STOP Chrono !"):
    top_chrono(message)

def delta_chrono(message="Chrono: Delta = %s"):
    chrono_delta = 0
    for i in range(0, len(CHRONOMETRE), 2):  # Somme des intervalles de temps passées
        chrono_delta += CHRONOMETRE[i+1] - CHRONOMETRE[i]
    texte_chrono = "{0:02}:{1:02}.{2:03}".format(
        localtime(chrono_delta)[4],
        localtime(chrono_delta)[5],
        int(1000 * (chrono_delta - int(chrono_delta))))
    print(CHRONO_PATTERN % message % texte_chrono)
    return texte_chrono

init_chrono()
le_nombre = 1
compteur = 0
# Étape n°1
print("Liste des", limite := 10000, "premiers nombres premiers :")

top_chrono()
while compteur < limite:
    le_nombre += 1
    if est_un_nombre_premier_v3(le_nombre):
        compteur += 1
        print(" • n°", afficher_nombre(compteur), ":", afficher_nombre(le_nombre))
    if compteur == limite: # Étape n°2
        stop_chrono()
        delta_chrono()
        limite = int(input("Indiquer une nouvelle limite pour continuer : ") or 0)
        top_chrono()  # Relance du chronomètre

stop_chrono()
print("_________________________Fin du programme")
