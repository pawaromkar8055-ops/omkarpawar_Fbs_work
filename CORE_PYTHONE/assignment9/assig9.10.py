def revnum(n):
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    return rev  
n=int(input("Enter a number: "))
res=revnum(n)
print("Reverse of the number is:",res)            