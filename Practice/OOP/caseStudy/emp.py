class Employee:
    def __init__(self,id,name,sal):
        self.__id=id
        self.__name=name
        self.__sal=sal
    def getId(self):
        return self.__id
    def setId(self,newid):
        self.__id=newid
        
    def getName(self):
        return self.__name
    def setName(self,Newname):
        self.__name=Newname
        
    def getSal(self):
        return self.__sal
    def setSal(self,Newsal):
        self.__sal=Newsal
        
    def __str__(self):
        return f" id={self.__id}\t name={self.__name}\tsal={self.__sal}"        