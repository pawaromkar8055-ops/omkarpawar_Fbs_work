#data types in python
##numberic
var=10 #int
print(type(var))

var = 10.5 #float
print(type(var))

#complex
#var(5+8j)
#print(type(var))

##text
var ='omkar' #string
print(type(var))
s1 = '''this is first line'''

print(s1)
print(type(s1))

##sequence data types
var=[10,20,30,40] #list

var = (10,20,30,40) #tuple

var = range (1,20) #range
print(type(var))
 
##set
var=set={10,20,30,40} #set
print(type(var))

var=frozenset({10, 20 , 30, 40}) #frozenset 
print(type(var))

##mapping
var={'id':10, 'name':'omkar', 'age':20} #dictionary
print(type(var)) 

#other
var= True #boolean
print(type(var))

var = None #NoneType
print(type(var))