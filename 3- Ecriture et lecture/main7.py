import chardet

# Bloc 1: Traitement de "fichier_latin1.txt"
# Lecture initiale des données binaires
with open("fichier_latin1.txt", "rb") as f:
    print(f.read())

    # Détection de l'encodage
    f.seek(0)
    encoding = chardet.detect(f.read())['encoding']
    print(encoding)

    # Décodage et affichage du contenu
    f.seek(0)
    content = f.read().decode(encoding)
    print(content)

# Bloc 2: Manipulation de "fichier.txt"
# L'utilisation de 'r+' pour l'ouverture permet la lecture et l'écriture,
# mais il est crucial de noter que l'écriture peut avoir des effets
# inattendus si le fichier n'est pas géré avec précaution (ex: troncature).
with open('fichier.txt', 'r+') as f:
    print(f.tell())
    print(f.read())
    print(f.tell())

    # Écriture à une position spécifique
    f.seek(4)
    f.write('-Fred-')

    # Retour au début et lecture du contenu modifié
    f.seek(0)
    print(f.read())