import random
import string


class Robot:
    nb_robot = 0
    ORIENTATIONS = ["NORD", "EST", "SUD", "OUEST"]
    STATUTS = {1: "En service", 2: "Hors Service", 3: " En réparation"}
    DEFAULT_TYPE = "Générique"

    def __init__(self, robot_type=DEFAULT_TYPE):
        self.robot_type = robot_type
        self._numero_serie = ''.join([random.choice(string.ascii_uppercase) for i in range(2)]) \
                             + ("%4d" % random.randint(0, 1000000000))
        self._orientation = Robot.ORIENTATIONS[0]
        self._statut = 1

        Robot.nb_robot += 1

    @property
    def robot_type(self):
        return self._robot_type

    @robot_type.setter
    def robot_type(self, value):
        if len(value) >= 2:
            self._robot_type = value
        else:
            self._robot_type = Robot.DEFAULT_TYPE
            print("Le type du robot doit comporter au minimum 2 caractères.")

    @property
    def numero_serie(self):
        return self._numero_serie

    @property
    def orientation(self):
        return self._orientation

    @property
    def statut(self):
        return self.statut

    @statut.setter
    def statut(self, value):
        if value in Robot.STATUTS.keys():
            self._statut = value
        else:
            self._robot_type = Robot.DEFAULT_TYPE
            print("Statut invalide ! Valeurs acceptées : ", Robot.STATUTS)

    def __str__(self):
        return "Robot {} - {}\nStatut : {}\nOrientation : {}".format(self._numero_serie, self._robot_type, Robot.STATUTS[self._statut],
                                                                     self._orientation)

    def tourner(self, value):
        if value in [1, -1]:
            self._orientation = Robot.ORIENTATIONS[(Robot.ORIENTATIONS.index(self._orientation) + value)%len(Robot.ORIENTATIONS)]
        else:
            print("Un robot peut tourner de 1 ou de -1.")
