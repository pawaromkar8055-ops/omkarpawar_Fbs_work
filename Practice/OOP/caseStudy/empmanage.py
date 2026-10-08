from hr import Hr
from dev import Dev

class Empmanage:
    Empdetil={} #indepented because it is static karu
    def addEmp(self):
        eid=(input("Enter Emp Id="))
        if eid in Empmanage.Empdetil:
            print("Employee is Alredy Exist..")
            return
        else:
            ename=input("enter the Emp Name=")
            esal=int(input("Enter a Emp salary="))
            print("1.Hr")
            print("2.Devloper")
            
            ch=int(input("Enter a Choice="))
            if ch==1:
                ecom=float(input("Enter the com of Hr="))
                emp= Hr(eid,ename,esal,ecom)
            elif ch==2:
                bonus=int(input("Enter the Bonus of dev="))
                emp=Dev(eid,ename,esal,bonus)  
            else:
                print("Invalid Choice")
                return    
            Empmanage.Empdetil[eid]=emp
            print("Emp added sussefully.....")
                 
    def displayEmp(self):
        if len(Empmanage.Empdetil)==0:
            print("Emp is not Exist.....")
        else:
            for var in Empmanage.Empdetil.values():
                print(var)
        
    
    def searchEmp(self):
        eid = input("Enter Employee Id = ")

        if eid in Empmanage.Empdetil:
            emp = Empmanage.Empdetil[eid]
            print(emp)
        else:
            print("Employee Not Found...")
        
        
    def updateEmp(self):
        eid =input("Enter Employee Id = ")
        
        if eid in Empmanage.Empdetil:
            emp = Empmanage.Empdetil[eid]
            
            ename = input("Enter New Employee Name = ")
            esal=float(input("Enter New Employee Salary = "))
            
            emp.setName(ename)
            emp.setSal(esal)
                   
            if isinstance(emp,Hr):
                ecom=float(input("Enter New Comission of Hr = "))
                emp.setcom(ecom)
                
            elif isinstance(emp,Dev):
                bonus=float(input("Enter New Bonus of Developer = "))
                emp.setbonus(bonus)
            
            print("Employee Updated Successfully....")
        
        else:
            print("Employee not found......")
        
            
    def deleteEmp(self):
        eid =input("Enter Employee Id = ")
        
        if eid in Empmanage.Empdetil:
            del Empmanage.Empdetil[eid]
            print("Employee Deleted Successfully....")
        else:
            print("Employee Not Found......")

        eid=input("Enter Employee Id to Update = ")            
            
        
        
   