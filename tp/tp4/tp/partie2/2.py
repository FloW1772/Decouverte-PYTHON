from Modele.Robot import Robot

class RobotMobile(Robot):
    def __init__(self, robot_type="Générique", abscisse=0, ordonnee=0):
        super().__init__(robot_type)
        self._abscisse = abscisse
        self._ordonnee = ordonnee

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
