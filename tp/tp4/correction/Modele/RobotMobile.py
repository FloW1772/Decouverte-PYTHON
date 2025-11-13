from Modele.Robot import Robot


class RobotMobile(Robot):
    def __init__(self, robot_type='Générique', abs=0, ord=0):
        Robot.__init__(self, robot_type)
        self._abs = abs
        self._ord = ord

    @property
    def abs(self):
        return self._abs

    @property
    def ord(self):
        return self._ord

    def afficher_position(self):
        return 'Position : [abs={} ; ord={}]'.format(self.abs, self.ord)

    def avancer(self, value):
        if self.orientation == "EST":
            self._abs += value
        elif self.orientation == "OUEST":
            self._abs -= value
        elif self.orientation == "NORD":
            self._ord += value
        else:
            self._ord -= value

    def __str__(self):
        return Robot.__str__(self) + "\n" + self.afficher_position()