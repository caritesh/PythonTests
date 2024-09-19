""" 
class Person:
    #class attr or constant (instead of global constant)
    number_of_people = 0

    def __init__(self,name):
        self.name = name
        Person.number_of_people += 1

p1 = Person("tim")

print(p1.number_of_people) #accessing usng instance of class ie p1
print(Person.number_of_people) #accessing using class
p2 = Person("john") 
print(p2.number_of_people)
#to change
Person.number_of_people = 4
print(p1.number_of_people)
print(p2.number_of_people)
 """
#class mthods
""" class Person:
    #class attr or constant (instead of global constant)
    number_of_people = 0

    def __init__(self,name):
        self.name = name
        Person.add_people()

    @classmethod
    def number_of_people_m(cls):
        return cls.number_of_people()
    
    @classmethod
    def add_people(cls):
        cls.number_of_people += 1
    
p1 = Person("tim")

print(p1.number_of_people) #accessing usng instance of class 
print(Person.number_of_people) #accessing using class


p2 = Person("john") 
print(p2.number_of_people)
print(Person.number_of_people)
 """








