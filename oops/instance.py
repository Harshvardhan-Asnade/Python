class Student:
    def __init__(self,name):
        self.name=name
    Subject="python"
    College="Abc"
    Year="2nd"

    def get_infoStudnet(self):
        return(f"Myself {self.name} Study {Student.Subject} in {Student.College} College in {Student.Year} Year.")



st1=Student("Harsh")
st2=Student("Ajay")
print(st1.get_infoStudnet())
print(st2.get_infoStudnet())