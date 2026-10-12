try:
 num1=int(input("Enter a number:"))
 num2=int(input("Enter a number:"))
 print(num1//num2)
 
except ZeroDivisionError as a: #specilized exception
    print(f"I am in zeroDiv",a)
    
except ValueError as v: #specilized exception
    print(f"Value err={v}")
    
except Exception as e:  #generalized exception
    print(e)

else: # executed when no exception occurs
    print("I am in else block")
    
finally: # executed always
    print("I am in finally block")
    
