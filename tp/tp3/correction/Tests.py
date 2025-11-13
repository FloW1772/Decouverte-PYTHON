from Intervalle import Intervalle

# Question 1
inter_1 = Intervalle(5, 12)
inter_2 = Intervalle(44, 13)

# Question 2 : vérifiez qu'à l'affichage, pour inter_2, les bornes ont été remises dans l'ordre par le constructeur
print('Question 2 - Affichage des intervalles')
print('Affichage de l\'intervalle 1')
print(inter_1)
print('Affichage de l\'intervalle 2')
print(inter_2)
print('----------------\n')

# Question 3 : vérifier que cette ligne génère une erreur. Commentez-là avant de passer aux questions suivantes
# print('Affichage de l\'intervalle 1')
# print(inter_1.__borne_min)
# print('Affichage de l\'intervalle 2')
# print(inter_2.__borne_max)

# Question 4
print('Question 4 - Setters pour les bornes min et max')
print("Modification de la borne min de l'intervalle 1 : ")
inter_1.set_borne_min(6)
print(inter_1)

print("Modification de la borne max de l'intervalle 2 : ")
inter_2.set_borne_max(20)
print(inter_2)

print("Modification de la borne max de l'intervalle 1 : ")
inter_1.set_borne_max(1) # Doit générer un message d'erreur
print(inter_1)  # Les bornes n'ont pas été modifiées

print("Modification de la borne min de l'intervalle 2 : ")
inter_2.set_borne_min(25)  # Doit générer un message d'erreur
print(inter_2)  # Les bornes n'ont pas été modifiées

print('----------------\n')

# Question 5
print('Question 5 - Getters pour les bornes min et max')
print('Borne min de l\'intervalle 1 : ', inter_1.get_borne_min())
print('Borne max de l\'intervalle 2 : ', inter_2.get_borne_max())

print('----------------\n')

# Question 6
print('Question 6 - Addition de deux intervalles')
inter_3 = inter_1 + inter_2 # inter_3 = inter_1.__add__(inter_2)
print("Addition des deux intervalles : ", inter_1, "+", inter_2, "=", inter_3)
print('----------------\n')

# Question 7
print('Question 7 - Intersection de deux intervalles')
print(inter_1, "∩", inter_2, "=", inter_1.intersection(inter_2))
print(inter_2, "∩", inter_1, "=", inter_2.intersection(inter_1))
print(inter_2, "∩", inter_3, "=", inter_2.intersection(inter_3))
print(inter_3, "∩", inter_2, "=", inter_3.intersection(inter_2))
print('----------------\n')

# Question 8
print('Question 8 - Union de deux intervalles')
print(inter_1, "⋃", inter_2, "=", inter_1.union(inter_2))
print(inter_2, "⋃", inter_1, "=", inter_2.union(inter_1))
print(inter_2, "⋃", inter_3, "=", inter_2.union(inter_3))
print(inter_3, "⋃", inter_2, "=", inter_3.union(inter_2))
print('----------------\n')
