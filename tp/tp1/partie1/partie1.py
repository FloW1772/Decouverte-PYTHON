# Étape 1 : Afficher les nombres premiers entre 0 et 1000

for nombre in range(2, 1001):  # On commence à 2 car 0 et 1 ne sont pas premiers
    est_premier = True
    for diviseur in range(2, int(nombre ** 0.5) + 1):  # Optimisation : on teste jusqu’à √nombre
        if nombre % diviseur == 0:
            est_premier = False
            break
    if est_premier:
        print(nombre)
