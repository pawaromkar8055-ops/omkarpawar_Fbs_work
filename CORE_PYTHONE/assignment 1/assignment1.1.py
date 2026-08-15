#percentage calculation of 5 subjects

E=int(input('enter obtained marks in english:'))
M=int(input('enter obtained marks in maths:'))
H=int(input('enter obtained marks in hindi:'))
P=int(input('enter obtained marks in physics:'))
C=int(input('enter obtained marks in chemistry:'))
 #percentage 
total_marks = E + M + H + P + C
percentage = (total_marks / 500) * 100
print(f"Percentage: {percentage}%")