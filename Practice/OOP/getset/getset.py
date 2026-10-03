##employee calss with get set 
class Employee:

    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal

    def getid(self):
        return self.id
    def setid(self,newid):
        self.name=newid
        
    def getname(self):
            return self.name
    def setname(self,newname):
            self.name=newname
            
    def getsal(self):
            return self.sal
    def setsal(self,newsal):
            self.sal=newsal        


    def display(self):
        print(f"Id={self.id}\tName={self.name}\tSal={self.sal}")


e1 = Employee(12, "Sachin", 9087)
e2 = Employee(18, "Smriti", 38383)

e1.display()

e1.setname("Rohit")
e1.display()

print(e2.getsal())

e2.setsal(12121212)

print(e2.getname(),"",e2.getsal())

 
