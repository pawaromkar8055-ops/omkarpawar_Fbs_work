from myexception import Myexception
try:
    age=int(input("Enter a age: "))
    if age<=0:
        raise Myexception(age)
except Myexception as a:
    print(a)

except Exception as e:
    print(e)

    