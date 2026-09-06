# area of rectangle

#type1: without pp and without rv
def area():
    L=int(input("Enter a length:"))
    B=int(input("Enter a bradth:"))
    
    area=L*B
    print(f'area of rectangle is {area}.')
# area()    



#type2: with pp and without rv

def area(L,B):
    area=L*B
    print('area:',area)
L=20
B=4
area(L,B)    


#type3: without pp and with rv

def area():
    L=int(input('enter a length:'))
    B=int(input('enter a bradth:'))
    
    area=L*B
    return area
res=area()
print(res)

#type4: with pp with rv

def area(L,B):
    area=(L*B)
    return area
L=int(input('enter a length:'))
B=int(input('enter a bradth:'))

res=area(L,B)
print('area:',res)