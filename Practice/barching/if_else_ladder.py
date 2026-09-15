#use if else to check multiple conditions sequentially
#Decision among multiple independent choices.
#Python stops after the first true condition.


# num=int(input("Enter a number: "))
# if(num==0):
#    print('the number is neutral.')
# elif(num>0):
#    print('the number is positive.')
# else:
#    print('the number is negative.') 
   
   
num=int(input("Enter a number: "))
if(num<=0):
    print('less than or equal to zero')
elif(num <= 50):
    print('1-50') 
elif(num <= 100):
    print('51-100')
elif(num <= 150):
    print('101-150')
elif(num <= 250):
    print('151-250') 
else:
    print('greater than 250')
    
    
    
       
        
      