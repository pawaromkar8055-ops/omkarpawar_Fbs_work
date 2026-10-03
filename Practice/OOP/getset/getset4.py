#product
class Product:
    def __init__(self, pid, pname, quantity):
        self.pid = pid
        self.pname = pname
        self.quantity = quantity
        
    def getid(self):
        return self.pid
    def setid(self, newid):
        self.pid = newid

    def getname(self):
        return self.pname
    def setname(self, newname):
        self.pname = newname

    def getquantity(self):
        return self.quantity
    def setquantity(self, newquantity):
        self.quantity = newquantity
        
    def display(self):
        print(f"ID={self.pid}\tName={self.pname}\tQuantity={self.quantity}")


p1 = Product(1, "Laptop", 10)
p2 = Product(2, "Mouse", 50)

p1.display()
p2.display()

p1.setid(101)
p1.setname("HP Laptop")
p1.setquantity(20)
p1.display()

print(p2.getid(),p2.getname(),p2.getquantity())