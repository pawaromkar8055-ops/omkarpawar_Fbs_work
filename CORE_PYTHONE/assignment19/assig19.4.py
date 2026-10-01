# Remove all of the vowels in a string (take input from user)
int_str=input("Enter a string: ")
vowels="aeiouAEIOU"
new_str=" "
for s in int_str:
    if s not in vowels:
        new_str+=s
print("String after removing vowels:", new_str)