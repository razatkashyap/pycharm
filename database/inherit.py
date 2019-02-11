class Parent():
    def pap(self):
        print("I'm the father")

class Child():
    def pap(self):
        print("Stupid son")

class Inher(Child, Parent):
    pass

obj = Inher()
obj.pap()
obj.pap()