import random
import string

# ----------------- Classe Robot -----------------
class Robot:
    orientations_possibles = ["NORD", "EST", "SUD", "OUEST"]
    statuts_possibles = {1: "EN SERVICE", 2: "HORS SERVICE", 3: "EN RÉPARATION"}
    nb_robot = 0  # compteur de robots

    def __init__(self, robot_type="Générique"):
        self._robot_type = "Générique"
        self.robot_type = robot_type
        self._numero_serie = self._generer_numero_serie()
        self._orientation = "NORD"
        self._statut = 1
        Robot.nb_robot += 1

    @property
    def robot_type(self):
        return self._robot_type

    @robot_type.setter
    def robot_type(self, value):
        if isinstance(value, str) and len(value) >= 2:
            self._robot_type = value
        else:
            print("Erreur : le type de robot doit contenir au moins 2 caractères. Valeur par défaut utilisée.")
            self._robot_type = "Générique"

    @property
    def numero_serie(self):
        return self._numero_serie

    def _generer_numero_serie(self):
        lettres = ''.join(random.choices(string.ascii_uppercase, k=2))
        chiffres = str(random.randint(0, 999999999)).zfill(10)
        return lettres + chiffres

    @property
    def orientation(self):
        return self._orientation

    def tourner(self, direction):
        if direction not in [1, -1]:
            print("Erreur : la direction doit être 1 (horaire) ou -1 (anti-horaire).")
            return
        idx = Robot.orientations_possibles.index(self._orientation)
        idx = (idx + direction) % len(Robot.orientations_possibles)
        self._orientation = Robot.orientations_possibles[idx]

    @property
    def statut(self):
        return self._statut

    @statut.setter
    def statut(self, value):
        if value in Robot.statuts_possibles:
            self._statut = value
        else:
            print("Erreur : statut invalide. Valeurs possibles : 1, 2, 3.")

    def __str__(self):
        return f"Robot {self.numero_serie} – {self.robot_type}\nOrientation : {self.orientation}"

# ----------------- Classe RobotMobile -----------------
class RobotMobile(Robot):
    def __init__(self, robot_type="Générique", abs=0, ord=0):
        super().__init__(robot_type)
        self._abscisse = abs  # correspond à "abs" dans le test
        self._ordonnee = ord  # correspond à "ord" dans le test

    @property
    def abscisse(self):
        return self._abscisse

    @property
    def ordonnee(self):
        return self._ordonnee

    def afficher_position(self):
        return f"Position : [abs={self.abscisse} ; ord={self.ordonnee}]"

    def avancer(self, m):
        if self.orientation == "EST":
            self._abscisse += m
        elif self.orientation == "OUEST":
            self._abscisse -= m
        elif self.orientation == "NORD":
            self._ordonnee += m
        elif self.orientation == "SUD":
            self._ordonnee -= m

    def __str__(self):
        parent = super().__str__()
        return f"{parent}\nStatut : {Robot.statuts_possibles[self.statut]}\n{self.afficher_position()}"

# ----------------- Classe Aspirateur -----------------
class Aspirateur:
    def __init__(self, marque, puissance):
        self._marque = marque
        self._puissance = puissance

    @property
    def marque(self):
        return self._marque

    @marque.setter
    def marque(self, value):
        self._marque = value

    @property
    def puissance(self):
        return self._puissance

    @puissance.setter
    def puissance(self, value):
        self._puissance = value

    def __str__(self):
        return f"Aspirateur {self.marque}, puissance={self.puissance}W"

# ----------------- Classe AspirateurRobot -----------------
class AspirateurRobot(Aspirateur, RobotMobile):
    def __init__(self, marque, puissance, distance_max):
        RobotMobile.__init__(self, robot_type="Aspirateur robot", abs=0, ord=0)
        Aspirateur.__init__(self, marque, puissance)
        self._distance_max = distance_max

    @property
    def distance_max(self):
        return self._distance_max

    @distance_max.setter
    def distance_max(self, value):
        self._distance_max = value

    def __str__(self):
        parent_robot = RobotMobile.__str__(self)
        return f"{parent_robot}\nMarque : {self.marque}\nPuissance : {self.puissance}W"

    # BONUS : méthode parcours
    def parcours(self, largeur, longueur):
        x, y = 0, 0
        direction_x = 1
        distance_parcourue = 0

        piece = [['-' for _ in range(largeur)] for _ in range(longueur)]

        while y < longueur and distance_parcourue < self.distance_max:
            while 0 <= x < largeur and distance_parcourue < self.distance_max:
                piece[y][x] = '*'
                x += direction_x
                distance_parcourue += 1
            x -= direction_x
            direction_x *= -1
            y += 1

        for ligne in piece:
            print(''.join(ligne))
