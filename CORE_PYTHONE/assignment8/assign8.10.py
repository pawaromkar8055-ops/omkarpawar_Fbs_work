
def is_leap_year(year):
   if year % 400 == 0:
    return "Leap year"
   elif year % 100 == 0:
    return "Not a leap year"
   elif year % 4 == 0:
    return "Leap year"
   else:
    return "Not a leap year"

year = int(input("Enter year: "))    
res=is_leap_year(year)
print("leap year",res)