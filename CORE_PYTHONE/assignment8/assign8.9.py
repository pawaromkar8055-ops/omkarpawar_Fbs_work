def is_palindrome(n): 
    temp = n
    rev = 0

    for i in range(len(str(n))):
     digit = n % 10
     rev = rev * 10 + digit
     n = n // 10

    if temp == rev:
     return "Palindrome number"
    else:
      return "Not a palindrome number"
  
n = int(input("Enter a number: "))
res=is_palindrome(n)
print("palindrome number",res)
    