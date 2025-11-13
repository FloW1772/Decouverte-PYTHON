import random
import string

class Robot:
    # Attributs de classe
    orientations_possibles = ["NORD", "EST", "SUD", "OUEST"]
    statuts_possibles = {1: "EN SERVICE", 2: "HORS SERVICE", 3: "EN RÉPARATION"}
    nb_robot = 0  # correspond au test

    def __init__(self, robot_type="Générique"):
        self._robot_type = "Générique"
        self.robot_type = robot_type  # Utilise le setter pour validation
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
