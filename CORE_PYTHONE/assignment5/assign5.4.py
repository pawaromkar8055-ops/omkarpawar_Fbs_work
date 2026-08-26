N=int(input("enter a number:"))
i=1


for i in range(i,N):
    count=len(str(n))
    temp=n
    arno=0
    dig=n%10
    arno=arno+(dig**count)
    n//=10
if temp==arno:
    print(f"{temp} is Armstrong")
else:
    print("no is not armstrong")    