from Modele.RobotMobile import RobotMobile


class Aspirateur:

    def __init__(self, marque, puissance):
        self.marque = marque
        self.puissance = puissance

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
        return "Aspirateur {}, puissance={}W".format(self._marque, self._puissance)


class AspirateurRobot(RobotMobile, Aspirateur):
    def __init__(self, marque, puissance, distance_max):
        Aspirateur.__init__(self, marque, puissance)
        RobotMobile.__init__(self, robot_type="Aspirateur Robot")
        self.distance_max = distance_max

    @property
    def distance_max(self):
        return self._distance_max

    @distance_max.setter
    def distance_max(self, value):
        self._distance_max = value

    def __str__(self):
        return RobotMobile.__str__(self) + "\nPuissance : {}W".format(self._puissance)

    def parcours(self, abs_max, ord_max):
        grid = [['-' for i in range(abs_max)] for j in range(ord_max)]
        grid[0][0] = "*"
        # Se diriger vers l'Est
        while self.orientation != 'EST':
            self.tourner(1)
        distance = 0

        while distance < self._distance_max and self.abs < abs_max and self.ord < ord_max:
            self.avancer(1)
            distance += 1
            grid[self.ord][self.abs] = '*'
            # En bout de ligne on va vers le SUD puis l'OUEST
            if self._abs == abs_max - 1:
                self.tourner(-1)
                if distance < self._distance_max and self.abs < abs_max and self.ord < ord_max:
                    self.avancer(1)
                    distance += 1
                    grid[self.ord][self.abs] = '*'
                    self.tourner(-1)
            # En début de ligne on va vers le SUD puis l'EST
            if self._abs == 0:
                self.tourner(1)
                if distance < self._distance_max and self.abs < abs_max and self.ord < ord_max:
                    self.avancer(1)
                    distance += 1
                    grid[self.ord][self.abs] = '*'
                    self.tourner(1)

        # Affichage du parcours
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                print(grid[i][j], end='')
            print()
