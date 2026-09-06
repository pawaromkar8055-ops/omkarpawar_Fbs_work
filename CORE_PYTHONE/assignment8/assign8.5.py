#sum of all prime number upto n
def primesumno(n):
    sum=0
    for num in range(2, n + 1):
        count=0
        
        for i in range (1,num+1) :
          if num%i==0:
           count=count+1
        if count==2:
             
         sum=sum+num
    return sum
n=int(input("enter a number:"))
res=primesumno(n)
print("sum of all prime number: ",res)       