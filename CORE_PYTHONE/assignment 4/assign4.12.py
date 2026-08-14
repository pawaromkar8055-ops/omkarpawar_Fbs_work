# check armstrong number

N=int(input("enter a number:"))
count=len(str(N))
temp=N
arno=0
while N>0:
    dig=N%10
    arno=arno+(dig**count)
    N//=10
if temp==arno:
    print(f"{temp} is Armstrong")
else:
    print("no is not armstrong")    