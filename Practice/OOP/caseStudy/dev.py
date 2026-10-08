from emp import Employee
class Dev(Employee):
    def __int__(self,id,name,sal,bonus):
        super().__init__(id,name,sal)
        self.__bonus=bonus
    def getbonus(self):
        return self.__bonus
    def setbonus(self,newbonus):
        self.__bonus=newbonus
    def __str__(self):
        return super().__str__()+f"\tBonu={self.__bonus}"   
        