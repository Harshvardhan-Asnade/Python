class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):   # overriding
        print("Dog barks")

d = Dog()
d.sound()