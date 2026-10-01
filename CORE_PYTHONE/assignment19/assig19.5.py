# Find all of the words in a string that are less than 5 letters
# (take input from user)

int_str=input("Enter a string: ")
words=int_str.split()
print("Words in the string that are less than 5 letters:", 
      [word for word in words if len(str(word))<5])    