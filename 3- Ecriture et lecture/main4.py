import chardet

# Ouvrir le fichier en mode binaire pour détecter l'encodage
with open("fichier_unicode.txt", "rb") as f:
    # Lire tout le contenu du fichier binaire et détecter l'encodage
    encoding = chardet.detect(f.read())['encoding']

# Ouvrir à nouveau le fichier en mode texte, en utilisant l'encodage détecté
with open("fichier_unicode.txt", "r", encoding=encoding) as f:
    # Lire et afficher le contenu décodé
    print(f.read())