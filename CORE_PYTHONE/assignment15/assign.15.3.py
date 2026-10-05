class Shirt():
    def __init__(self,sid=0,sname="U.S.POLO",type="formal,Asthatic",price=0.0,size="small,large"):
        self.sid=sid
        self.sname=sname
        self.type=type
        self.price=price
        self.size=size
        
    def __del__(self):
        print("Shirt is destroy")
    
    def showShirt(self):
        print("Shirt Id: ",self.sid)
        print("Shirt Name: ",self.sname)
        print("Shirt Type: ",self.type)
        print("Shirt Price: ",self.price)
        print("Shirt Size: ",self.size)
    
S1=Shirt()
S1.showShirt()

print("----------------------------")

S2=Shirt(21,"More","Formal",1534,"large")
S2.showShirt()      
        