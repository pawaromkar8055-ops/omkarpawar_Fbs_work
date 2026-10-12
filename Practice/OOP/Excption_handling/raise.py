try: 
    age=int(input("Enter a age: "))
    if age <=0:
        raise ZeroDivisionError("Enter a valid age")
except Exception as e:
    print(e)