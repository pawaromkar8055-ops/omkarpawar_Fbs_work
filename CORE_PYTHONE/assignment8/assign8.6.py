#Write a program to find print the following Fibonacci series using function


def fibserSum(n):
    a=0
    b=1
    for i in range(n):
        c=a+b    
        print(a,end=' ')
        sum=c
        a=b
        b=c
n=int(input("enter a number:"))
print=fibserSum(n)    