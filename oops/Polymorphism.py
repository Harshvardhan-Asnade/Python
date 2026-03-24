class UPI:
    def pay(self):
        print("Payment done using UPI")

class Card:
    def pay(self):
        print("Payment done using Card")

class Cash:
    def pay(self):
        print("Payment done using Cash")


 
def make_payment(method):
    method.pay()


 
u = UPI()
c = Card()
ca = Cash()

make_payment(u)
make_payment(c)
make_payment(ca)