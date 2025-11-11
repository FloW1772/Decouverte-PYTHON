# ---------------------------------------------
# NOMBRES PREMIERS - Étape 1 et Étape 2
# ---------------------------------------------
# Étape 1 : Afficher les nombres premiers entre 0 et 1000
# Étape 2 : Permettre à l'utilisateur de choisir la limite de recherche
# ---------------------------------------------

# --- Étape 1 ---
print("=== Étape 1 : Nombres premiers entre 0 et 1000 ===")

for nombre in range(2, 1001):
    est_premier = True
    for diviseur in range(2, int(nombre ** 0.5) + 1):
        if nombre % diviseur == 0:
            est_premier = False
            break
    if est_premier:
        print(nombre, end=" ")

print("\n")  # Saut de ligne après la liste

# --- Étape 2 ---
print("=== Étape 2 : Nombres premiers jusqu'à une limite choisie ===")

# Demande de la limite à l'utilisateur
limite = int(input("Entrez la limite supérieure de recherche : "))

print(f"Nombres premiers entre 0 et {limite} :")

for nombre in range(2, limite + 1):
    est_premier = True
    for diviseur in range(2, int(nombre ** 0.5) + 1):
        if nombre % diviseur == 0:
            est_premier = False
            break
    if est_premier:
        print(nombre, end=" ")

print("\n=== Fin du programme ===")
