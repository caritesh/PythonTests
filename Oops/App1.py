class Testc:
    x = 100

ob1 = Testc()
ob2 = Testc()
print(ob1.x)
print(ob2.x)

class Person:

    def __init__(self,name,age,x="welcome"):
        self.name = name
        self.age = age
        self.x = x

    def __str__(self):
        return f"{self.name} ({self.age})"

    def testf(self):
        print("name provided is   :" + self.name)

ob1 = Person("peter",40,'cool')
ob2 = Person("marie",50)
ob3 = Person("johny",33)

print(ob1.name,ob1.age,ob1.x)
#OR
print(ob1.__str__())
#OR
print(str(ob1))
print(ob1.__repr__())
print(ob1.testf())

"""del ob1"""

"""ob1.name = 'Peter'
ob1.age = 40
ob1.name,ob2.name,ob3.name = ('marie','john','johny')
print(ob1.name)"""

