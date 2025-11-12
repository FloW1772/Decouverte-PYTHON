# TP Cryptage poly-alphabétique (table de VIGENÈRE)
SEPARATEUR, FIN, LIMITE = '_', '=', 80
print("Cryptage Poly-Alphabétique v3".center(LIMITE, SEPARATEUR))

# Définitions des méthodes :

def generer_matrice(une_trame="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    """Génération de la matrice en fonction d'une trame,
     consituée de toutes les lettres de l'alphabet."""
    la_matrice = [] # Création d'une matrice vide
    for i in range(len(une_trame)):
        la_matrice.append(list(une_trame))
        une_trame = une_trame[1:] + une_trame[0]
    return la_matrice

def afficher_matrice(une_matrice, nb_sepa_horizontal=2, prefixe=""):
    """Affichage d'une matrice avec la gestion d'un séparateur d'élément,
     et d'un préfixe pour chaque ligne"""
    dimension = len(une_matrice)
    for ligne in range(dimension):
        trame = prefixe # Getsion du préfixe
        for colonne in range(dimension):
            trame += une_matrice[ligne][colonne]
            if colonne < dimension: trame += ' ' * nb_sepa_horizontal # Gestion du séparateur
        print(trame)

def normaliser(une_chaine, supprimer=""):
    """Normalisation d'une chaîne de caractère poursupprimer les accents,
     avec en option la suppression d'autres caractères non autorisés."""
    normalisee = str(une_chaine).strip().upper()
    transformation = str.maketrans(  
        "ÀÄÂÉÈËÊÏÎÖÔÙÜÛŸŶÇ", # Caractère à modifier 
        "AAAEEEEIIOOUUUYYC" # Caractères à remplacer 
        )
    normalisee = normalisee.translate(transformation)
    ligatures = str.maketrans({'Æ':"AE", 'Œ':"OE"})
    normalisee = normalisee.translate(ligatures)
    return normalisee

def cryptage_polyalpabetique(un_message, une_clef, inverse=False):
    """Mécanisme de chiffrage (par défaut) ou de déchiffrage avec le paramètre 'inverse=True', 
    d'un message avec une clef pour d'obtenir le message secret en fonction, 
    à l'aide d'une matrice constituée de toutes les lettres de l'alphabet."""
    la_matrice = generer_matrice() # Génération de la matrice
    sequence = la_matrice[0] # Récupération de la séquence pour identifier les positions des lettres

    # Normalisation par précaution
    un_message = normaliser(un_message)
    une_clef = normaliser(une_clef, ' ')

    index_clef = len(une_clef) # Initialisation de la position de la lettre clef
    le_message_secret = "" # Initialisation du message à chiffrer
    for lettre in un_message: # parcours de la phase lettre par lettre
        lettre_secrete = lettre # Conservation du caractère de depart par défaut
        if index_clef >= len(une_clef): index_clef *= 0 # remise sur la première lettre de la clef
        lettre_clef = une_clef[index_clef]
        if sequence.count(lettre): # Vérification de la présence de la lettre dans la séquence
            index_ligne = sequence.index(lettre_clef)
            if inverse: # Détermination de la lettre d'origine (Déchiffrage)
                index_colonne = la_matrice[index_ligne].index(lettre)
                lettre_secrete = sequence[index_colonne]
            else: # Détermination de la lettre chiffrée (Chiffrage)
                index_colonne = sequence.index(lettre)
                lettre_secrete = la_matrice[index_ligne][index_colonne]
            index_clef += 1 # incrémentation de la position de la lettre de la clef
        le_message_secret += lettre_secrete
    return le_message_secret # Retourne en fonction la phrase codée ou en clair


# Constantes pour les exemples par défaut :
MESSAGE_CLAIR = "ON DEBARQUE DEMAIN SUR LA PLAGE"
CLEF_CHIFFRAGE = "OMAHA"
MESSAGE_SECRET = "RXUIYEMFR : JP J LYIE EID ESLVJWEPW !"
CLEF_DECHIFFRAGE = "REBELLE"

# Fonctions Lambda :
separation = lambda nombre=LIMITE: print(SEPARATEUR * LIMITE)
pause = lambda : input((SEPARATEUR * (LIMITE // 2)) + "Appuyer sur 'Entrée' pour continuer…")
saisir_message = lambda message, message_defaut: normaliser(input("\n - {} :\n".format(message)) or message_defaut)
saisir_phrase = lambda verbe, phrase_defaut: saisir_message("Saisir votre message à {} ci-dessous".format(verbe), phrase_defaut)
saisir_clef = lambda clef_defaut: saisir_message("Saisir la clef (4 ou 16 lettres)", clef_defaut)
afficher_resultat = lambda message, valeur: print("\t • {} : {}".format(message, valeur))

chiffrer_message = lambda un_message, une_clef: cryptage_polyalpabetique(un_message, une_clef, False)
dechiffrer_message = lambda un_message, une_clef: cryptage_polyalpabetique(un_message, une_clef, True)

# Exécution du programme :
print("\nGénération et affichage de la table de VIGENÈRE :")
separation()
table_vigenere = generer_matrice()
afficher_matrice(table_vigenere)

pause()
message_clair = saisir_phrase("chiffrer", MESSAGE_CLAIR)
afficher_resultat("Message original", message_clair)
clef = saisir_clef(CLEF_CHIFFRAGE)
afficher_resultat("Clef de chiffrage", clef)
afficher_resultat("Message chiffré", chiffrer_message(message_clair, clef))

pause()
message_secret = saisir_phrase("déchiffrer", MESSAGE_SECRET)
afficher_resultat("Message à déchiffrer", message_secret)
clef = saisir_clef(CLEF_DECHIFFRAGE)
afficher_resultat("Clef de déchiffrage", clef)
afficher_resultat("Message déchiffré", dechiffrer_message(message_secret, clef))

print((FIN * LIMITE) + "Fin du programme")