import re # regular expression
# data="My name is Rohit and age is 36 or 37"

# re.findall(pattern,data) it takes 2 parameter return output in list format
# d=re.findall(r"\d+",data)
# print(d)
# d=re.findall(r"\d{2}",data)

# d=re.search(pattern,data)
# d=re.search(r"\d+",data) #it return none after search it don't find and take first match only it not cheak secound 
# print(d.group())

# d=re.match(r"\d+",data) # returns None because the string starts with letters.  
# print(d)

# d=re.fullmatch(r"\d+",'12345')
# print(d)
# print(d.group())

data="Pradip sir Mocks is Easy"
# print(data)
print(re.sub("Easy","Worthy",data)) # three parametrs will pass

# print(re.findall(r'\D',"ABCD1234"))
# print(re.findall(r'\w',"ABCD1234#&_"))
# print(re.findall(r'\W',"ABCE1234&*!"))
# print(re.findall(r'\s',"I am Good"))
# print(re.findall(r'c...t',"cauet cot cut"))
# print(re.findall('ab*','abcd abd ab'))
# print(re.findall('ab?','abcd abd ab'))
# print(re.findall(r'\w{4}','abc abcd adc abcd'))
# print(re.findall(r'\w{3,4}','abc abcd adc abcd'))
# print(re.findall("[aeiou]","I am good in python"))
# print(re.findall("[1-9]{2}","I am good in python4747")) #anicer
# print(re.findall("[1-9]$","I am good in python9"))


# \d  Any digit  r"\d" 
#  \D  Any non-digit  r"\D" 
#  \w  Word character: letters, digits, underscore  r"\w+" 
#  \W  Non-word character  r"\W" 
#  \s  Whitespace  r"\s+" 
#  \S  Non-whitespace  r"\S+" 
#  .  Any character except newline by default  r"a.c" 
#  ^  Beginning of string  r"^Hello" 
#  $  End of string  r"end$" 
#  *  Zero or more repetitions  r"a*" 
#  +  One or more repetitions  r"a+" 
#  ?  Zero or one repetition  r"colou?r" 
#  {n}  Exactly n repetitions  r"\d{3}" 
#  {n,m}  Between n and m repetitions  r"\d{2,4}" 
#  []  Any one character from a set  r"[aeiou]" 
#  [^ ]  Any character not in the set  r"[^0-9]" 
#  ()  Capturing group  r"(\d+)" 
#    OR condition  r"cat\dog" 
#  \b  Word boundary  r"\bcat\b" 
#  \A  Beginning of string  r"\AHello" 
#  \Z  End of string  r"end\Z" 
#  \\  Literal backslash in a regex pattern  r"\\"
