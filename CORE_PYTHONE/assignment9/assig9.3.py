def reverse_number(n):
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    return rev
n=56784
res=reverse_number(n)
print("Reverse of the number is:",res)