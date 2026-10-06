#next is function
#we can't use for loop in this because it goes in infintie 

def infinite():
    i = 1
    while(True):
        yield i
        i +=1
        
res=infinite()

print(next(res))
print(next(res))