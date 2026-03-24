#Hiding internal Details & showing only Esstional feature
#Abstract Classe - Blueprint for other classes 

from abc import ABC, abstractmethod

class FoodOrder(ABC):

    @abstractmethod
    def place_order(self):
        pass

class PizzaOrder(FoodOrder):

    def place_order(self):
        print("Pizza is being prepared and delivered")

class BurgerOrder(FoodOrder):

    def place_order(self):
        print("Burger is being prepared and delivered")

p = PizzaOrder()
b = BurgerOrder()

p.place_order()
b.place_order()