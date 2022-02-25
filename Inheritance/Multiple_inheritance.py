class Animal(object):#A
    def __init__(self,name):
        self.name=name
    def getname(self):
        return self

class Dog(Animal):#B
    def sleeps(self, name, food=None):
        print("%s sleeps at %s"%(self.name,food))

class Elephant(Dog):#C=(A,B)
    def jungle(self,name,sugar):
        print("%s eats %s"%(self.name,sugar))

c=Elephant("Animal")
c.eat("food")
c.sleeps("Dog","pet house")
c.jungle("Elephant","Aravali")

