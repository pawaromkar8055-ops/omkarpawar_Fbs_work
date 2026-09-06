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