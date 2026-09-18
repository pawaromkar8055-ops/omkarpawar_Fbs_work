##pass:to neglect expected indented block error
# for i in  range(1,10):
#   pass

##break:to stop the loop
for i in range (1,10):
    if (i==6):
        break
    print(i)

##continue:to stop current iteration
# for i in range (1,10):
#     if(i==4):
#       continue
#     print(i)
    

##else:will exeute when loop executed successful
# for i in range (1,10):
#     if (i==5):
#         break
#     print(i)
# else:
#     print("else executed")
    
##prime number eg:
# num=int(input('Enter number:'))
# for i in range(2,num):
#     if(num%i==0):
#         print(i)
#         print(f'{num} is a not  prime number')
#         break
# else:
#     print(f"{num} is a prime number")        