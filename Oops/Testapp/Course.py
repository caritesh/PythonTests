import Student

S4 = Student('newstu',20,50)

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
course.add_student(S1)
course.add_student(S2)

#print(course.students)
#print(course.students[0].name)
print(course.get_average_grade())

course = Course("sc",4)
course.add_student(S4)
print(course.get_average_grade())

print(S1.school)
print(S2.school)
print(S3.school)
