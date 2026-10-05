class Book :
    def __init__(self,bid=0,bname="unknown",bprice=0.0,bauthor="unknown"):
        self.bid=bid
        self.bname=bname
        self.price=bprice
        self.author=bauthor

    def __del__(self):
        print("Book object destroyed")
        
    def showbook(self):
        print("BOOK Id: ",self.bid)
        print("BOOK NAME: ",self.bname)
        print("BOOK PRICE: ",self.price)
        print("BOOK AUTHOR: ",self.author)
        

b1=Book()
b1.showbook() 

print("+++++++++++++++++++++++++++++")

b2=Book(52,"Vaibhavwadi",4735,"Shivpatil")
b2.showbook()
    
    
    