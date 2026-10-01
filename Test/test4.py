## Write a function to which we pass a parameter and
# print the factors of a given number

def factors(num):
    i=1
    while i <= num:
        if num % i == 0:
            print(i, end=" ")
        i += 1
num=int(input("Enter a number: "))
factors(num)


## Write a program to find factorial of given number using recursion
def factorial(num):
    if num == 0 or  num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    
num = int(input("Enter a number: "))
result = factorial(num) 
print(f"The factorial of {num} is: {result}")
    
## WAP to print following patterns

n = 12

for i in range(n):
    print("*", end="")
print()

for i in range(1, n - 1):
    for j in range(n - i):
        print(" ", end="")
    print("*")

for i in range(n):
    print("*", end="")

 