#Resusing attribute and methods from a parent class is know as Inheritance 
class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)

class Student(Person):  # inheriting Person
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def show_course(self):
        print("Course:", self.course)

s1 = Student("Harsh", "Computer Science")

s1.show_name()      
s1.show_course()    
