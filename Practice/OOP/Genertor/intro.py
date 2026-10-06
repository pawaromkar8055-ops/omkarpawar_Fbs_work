#1. for memory optimization 
#2. Generating value according to user requriment
#3. Use yield keyword in code , not use return use yield
#4. Maintain state maintain stack frame
#5. Iterate upcoming value using next from iterable

def generstValues(n):
    for i in range(1, n + 1):
        yield i
        
res=generstValues(10)

print(next(res))
print(next(res))
print(next(res))
print(next(res))

print(next(res))
print(next(res))
print(next(res))
