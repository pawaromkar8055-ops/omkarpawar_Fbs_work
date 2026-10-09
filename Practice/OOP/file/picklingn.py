import pickle # always we have to use when there is pickling
class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name
         
    def getid(self):
        return self.id
    def setid(self,newid):
        self.id=newid
        
    def getname(self):
        return self.name
    def setname(self,newname):
        self.name=newname
            
    def display(self):
        print(f"ID={self.id}\t Name={self.name}")

    def __str__(self):
        return(f"ID={self.id}\t Name={self.name}")

e1=Employee(10,'SumitRao')
e2=Employee(2,"Topperer")

#using wb mode in piklingn
#piklingn
f=open("emp.dat","wb")
print(f.tell)

#pickle.dump("ObjectName","Object of a file")

pickle.dump(e1,f)
pickle.dump(e2,f)

fr=open("emp.dat","rb")
f.seek(8)

#unpkileing 
data=pickle.load(fr)
data1=pickle.load(fr)

print(data)
print(data1)

# WRITE / APPEND
# f = open("abc.txt", "ab")
# pickle.dump(e1, f)
# pickle.dump(e2, f)
# f.close()


# READ
# fr = open("abc.txt", "rb")
# data = pickle.load(fr)
# data1 = pickle.load(fr)

# print(data)
# print(data1)
# fr.close()









