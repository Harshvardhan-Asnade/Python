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


# Object
st1 = Student("Harsh")

# Before change
st1.get_info()

# Change class variable using class method
Student.change_college("XYZ")

# After change
st1.get_info()