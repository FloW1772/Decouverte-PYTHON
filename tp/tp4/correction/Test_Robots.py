from Modele.Aspirateur import Aspirateur, AspirateurRobot
from Modele.Robot import Robot
from Modele.RobotMobile import RobotMobile

r1 = Robot()
r2 = Robot("Mécanique")
r3 = Robot("Electrique")

print("------------------------------------")
print("------- TP : PREMIERE PARTIE -------")
print("------------------------------------")

print("-------- CREATION DE ROBOTS --------")
print(r1)
print('_'*36)
print(r2)
print('_'*36)
print(r3)
print('_'*36)
print("Nombre de robots créés au total : ", Robot.nb_robot)
print("------------------------------------")

print("--------- TEST SETTER TYPE ---------")
r4 = Robot("T")  # Doit afficher un message d'erreur
print(r4)  # Doit afficher un type Générique
print('_'*36)
r2.robot_type = "K"  # Doit afficher un message d'erreur
print(r2)  # Le type ne doit pas avoir été modifié
print("------------------------------------")

print("--------- TEST STATUT ---------")
r2.statut = 2
print(r2)
print('_'*36)
r2.statut = 5  # Doit afficher un message d'erreur
print(r2)  # Le statut ne doit pas avoir été modifié
print("------------------------------------")

print("--------- TEST TOURNER ---------")
r3.tourner(1)
print(r3)
print('_'*36)
r3.tourner(-1)
print(r3)
print('_'*36)
r3.tourner(12)  # Doit afficher un message d'erreur
print(r3)  # Le robot ne doit pas avoir tourné
print("------------------------------------")

print("------------------------------------")
print("------- TP : DEUXIEME PARTIE -------")
print("------------------------------------")

r5 = RobotMobile()
r6 = RobotMobile(ord=4)
r7 = RobotMobile(robot_type="Electronique", abs=2, ord=5)

print("---- CREATION DE ROBOTS MOBILES ----")
print(r5)
print('_'*36)
print(r6)
print('_'*36)
print(r7)
print('_'*36)
print("Nombre de robots créés au total : ", Robot.nb_robot)
print("------------------------------------")

print("--- DEPLACEMENT DE ROBOTS MOBILES --")
print(r5.afficher_position())
r5.avancer(4)
print(r5.afficher_position())
print('_'*36)
print(r6.afficher_position())
r6.tourner(1)
r6.avancer(4)
print(r6.afficher_position())
print('_'*36)
print(r7.afficher_position())
r7.tourner(-1)
r7.avancer(6)
print(r7.afficher_position())
print("------------------------------------")

print("------------------------------------")
print("------- TP : TROISIEME PARTIE ------")
print("------------------------------------")

print("----- CREATION D'UN ASPIRATEUR -----")
a1 = Aspirateur('Rowenta', 4500)
print(a1)
print("------------------------------------")

print("--- CREATION D'UN ASPIRATEUR ROBOT --")
ar1 = AspirateurRobot('Rowenta', 4500, 115)
print(ar1)
print("------------------------------------")

print("--- TEST PARCOURS --")
ar1.parcours(10, 15)
print("------------------------------------")
