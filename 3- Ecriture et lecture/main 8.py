import chardet

# Lecture et détection de l'encodage du fichier
with open("fichier_latin1.txt", "rb") as f:
    # Lecture initiale pour la démo, mais cela déplace le pointeur
    print(f.read())

    # Remise du pointeur au début
    f.seek(0)

    # Détection de l'encodage
    encoding = chardet.detect(f.read())['encoding']
    print(encoding)

    # Remise du pointeur au début pour décoder
    f.seek(0)

    # Lecture, décodage et affichage du contenu
    content = f.read().decode(encoding)
    print(content)

# Écriture dans un nouveau fichier
with open("fichier.txt", 'a', newline='\n') as f:
    f.writelines(['contenu', 'contenu'])