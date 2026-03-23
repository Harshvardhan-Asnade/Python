class Student:
    Subject="python" #Class
    College="Abc"
    Year="2nd"

    def __init__(self,name): 
        self.name=name #instance


st1=Student("Harsh")

print(st1.name)
print(st1.College)
print(st1.Year)
print(st1.Subject)

