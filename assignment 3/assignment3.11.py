#ticket and discount by age

totalamount=0
Age1=int(input("enter the age of first person="))
Tic1=float(input("enter the ticket price of first person="))
if Age1<12:
    disco=Tic1*(30/100)
    totalamount=totalamount+-(Tic1-disco)
    print(f"passenger get discount of rs {disco} ")
    # totalamount=totalamount+(Tic1-disco)
elif Age1>59:
    disc=Tic1*(50/100)
    print(f"passengeer get disount of rs{disc} ")
    totalamount=totalamount(Tic1-disc)
else :
    totalamount=totalamount+Tic1
    print(totalamount)
 
Age2=int(input("enter the age of first person:"))
Tic2=float(input("enter the ticket price of first person:"))
if Age2<12:
    disco=Tic2*(30/100)
    totalamount=totalamount+(Tic2-disco)
    print(f"passenger get discount of rs {disco} ")
    # totalamount=totalamount+(Tic1-disco)
elif Age2>59:
    disc=Tic2*(50/100)
    print(f"passengeer get disount of rs{disc}")
    totalamount=totalamount(Tic2-disc)
else :
    totalamount=totalamount+Tic2
    print(totalamount)
  
    
    
     
    

