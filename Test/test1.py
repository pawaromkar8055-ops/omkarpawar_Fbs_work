##area and parimeter
L=int(input("length :")) 
D=int(input("diameter :"))
# r=int(input("raduis :"))

r = D / 2
straight = L - D

# Area = rectangle + circle
area = (straight * D) + ( r * r)

# Perimeter = 2 straight sides + circumference of circle
perimeter = (2 * straight) + (2 *  r)

print("Area =", area)
print("Perimeter =", perimeter)



##simple interst
P = float(input("Enter Principal: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))

SI = (P * R * T) / 100

print("Simple Interest =", SI)

##distance travel
km = float(input("Enter distance in kilometers: "))

meter = km * 1000
centimeter = km * 100000

print("Distance in meters =", meter)
print("Distance in centimeters =", centimeter)


#area of painting wall
A = float(input("Enter area of one wall: "))
B= float(input("Enter area of secound wall: "))
interior_cost = float(input("Enter interior painting cost per unit area: "))
exterior_cost = float(input("Enter exterior painting cost per unit area: "))

exterior_area = A * 1 and B*1
interior_area = A * 1 and B*1

exterior_painting_cost = exterior_area * exterior_cost
interior_painting_cost = interior_area * interior_cost

total_cost = exterior_painting_cost + interior_painting_cost

print("Exterior wall area =", exterior_area)
print("Interior wall area =", interior_area)
print("Exterior painting cost =", exterior_painting_cost)
print("Interior painting cost =", interior_painting_cost)
print("Total painting cost =", total_cost)