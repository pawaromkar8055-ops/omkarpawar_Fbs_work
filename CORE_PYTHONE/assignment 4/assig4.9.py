# number in range divisible by a given number

start=int(input("enter starting number:"))
end=int(input("enter ending number:"))
n=int(input("enter divisible number:"))
i=start
while(i<=end):
    if i%n==0:
         print(i, end=' ') 
    i+=1 