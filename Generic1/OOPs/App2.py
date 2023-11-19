#inheritance
class Person:

    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def prtf(self):
        print(self.fname,self.lname)

ob1 = Person("peter","johnes")

print(ob1.fname,ob1.lname)

"""class emp(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)"""

class emp(Person):
    def __init__(self,fname,lname,empexper):
        super().__init__(fname,lname)
        self.empexper = empexper

emp1 = emp("marie","curie",empexper=20)
print(emp1.fname,emp1.lname,emp1.empexper)

x = 'encyclopedia'
print(len(x))

#polymorphism
class vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive it!!!!!")

class car(vehicle):
    pass
    """def __init__(self,brand,model):
        self.brand = brand
        self.mode = model"""

    def move(self):
        print("Drive smooth!!!")


class bike:
    def __init__(self, brand, model):
        self.brand = brand
        self.mode = model

    def move(self):
        print("Ride smooth!!!")

veh1 = vehicle("merc","sports")
car1 = car("ford","suv")
bik1 = bike("hyeu","mountain")

for i in (veh1,car1,bik1):
    i.move()

#Abstraction
from abc import ABC,abstractmethod
class testc:

    @abstractmethod
    def testf(self):
        pass





