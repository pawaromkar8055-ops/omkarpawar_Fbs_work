# Count the number of spaces in a string (take input from user)
int_str=input("Enter a string: ")
count_space=0
for s in int_str:
    if s==" ":
        count_space+=1
print("Number of spaces in the string:", count_space)