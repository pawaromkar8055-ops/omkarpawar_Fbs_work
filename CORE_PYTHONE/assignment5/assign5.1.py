correctUID="firstbit"
correctPass="1213"

i=0

while i<=3:
    UID=input("enter UID:")
    Pass=input("enter Pass:")
    
    if UID==correctUID and Pass==correctPass:
        print("login successful")
        
        break
    else:
        print("Incorrect UID or Pass")
        print("attempts left:", 3-i)
        
    i+=1    
    
if i>3:
        print("you exceeded maximum attempts. ")
        print("program terminated.")
        