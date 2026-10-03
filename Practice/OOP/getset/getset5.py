#tree
class Tree:

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def getname(self):
        return self.name
    def setname(self, newname):
        self.name = newname
        
    def getheight(self):
        return self.height
    def setheight(self, newheight):
        self.height = newheight
        
    def getage(self):
        return self.age
    def setage(self, newage):
        self.age = newage
        
    def display(self):
        print(f"Name={self.name}\tHeight={self.height}m\tAge={self.age} years")


t1 = Tree("Mango", 15, 20)
t2 = Tree("Neem", 12, 15)

t1.display()
t2.display()

t1.setname("Apple")
t1.setage(8)
t1.display()

t2.setheight(10)
t2.display()

print(t1.getname(),t2.getheight(),t1.getage())