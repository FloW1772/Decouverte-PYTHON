# TP Cryptage poly-alphabétique (table de VIGENÈRE)
SEPARATEUR, FIN, LIMITE = '_', '=', 80
print("Cryptage Poly-Alphabétique v4".center(LIMITE, SEPARATEUR))
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Définitions des méthodes :
def generer_matrice(une_trame=ALPHABET):
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

def cryptage_polyalpabetique(un_message, une_clef, inverse=False, une_trame=ALPHABET):
    """Mécanisme de chiffrage (par défaut) ou de déchiffrage avec le paramètre 'inverse=True', 
    d'un message avec une clef pour d'obtenir le message secret en fonction, 
    à l'aide pseudo matrice constituée de toutes les lettres de l'alphabet."""
    # Normalisation par précaution
    un_message = normaliser(un_message)
    une_clef = normaliser(une_clef, ' ')
    sequence = normaliser(une_trame) # Récupération de la séquence pour identifier les positions des lettres
    max_sequence = len(sequence) # nombre de lettres de la sequence, à ne pas dépasser
    max_clef = len(une_clef) # nombre de lettres de la clef, à ne pas dépasser
    index_clef = max_clef # Initialisation de la position de la lettre clef
    le_message_secret = "" # Initialisation du message à chiffrer
    for lettre in un_message: # parcours de la phase lettre par lettre
        lettre_secrete = lettre # Conservation du caractère de depart par défaut
        if index_clef >= max_clef: index_clef *= 0 # remise sur la première lettre de la clef
        lettre_clef = une_clef[index_clef]
        if sequence.count(lettre): # Vérification de la présence de la lettre dans la séquence
            index_ligne = sequence.index(lettre_clef)
            index_lettre = sequence.index(lettre)
            index_secret = index_ligne + index_lettre
            if inverse: index_secret = max_sequence - index_ligne + index_lettre
            if index_secret >= max_sequence: index_secret -= max_sequence
            lettre_secrete = sequence[index_secret]
            index_clef += 1 # incrémentation de la position de la lettre de la clef
        le_message_secret += lettre_secrete
    return le_message_secret # Retourne en fonction la phrase codée ou en clair

# Constantes pour les exemples par défaut :
MESSAGE_CLAIR = "ON DEBARQUE DEMAIN SUR LA PLAGE"
CLEF_CHIFFRAGE = "OMAHA"
VERIFICATION_1 = "CZ DLBODQBE RQMHIB EUY LO BLHGS"

MESSAGE_SECRET = "RXUIYEMFR : JP J LYIE EID ESLVJWEPW !"
CLEF_DECHIFFRAGE = "REBELLE"
VERIFICATION_2 = "ATTENTION : IL Y AURA DES TOURISTES !"

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

afficher_resultat("Message original", message_clair := MESSAGE_CLAIR)
afficher_resultat("Clef de chiffrage", clef := CLEF_CHIFFRAGE)
afficher_resultat("Message chiffré", resultat := chiffrer_message(message_clair, clef))
print("Cryptage :", ("Erreur !","Ok")[resultat == VERIFICATION_1])

afficher_resultat("Message à déchiffrer", message_secret := MESSAGE_SECRET)
afficher_resultat("Clef de déchiffrage", clef := CLEF_DECHIFFRAGE)
afficher_resultat("Message déchiffré", resultat := dechiffrer_message(message_secret, clef))
print("Décryptage :", ("Erreur !","Ok")[resultat == VERIFICATION_2])

print((FIN * LIMITE) + "Fin du programme")