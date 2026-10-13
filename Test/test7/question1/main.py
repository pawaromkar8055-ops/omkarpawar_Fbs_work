from book import Storebook

books={}

while True:
    print("\n+++++")
    print("1.add books")
    print("2.delete books")
    print("3.display all books")
    print("4.search books ID")
    
    choice=int(input("enter books ID: "))
    if choice==1:
        bid=int(input("Enter a books ID: "))
        
        if bid in books:
            print("books id Exists....")
        else:
            name=input("Enter books Name: ")
            price=float(input("Enter books Price: "))
            author=input("Enter books  Author: ")
            
            b=Storebook(bid,name,price,author)
            books[bid]=b 
            
            print("books added Done")
    
    elif choice == 2:
        bid = int(input("Enter books ID to delete: "))

        if bid in books:
            del books[bid]
            print("books deleted successfully!")
        else:
            print("books not found!")
            
    elif choice == 3:
        if len(books) == 0:
            print("No books available!")
        else:
            for bid in books:
                print("\n+++++++++++++")
                books[bid].display()
                
    elif choice == 4:
        bid = int(input("Enter books ID to search: "))

        if bid in books:
            print("\nbooks is  Found:")
            books[bid].display()
        else:
            print("Book not found!")

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice! Try again.....")
