with open("fichier_latin1.txt", "r") as f:
    content = f.read()

print(content)

with open("fichier_unicode.txt", "r", encoding='utf-8') as f:
    content = f.read()

print(content)