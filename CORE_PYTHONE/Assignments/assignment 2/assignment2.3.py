#distant in feet and inches
F=float(input("enter the distant in feet:"))
I=float(input("enter the distant in inches:"))

M=F*0.3048 + I*0.0254
CM=F*30.40 + I*2.54
print(f"distant in meter is: {M}")
print(f"distant in centimeter is: {CM}")