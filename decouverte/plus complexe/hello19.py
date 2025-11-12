s = "Ceci est une chaîne de caractères avec €"

print(type(s))

b = s.encode("iso8859-15")

print(type(b))

print(b.decode("utf-8"))