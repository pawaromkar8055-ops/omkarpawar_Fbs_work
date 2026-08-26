#sum fact
n=int(input("enter a number:"))
fact=1
sum=0
for i in range(1,n+1):
    fact=fact*i
    sum=sum+fact
print("Sum=",sum)    


# **sum
n=int(input("enter a number:"))
sum=0
for i in range(1,n+1):
    sum=sum+n**i
print("Sum=",sum)    


#gemotric series
n=int(input("enter a number:"))
term=1
sum=0
for i in range(1,n+1):
    sum=sum+term
    term=term*2
print("Sum=",sum)    