#mobile
class Mobile:
    def __init__(self, model, brand, price):
        self.model = model
        self.brand = brand
        self.price = price
        
    def getmodel(self):
        return self.model
    def setmodel(self,newmodel):
        self.model=newmodel
        
    def getbrand(self):
            return self.brand
    def setbrand(self,newbrand):
            self.brand=newbrand
            
    def getprice(self):
            return self.price
    def setprice(self,newprice):
            self.price=newprice
            
                
    

    def display(self):
        print(f"Model={self.model}\tBrand={self.brand}\tPrice={self.price}")


m1 = Mobile("S24", "Samsung", 75000)
m2 = Mobile("iPhone 17", "Apple", 90000)

m1.display()
m2.display()

m1.setprice(50000)
m1.display

m2.setbrand("oppo")

m2.setmodel("oppo 15")
m2.display



print(m1.getprice(),"",m2.getmodel(),m2.getbrand())