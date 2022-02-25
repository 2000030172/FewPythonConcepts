class KLU(object):
    def __init__(self,name):
        self.name=self
    def details(self,college):
        print("{} {}".format(self.name,college))

class Location(KLU):
    def grrenfields(self,location):
        print("{}".format(self.name,location))

class student(KLU):
    def Vijayawada(self, name=None):
        print("{}".fomrat(self,name))

loc=Location("Vaddesswaram")
student=("Prashanth")
loc.grrenfields("Vijayawada")

