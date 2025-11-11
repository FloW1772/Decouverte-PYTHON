# Étape 2 : Saisie de la limite supérieure

# On demande la limite à l'utilisateur
limite = int(input("Entrez la limite supérieure de recherche : "))

for nombre in range(2, limite + 1):
    est_premier = True
    for diviseur in range(2, int(nombre ** 0.5) + 1):
        if nombre % diviseur == 0:
            est_premier = False
            break
    if est_premier:
        print(nombre)
