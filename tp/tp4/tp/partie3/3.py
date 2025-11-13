from Modele.RobotMobile import RobotMobile

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


class AspirateurRobot(Aspirateur, RobotMobile):
    def __init__(self, marque, puissance, distance_max):
        RobotMobile.__init__(self, robot_type="Aspirateur robot", abscisse=0, ordonnee=0)
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

    # Méthode pour simuler le parcours de l’aspirateur
    def parcours(self, largeur, longueur):
        x, y = 0, 0
        direction_x = 1  # 1 = droite, -1 = gauche
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
