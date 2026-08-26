# percentage

N=int(input("enter number of students:"))

total_percentage=0

for i in range(1, N+1):
    print("\nEnter marks for students", i)
    
    E=float(input("english marks:"))
    M=float(input("maths marks:"))
    C=float(input("chem marks:"))
    P=float(input("phiy marks:"))
    H=float(input("hindi marks:"))

    total=E+M+C+P+H
    persentage = total / 5

    print("percentage of student",i,"=",persentage,"%")

    total_percentage=total_percentage+persentage

average=total_percentage/N

print("\nAverage percentage=",average,"%")



