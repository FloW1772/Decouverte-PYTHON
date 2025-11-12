# =========================================
# 1. Création de la classe Intervalle
# =========================================
class Intervalle:
    def __init__(self, borne_min, borne_max):
        # Vérification et inversion si nécessaire
        if borne_min > borne_max:
            borne_min, borne_max = borne_max, borne_min
        # Attributs privés (question 3)
        self.__borne_min = borne_min
        self.__borne_max = borne_max

    # =========================================
    # 2. Méthode d'affichage
    # =========================================
    def __str__(self):
        return f"[{self.__borne_min} ; {self.__borne_max}]"

    # =========================================
    # 4 et 5. Setters et Getters
    # =========================================
    def get_borne_min(self):
        return self.__borne_min

    def get_borne_max(self):
        return self.__borne_max

    def set_borne_min(self, nouvelle_borne_min):
        if nouvelle_borne_min <= self.__borne_max:
            self.__borne_min = nouvelle_borne_min
        else:
            print("Erreur : la borne minimale ne peut pas dépasser la borne maximale.")

    def set_borne_max(self, nouvelle_borne_max):
        if nouvelle_borne_max >= self.__borne_min:
            self.__borne_max = nouvelle_borne_max
        else:
            print("Erreur : la borne maximale ne peut pas être inférieure à la borne minimale.")

    # =========================================
    # 6. Redéfinition de l’opérateur d’addition
    # =========================================
    def __add__(self, other):
        if not isinstance(other, Intervalle):
            raise TypeError("L'opération n'est possible qu'entre deux intervalles.")
        # Addition des bornes respectives
        nouvelle_borne_min = self.__borne_min + other.__borne_min
        nouvelle_borne_max = self.__borne_max + other.__borne_max
        return Intervalle(nouvelle_borne_min, nouvelle_borne_max)

    # =========================================
    # 7. Méthode d’intersection
    # =========================================
    def intersection(self, other):
        if not isinstance(other, Intervalle):
            raise TypeError("L'intersection n'est possible qu'entre deux intervalles.")
        # Calcul des bornes de l'intersection
        borne_min = max(self.__borne_min, other.__borne_min)
        borne_max = min(self.__borne_max, other.__borne_max)

        # Si l’intersection est vide
        if borne_min > borne_max:
            return None
        else:
            return Intervalle(borne_min, borne_max)

    # =========================================
    # 8. Méthode d’union
    # =========================================
    def union(self, other):
        if not isinstance(other, Intervalle):
            raise TypeError("L'union n'est possible qu'entre deux intervalles.")
        # Vérifier s'il y a une intersection (donc une union possible)
        if self.intersection(other) is None:
            return None
        else:
            borne_min = min(self.__borne_min, other.__borne_min)
            borne_max = max(self.__borne_max, other.__borne_max)
            return Intervalle(borne_min, borne_max)
