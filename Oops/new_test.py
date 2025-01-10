x = 1
type(x)
print(type(x))
#here assigning 1 to x is nothing but setting x equals an object
# which is a type 'int' of value 1
#ie whatever we work with is an object of some class.

#similarly
def testf():
    print("hello")

print(type(testf))

#method acting on an object of certain type
string = "welcome"
print(string.upper())

#try same with different datatype (notice the error)
x = 1
print(x.upper())

#method in a class and instantiating class
#method defines the operation that can be allowed
class Dog:
    def bark(self):
        print("bark")

d = Dog()
print(type(d))
#shows the 'main' module in which the class was defined.

d.bark()
print(type(d))

#add one more method in class

class Dog:
    def add_one(self,x):
        return x+1
    
    def bark(self):
        print("bark")

d = Dog()
print(d.add_one(10))

#understandinf init method
#creating an attribute of the class, 'name'
class Dog:
    def __init__(self,name):
        self.name = name
        print(name)

d = Dog("snow")
d1 = Dog("pery")
d2 = Dog("winter")

#invoking instances
class Dog:
    def __init__(self,name):
        self.name = name

d = Dog("snow")
print(d.name)
d1 = Dog("pery")
print(d1.name)
d2 = Dog("winter")
print(d2.name)

#check
d1 == d2

#using additional method
class Dog:
    def __init__(self,name):
        self.name = name
    
    def get_name(self):
        return self.name

d = Dog("snow")
print(d.get_name())
d1 = Dog("pery")
print(d1.get_name())
d2 = Dog("winter")
print(d2.get_name())

#check
d1 == d2










