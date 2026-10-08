from emp import Employee
class Hr(Employee):
    def __init__(self, id, name, sal,com):
        super().__init__(id, name, sal)
        self.__com=com
        
    def getcom(self):
        return self.__com
    def setcom(self,newcom):
        self.__com=newcom
    
    def __str__(self):
        return super().__str__()+f"\tcom={self.__com}"