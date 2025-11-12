# ============================================================
# Programme : Chiffrement et Déchiffrement Vigenère
# Niveaux : Essentiel / Attendu / Avancé
# ============================================================

import unicodedata

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# ------------------------------
# NIVEAU 1 — Génération de la matrice
# ------------------------------
def generate_matrix():
    """Génère la matrice Vigenère (26 alphabets décalés)."""
    matrix = []
    for i in range(26):
        row = ALPHABET[i:] + ALPHABET[:i]
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    """Affiche la matrice de chiffrement."""
    print("   " + " ".join(ALPHABET))
    for i, row in enumerate(matrix):
        print(f"{ALPHABET[i]}  " + " ".join(row))


# ------------------------------
# Fonctions utilitaires
# ------------------------------
def normalize(text):
    """Normalise le texte :
       - Passe en majuscules
       - Supprime les accents
       - Ne garde que les lettres et espaces
    """
    nfkd = unicodedata.normalize('NFKD', text)
    no_accents = "".join([c for c in nfkd if not unicodedata.combining(c)])
    up = no_accents.upper()
    filtered = "".join([c if ('A' <= c <= 'Z' or c == ' ') else '' for c in up])
    return " ".join(filtered.split())


def repeat_key_over_message(key, message):
    """Répète la clef sur le message en respectant les espaces."""
    key = key.upper()
    res = []
    i = 0
    for ch in message:
        if 'A' <= ch <= 'Z':
            res.append(key[i % len(key)])
            i += 1
        else:
            res.append(' ')
    return "".join(res)


# ------------------------------
# NIVEAU 2 — Chiffrement
# ------------------------------
def encrypt_vigenere(message, key):
    """Chiffre un message avec la clef donnée."""
    message = normalize(message)
    key_seq = repeat_key_over_message(key, message)
    cipher = []
    for m, k in zip(message, key_seq):
        if 'A' <= m <= 'Z':
            shift = ord(k) - ord('A')
            c = chr((ord(m) - ord('A') + shift) % 26 + ord('A'))
            cipher.append(c)
        else:
            cipher.append(m)
    return "".join(cipher), key_seq


# ------------------------------
# NIVEAU 3 — Déchiffrement
# ------------------------------
def decrypt_vigenere(ciphertext, key):
    """Déchiffre un message chiffré avec la clef donnée."""
    ciphertext = ciphertext.upper()
    key_seq = repeat_key_over_message(key, ciphertext)
    plain = []
    for c, k in zip(ciphertext, key_seq):
        if 'A' <= c <= 'Z':
            shift = ord(k) - ord('A')
            m = chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
            plain.append(m)
        else:
            plain.append(c)
    return "".join(plain), key_seq


# ------------------------------
# Programme principal (menu)
# ------------------------------
def main():
    print("=== Programme de chiffrement Vigenère ===\n")
    print("1. Afficher la matrice")
    print("2. Chiffrer un message")
    print("3. Déchiffrer un message")
    print("4. Quitter\n")

    while True:
        choix = input("Choisissez une option (1-4) : ").strip()

        if choix == "1":
            print("\n--- MATRICE DE CHIFFREMENT ---\n")
            print_matrix(generate_matrix())
            print()

        elif choix == "2":
            message = input("Message à chiffrer : ")
            key = input("Clef (4 à 16 caractères) : ").strip().upper()
            if len(key) < 4 or len(key) > 16:
                print("⚠️ La clef doit contenir entre 4 et 16 caractères.\n")
                continue
            cipher, rep_key = encrypt_vigenere(message, key)
            print("\n--- RÉSULTAT DU CHIFFREMENT ---")
            print(f"Message normalisé : {normalize(message)}")
            print(f"Répétition clef : {rep_key}")
            print(f"Message chiffré : {cipher}\n")

        elif choix == "3":
            cipher = input("Message à déchiffrer : ")
            key = input("Clef (4 à 16 caractères) : ").strip().upper()
            if len(key) < 4 or len(key) > 16:
                print("⚠️ La clef doit contenir entre 4 et 16 caractères.\n")
                continue
            plain, rep_key = decrypt_vigenere(cipher, key)
            print("\n--- RÉSULTAT DU DÉCHIFFREMENT ---")
            print(f"Répétition clef : {rep_key}")
            print(f"Message déchiffré : {plain}\n")

        elif choix == "4":
            print("Fin du programme. 👋")
            break

        else:
            print("Choix invalide, réessayez.\n")


# ------------------------------
# Point d'entrée
# ------------------------------
if __name__ == "__main__":
    main()
