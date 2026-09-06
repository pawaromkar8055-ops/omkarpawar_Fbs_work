#sum of digit of number

def sumdigit(num):
    sum=0
    while num>0:
        d=num%10
        sum=sum+d
        num=num//10
        
    return sum    
                
num=int(input("enter a number:"))  
res=sumdigit(num)      
print("sum of digit =",res)  
    




    