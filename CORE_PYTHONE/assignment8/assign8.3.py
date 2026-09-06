#sum of series 
def sumSeries():
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum

n=int(input('enter a number:'))
res=sumSeries()
print("sum of series=",res)        
    
#sum of factroal
def factsumSeries():
    fact=1
    sum=0
    for i in range(1,n+1):
        fact=fact*i
        sum=fact+sum
    return sum
n=int(input('enter a number:'))

res=factsumSeries()
print("sum of fact series=",res)        

#sum of power series
def powerSeries():
    sum=0
    for i in range(1,n+1):
        sum=sum+(i**i)
    return sum
n=int(input('enter a number:'))
res=powerSeries()
print("sum of power series=",res)    