try:
    f=open("abc.txt","r")
    data=f.read() #  R for reading method 
except Exception as e:
    print(e)
else:
    print(data)
# finally:
#     f.close
print("I am in Outside Abc")
 
