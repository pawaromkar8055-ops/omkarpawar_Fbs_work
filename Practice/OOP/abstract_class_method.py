#abstract method
#1. need to implement compulsory in subclasses
#2. no body only definition present

from  abc  import    ABC,   abstractmethod
#from file import classname functionname

class Vechile(ABC):
    @abstractmethod # decorater
    def stop():
        pass
# v1=Vechicle() # can't instantiate
#we can't creat object in genric class

class Bike(Vechile): #subclass
    def start(self):
        print('start method...')
        
    def stop(self):
        print('stop method...')
        
b1=Bike()
b1.start()
b1.stop()