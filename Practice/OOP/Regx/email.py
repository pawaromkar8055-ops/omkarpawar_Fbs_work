import re
emai=input("Enter the mail to check:")
pat=r"^[a-z0-9._%+-]+@[a-zA-ZO-9.-]+\.[a-zA-Z]{2,}$" # email validation pattern, r =raw string ,start from r
res=re.search("gmail",emai)
if res:
    print("Pattern Found")
else:
    print("Pattern is not found")

    