#2.car class
class Car:
    def __init__(self, number, brand, price):
        self.number = number
        self.brand = brand
        self.price = price
        
    def getnumber(self):
        return self.number
    def setnumber(self,newnumber):
        self.number=newnumber
    
    def getbrand(self):
            return self.brand
    def setbrand(self,newbrand):
            self.brand=newbrand
            
    def getprice(self):
            return self.price
    def setprice(self,newprice):
            self.price=newprice        
    
    
    def display(self):
        print(f"Number={self.number}\tBrand={self.brand}\tPrice={self.price}")


c1 = Car(101, "BMW", 5000000)
c2 = Car(102, "Audi", 4500000)

c1.display()

c1.setprice(8090800)
c1.display()

print(c2.getbrand())

c2.setbrand("Porche")
c2.display()

print(c1.getbrand(),"",c2.getbrand())
