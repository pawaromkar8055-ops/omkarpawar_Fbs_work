#3.bank account
class BankAccount:
    def __init__(self, accno, name, balance):
        self.accno = accno
        self.name = name
        self.balance = balance
        
    def getaccno(self):
        return self.accno
    def setaccno(self,newaccno):
        self.accno=newaccno 
        
    def getname(self):
            return self.name
    def setname(self,newname):
            self.name=newname
            
    def getbalance(self):
            return self.balance
    def setbalance(self,newbalance):
            self.balance=newbalance            

    def display(self):
        print(f"Account={self.accno}\tName={self.name}\tBalance={self.balance}")


a1 = BankAccount(1001, "Omkar", 25000)
a2 = BankAccount(1002, "Amit", 40000)

a1.display()

a1.setbalance(500000)
a1.display()

a2.setname("piyush")
a2.display()

print(a1.getbalance(),"",a2.getname())