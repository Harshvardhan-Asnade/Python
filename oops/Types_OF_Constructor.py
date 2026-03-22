class Student:
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa
    def get_cgpa(self):
        return self.cgpa
    Subject="python"
    College="Abc"
    Year="2nd"
st1=Student("Harsh",9.3)
st2=Student("Ankur",9.9)
st3=Student("Ajay",8.9)

print(st1.name)
print(st1.College)
print(st1.Year)
print(st1.Subject)
print(st2.get_cgpa())
 