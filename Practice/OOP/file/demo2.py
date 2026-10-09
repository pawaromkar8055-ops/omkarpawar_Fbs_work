#dynasatu
f=None
try:
    f=open("xyz.txt",'r')
    data=f.read() # reading data from file
except FileNotFoundError as fe: # specilize ecpection handlig error imp****
    print(fe)
else:
    print(data)
finally:
    if f is not None:
        print("File close ho gayi")
        f.close
print("All task are done....")

## with useing raise expception handling
# f=None
# try:
#     f=open("xyz.txt",'r')
#     data=f.read() # reading data from file
#     if not data:
#         raise Exception("File mai kuch nahi hai")
# except FileNotFoundError as fe: # specilize ecpection handlig error imp****
#     print(fe)
# else:
#     print(data)
# finally:
#     if f is not None:
#         print("File close ho gayi")
#         f.close
# print("All task are done....")