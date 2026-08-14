# check which numbers are divisible by 7 and multiple of 5 in given range

n=int(input("enter the number:"))

i=0
while i<=n:
    if i%7==0 and i%5==0:
     print(i, end=' ') 
    i+=1