class Product:
    def __init__(self,pid=0,pname="unknow",Pprice=0.0,quantity=0):
        self.pid=pid
        self.pname=pname
        self.Pprice=Pprice
        self.quantity=quantity
        
    def __del__(self):
        print("Product Done")
    
    def showproduct(self):
        print("Product Id: ",self.pid)    
        print("Product Name: ",self.pname)
        print("Product Price: ",self.Pprice)
        print("Product Quantity: ",self.quantity)
    
p1=Product()
p1.showproduct()

print("++++++++++++++++++++++")

p2=Product(2125,"Opppp",7938,5)
p2.showproduct()