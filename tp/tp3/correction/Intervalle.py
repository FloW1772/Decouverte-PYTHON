class Intervalle:

    def __init__(self, borne_min, borne_max):
        # if borne_min > borne_max:
        #     borne_min, borne_max = borne_max, borne_min
        self.__borne_min = min(borne_min, borne_max) # borne_min
        self.__borne_max = max(borne_min, borne_max) # borne_max

    def __str__(self):
        return '[{} ; {}]'.format(self.__borne_min, self.__borne_max)

    def get_borne_min(self):
        return self.__borne_min
    
    def set_borne_min(self, borne_min):
        if borne_min < self.__borne_max:
            self.__borne_min = borne_min
        else:
            print('ERREUR : la borne minimale demandée est supérieure à la borne maximale de l\'intervalle')
    
    """Décorateur pour utiliser les propriétés d'attributs"""
    # @property
    # def mini(self):
    #     return self.__borne_min
    
    # @mini.setter
    # def mini(self, borne_min):
    #     if borne_min < self.__borne_max:
    #         self.__borne_min = borne_min
    #     else:
    #         print('ERREUR : la borne minimale demandée est supérieure à la borne maximale de l\'intervalle')

    
    def get_borne_max(self):
        return self.__borne_max
    
    def set_borne_max(self, borne_max):
        if borne_max > self.__borne_min:
            self.__borne_max = borne_max
        else:
            print('ERREUR : la borne maximale demandée est inférieure à la borne minimale de l\'intervalle')

    


    def __add__(self, other):
        return Intervalle(self.__borne_min+other.get_borne_min(), self.__borne_max+other.get_borne_max())

    def intersection(self, other):
        if self.__borne_max < other.__borne_min or other.__borne_max < self.__borne_min:
            return None
        else:
            return Intervalle(max(self.__borne_min, other.__borne_min), min(self.__borne_max, other.__borne_max))

    def union(self, other):
        if self.__borne_max < other.__borne_min or other.__borne_max < self.__borne_min:
            return None
        else:
            return Intervalle(min(self.__borne_min, other.__borne_min), max(self.__borne_max, other.__borne_max))
