import chardet

with open("fichier_latin1.txt", "rb") as f:
    print(f.read())
    f.seek(0)
    encoding = chardet.detect(f.read())['encoding']
    f.seek(0)
    content = f.read().decode(encoding)
    print(content)

#with open("fichier_unicode.txt", "r", encoding=encoding) as f:
#    print(f.read())