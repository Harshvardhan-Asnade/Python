class Student:
    Subject = "Python"
    College = "Abc"
    Year = "2nd"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_college(cls, new_college):
        cls.College = new_college

    def get_info(self):
        print(f"Myself {self.name} Study {Student.Subject} in {Student.College} College in {Student.Year} Year.")

    @staticmethod #static
    def greet():
        print("Welcome to the Student Portal")

st1 = Student("Harsh")
Student.change_college("XYZ")
Student.greet()
st1.get_info()
