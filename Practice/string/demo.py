#check digit palindrome


# string = input("Enter a string: ")

# # original = num
# reverse = string[::1]
# print(reverse)

# if string == reverse:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
    
    
    

def chkpallidrimestring(str):
    rev_str=''
    for char in str:
        rev_str=char+rev_str
        #pirnt(rev_str)
    if(str==rev_str):
        print('the string is pallindrome.')
    else:
        print('the string is not pallindrome')
                    
str=input("enter a string:")
chkpallidrimestring(str)