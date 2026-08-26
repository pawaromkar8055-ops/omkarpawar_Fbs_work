#Ticket price

P=int(input("enter number of passengers:"))
Ticketcost=float(input("enter ticket cost of one person:"))

totalamount=0

for i in range(1,P+1):
    age=int(input(f' enter age of passanger {i}:'))
    
    if age < 12:
        amount=Ticketcost-(Ticketcost*30/100)
        print("30% discount applied")
    
    elif age>59:
        amount=Ticketcost-(Ticketcost*50/100)
        print("50% discount applied")
            
    else:
        amount=Ticketcost
        print("full ticket price")
        
    totalamount=totalamount+amount
  
print("total ticket=", totalamount)                