class A(object):
    @staticmethod
    def methode_statique():
        print("je suis une méthode statique")

    def methode_d_instance(self):
        print("je suis une méthode de l'instance %s (A)" % self)

class B(A):
    def methode_d_instance(self):
        super().methode_d_instance()
        print("je suis une méthode de l'instance %s (B)" % self)

class C(A):
    def methode_d_instance(self):
        super().methode_d_instance()
        print("je suis une méthode de l'instance %s (C)" % self)

class D(B, C):
    def methode_d_instance(self):
        super().methode_d_instance()
        print("je suis une méthode de l'instance %s (D)" % self)

print(type(D))
print(D.mro())