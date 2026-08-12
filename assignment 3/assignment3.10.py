#age limit
Age=int(input("enter age of M/F:"))
Gender=input("enter gender (M/F):")

if Gender=="F":
    if Age>=18:
        print("eligible for marriage")
    else:
        print("not eligible for marriage")
      
else:
    if Age>=21:
        print("eligible for marriage")
    else:
        print("not eligible for marriage")           
