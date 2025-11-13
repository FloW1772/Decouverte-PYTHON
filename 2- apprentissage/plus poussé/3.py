class TestA:
    # 1 usage
    def methode1(self):
        print("*méthode 1 de la classe testA*")

    def methode2(self):
        print("*méthode 2 de la classe testA*")

    def methode4(self):
        print("*méthode 4 de la classe testA*")

class TestB:
    # 1 usage
    def methode1(self):
        print("*méthode 1 de la classe testB*")

    def methode3(self):
        print("*méthode 3 de la classe testB*")

    def methode4(self):
        print("*méthode 4 de la classe testB*")

class TestAB(TestA, TestB):
    # 1 usage
    def methode1(self):
        print("*méthode 1 de la classe testAB*")

        def methode4(self):
         TestB.methode4(self)

ab = TestAB()
ab.methode1()
ab.methode2()
ab.methode3()
ab.methode4()
