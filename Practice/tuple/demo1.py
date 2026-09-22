#1.()
tu=(10,20,30,40)
tu=(10,)

#2.hetrogeneous
tu=(10,'abc',3.14,10)

#3.ordered

#4.Immutable
# tu[0]=7

#5.duplication alloweed

#6.faster then list
print(type(tu))
print(tu)


import sys # for size of list 
print(sys.getsizeof(tu))