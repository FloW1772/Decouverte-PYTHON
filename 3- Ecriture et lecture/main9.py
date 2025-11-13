import pickle

# Listes à enregistrer
animaux = ['chat', 'chien', 'pingouin']
fruits = ['pomme', 'poire', 'banane']
monuments = ['Tour Eiffel', 'Mont Saint-Michel', 'Machu Pichu']

# Écriture dans un fichier binaire
with open("test.p", "wb") as f:
    pickle.dump(animaux, f)
    pickle.dump(fruits, f)
    pickle.dump(monuments, f)

# Lecture du fichier binaire
with open("test.p", "rb") as f:
    anim = pickle.load(f)
    fr = pickle.load(f)
    mon = pickle.load(f)

# Affichage du contenu
print(anim, fr, mon)
