class Product:
    count=0
    def __init__(self,Productname,ProductPrice):
        self.Productname=Productname
        self.ProductPrice=ProductPrice
        Product.count += 1

    def getProductInfo(self):
        print(f"The Price of the {self.Productname} is {self.ProductPrice} Rs." )
    
    @classmethod
    def get_count(cls):
        return cls.count
    
    @staticmethod
    def get_discount(Productname,ProductPrice,DiscountPercentage):
        print(f"{Productname} Final Price with Discout is {ProductPrice-(ProductPrice*DiscountPercentage/100)}")

Product1=Product('Phone',100000)
Product2=Product('Headphone',5000)
Product4=Product('Laptop',150000)
Product3=Product('Moniter',10000)

Product1.getProductInfo()
Product2.getProductInfo()
Product4.getProductInfo()
Product3.getProductInfo()

print(f"Total Product : {Product.count}")

Product1.get_discount(Product1.Productname,Product1.ProductPrice,10)
Product2.get_discount(Product2.Productname,Product2.ProductPrice,15)
Product3.get_discount(Product3.Productname,Product3.ProductPrice,50)
Product4.get_discount(Product4.Productname,Product4.ProductPrice,25)