
"""
class Dog:

    def __init__(self,name):
        self.name = name

    def bark(self):
        print("bark")
    
    def meow(self):
        return 'meow'
    
    def add_one(self,x):
        return x + 1

#instatiating a new instance of class Dog()

d = Dog("snow")
print(d)
print(type(d))
d.bark()
d.meow()
d.add_one(10)
d.name


###################
class Dog:

    def __init__(self,name):
        self.name = name
    
    def get_name(self):
        return self.name

#instatiating a new instance of class Dog()
d = Dog("snow")
print(d)
print(type(d))
d.name
d.get_name()


################
class Dog:

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self,age):
        self.age = age

#instatiating a new instance of class Dog()
d = Dog("snow",14)
print(d)
print(type(d))
d.name
d.get_name()
d.get_age()

#setting and checking age
d.set_age(10)
d.get_age()

"""
#creating complex objects

""" class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade #0 - 100
    
    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self,name,max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        #self.is_active = False
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value/len(self.students)
    

S1 = Student('tom',20,95)
S2 = Student('john',21,94)
S3 = Student('mary',19,76)

course = Course("sc",2)

print(course.students)
print(type(course.students))

course.add_student(S1)

course.add_student(S2)
print(course.students)

#print(course.students)
#print(course.students[0].name)
print(course.get_average_grade())


 """

#working with inheritance
""" 
class Pet: #generalization
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"i am {self.name} and my age is {self.age}")

    def speak(self):
        print("I dont know what to speak")

class Cat(Pet):
    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("Bow")

class Fish(Pet):
    pass

p = Pet('snow',19)
p.show()
p.speak()

c = Cat("sky",4)
c.show()
c.speak()

f = Fish('joy',23)
f.speak() #inherits frm Pet and doesn't have its own method speak

"""
#getting more complex
""" class Pet: #generalization
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"i am {self.name} and my age is {self.age}")

    def speak(self):
        print("I dont know what to speak")

class Cat(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"i am {self.name} and my age is {self.age} and i am {self.color}")
        
class Dog(Pet):
    def speak(self):
        print("Bow")

class Fish(Pet):
    pass

p = Pet('snow',19)
p.show()
p.speak()

c = Cat("sky",4,'black')
c.show()
c.speak()

f = Fish('joy',23)
f.speak() 
 """

""" class School():
    def __init__(self,name,location):
        self.name = name
        self.location = location
    
    def info(self):
        print(f'my school is {self.name} & am at {self.location}')
    
class types(School):
    def __init__(self,name,location,typeofstu):
        super().__init__(name,location)
        self.typeofstu = typeofstu

    def info(self):
        print(f'my school is {self.name} & am at {self.location} & conduct {self.typeofstu}')

q1 = School('PF','harih')
q1.info()

c1 = types('PF','harih','science')
c1.info()
 """