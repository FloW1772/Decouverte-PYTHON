import chardet

with open("fichier_unicode.txt", "rb") as f:
    print(chardet.detect(f.read()))