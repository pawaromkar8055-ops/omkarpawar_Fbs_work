# Topic:Student Result Management System using OOP
# Display student details
# Calculate total marks
# Calculate percentage
# Calculate grade
# Check pass/fail
# Use private variables
# Use getter and setter
# Use a constructor
# Create multiple student objects

class student:
    def __init__(self,name,rollno,python,sql,oop):
        self.name=name
        self.rollno=rollno
        self.python=python
        self.sql=sql
        self.oop=oop
        
    def getname(self):
        return self.name
    def setname(self,newname):
        self.name=newname
        
    def getrollno(self):
        return self.rollno
    def setrollname(self,newrollno):
        self.rollno=newrollno
        
    def getpython(self):
        return self.python
    def setpython(self,newpython):
        self.python=newpython
        
    def getsql(self):
        return self.sql
    def setsql(self,newsql):
        self.sql=newsql
        
    def getoop(self):
        return self.oop
    def setoop(self,newoop):
        self.oop=newoop
        
    def display(self):
        print("Name:",self.name)
        print("Rollno:",self.rollno)
        print("Python:",self.python)
        print("Sql:",self.sql)
        print("OOP:",self.oop)
        
    def total(self):
       return  self.python+self.sql+self.oop
   
    def percentage(self):
        return self.total()/3
    
    def grade(self):
        percentage=self.percentage()
        
        if percentage>=90:
            return "A+"
        
        elif percentage>=80:
            return "A"
        
        elif percentage>=70:
            return "B+"
        
        elif percentage>=60:
            return "B"
        
        elif percentage>=50:
            return "C"
        
        else:
            return "F"
        
    def result(self):
        if self.python>=40 and self.sql>=40 and self.oop>=40:
            print("Congrats")
            return "PASS"
        else:
            print("Best luck for next exam")
            return "FAIL"
        
name = input("Enter Name: ")
rollno = int(input("Enter Roll No: "))
python = int(input("Enter Python Marks: "))
sql = int(input("Enter SQL Marks: "))
oop = int(input("Enter OOP Marks: "))
print("++++++++++++++++++++++++++")
s1=student(name,rollno,python,sql,oop)
s1.display()

print("Total:",s1.total())
print("Percentage:",s1.percentage())
print("Grade:",s1.grade())
print("Result:",s1.result())
print("Thankyou")