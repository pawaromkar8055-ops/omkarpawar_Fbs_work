# Use a dictionary comprehension to count the length of each word
# in a sentence (take input from user)

di={word:len(word) for word in input("Enter a string: ").split()}
print("Length of each word in the string:", di)