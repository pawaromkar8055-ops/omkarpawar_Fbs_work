# use to code reduce or we can say that less line of code 

# li=[ele for ele in range(1,11)]
# print(li)

# li = [10,2,3,4,7,11,33]
# odd_li=[]
# for ele in li:
#     if ele%2!=0:
#         odd_li.append(ele)
# print(odd_li)


li=[10,2,3,4,7,11,33]
newli=[i for i in li if i%2!=0]
print(newli) 

li=[10,2,3,4,7,11,33]
new=[i+10 for i in li if (i%2!=0)]
print(new)

