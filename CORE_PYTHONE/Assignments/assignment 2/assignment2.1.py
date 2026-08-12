#hh, min, sec into sec

# hh=int(input('enter number of hours:'))
# min=60*hh
# sec=hh*3600

# print(f'min: {min} , sec {sec}')

h=int(input('enter the hours:'))
m=int(input('enteer the min:'))
s=int(input('enter the second:'))

total_sec=(h*3600) + (m*60)+s

print(f'total second is : {total_sec}')