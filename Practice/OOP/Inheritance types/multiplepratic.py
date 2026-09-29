# class A:
#     def add():
#      print("add a")
     
# class B:
#     def add():
#         print("add B")
        
# class C(B,A):
#     def add():
#         print("add C")
        
# c1=(C)
# c1.add()        

# #output=add C

##genric algorithem
# class Emp():
#     def calsal(self):
#         print("emp calsal")

# class hr(Emp):
#     pass
#     def calsul():
#          print("hr calsal")

# class admin(Emp):
#     def calsal():
#         pass
#         print("admin calsal")

# h1=hr()
# a1=admin() 

# h1.calsal()
# a1.calsal()


##with get set
# class Emp:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
    
#     def getName(self):
#         return self.name
#     def setName(self, name):
#             self.name = name
    
#     def getSalary(self):
#         return self.salary
#     def setSalary(self, salary):
#         self.salary = salary

#     def calsal(self):
#         print("emp calsal")


# class hr(Emp):

#     def calsal(self):
#         print("hr calsal")


# class admin(Emp):

#     def calsal(self):
#         print("admin calsal")


# h1 = hr("Omkar", 50000)
# a1 = admin("Rahul", 60000)

# print(h1.getName())
# print(h1.getSalary())

# print(a1.getName())
# print(a1.getSalary())

# h1.setName("Amit")
# h1.setSalary(55000)

# a1.setName("Akash")
# a1.setSalary(65000)

# print(h1.getName())
# print(h1.getSalary())

# print(a1.getName())
# print(a1.getSalary())

# h1.calsal()
# a1.calsal()


############### class example
class Employee:
    def _init_(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    def getName(self):
        return self.name
    def setName(self,newName):
        self.name=newName
    def getSal(self):
        return self.sal
    def setSal(self,newsal):
        self.sal=newsal
    def getId(self):
        return self.id
    def setId(self,newid):
        self.id=newid
    def display(self):
       print(f"id={self.id}\tName={self.name}\tSal={self.sal}")
    def calSal(self):
        print("Emp Sal=",{self.sal})
# Emp Ends here........................
class Hr(Employee):
    def _init_(self, id, name, sal,com):
        super()._init_(id, name, sal)
        self.com=com
    def getCom(self):
            return self.com
    def setcom(self,newcom):
            self.com=newcom
    def calSal(self):
        print(f"Fianl HR Sal= {self.com+self.getSal()}")
# Hr Ends HEre............................................
    
    
class Dev(Employee):
    def _init_(self, id, name, sal,bonus):
        super()._init_(id, name, sal)
        self.bonus=bonus
    def getBonus(self):
            return self.com
    def setBonus(self,newbon):
            self.bonus=newbon
            
    def calSal(self):
        print(f"Fianl Dev Sal= {self.bonus+self.getSal()}")
# Devoloper Ends HEre............................................
    
e1=Employee(12,"Sachin",900999)
h1=Hr(18,"Smriti",85669,1000)
# d=Dev(1,"Pravin",89650,100)
# e1.calSal()
# h1.calSal()
# d.calSal()
print(e1)