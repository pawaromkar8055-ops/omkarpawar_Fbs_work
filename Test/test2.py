# #life year or not 
year = int(input("Enter a year: "))

if year % 4 == 0:
    
    if year % 100 == 0:
        
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
            
    else:
        print("Leap Year")
        
else:
    print("Not a Leap Year")


# ## find  3 digit number 
num = int(input("Enter a 3-digit number: "))

first = num // 100
second = (num // 10) % 10
third = num % 10

if first == 2 * second and first * 2 == third:
    print("Yes, you have done it")
else:
    print("Please try next time")
    

# # ##cost of farmer
radius = 20
length = 50
breadth = 40
cost_per_meter = 35

circle_perimeter = 2 * 3.14 * radius

rectangle_perimeter = 2 * (length + breadth)

total_perimeter = circle_perimeter + rectangle_perimeter

total_wire = total_perimeter * 5

total_cost = total_wire * cost_per_meter

print("Total cost of fencing =", total_cost, "Rs")    

# # ##Colour painting
length = float(input("Enter length of wall: "))
height = float(input("Enter height of wall: "))
cost_per_sq_meter = float(input("Enter painting cost per square meter: "))

if length > 0 and height > 0 and cost_per_sq_meter > 0:

    one_wall_area = length * height

    total_area = 4 * one_wall_area

    total_cost = total_area * cost_per_sq_meter

    print("Total area to be painted =", total_area, "square meters")
    print("Total cost of painting =", total_cost, "Rs")

else:
    print("Invalid input")
    
    
# # ##Gst 
p1 = float(input("Enter product price 1: "))
p2 = float(input("Enter product price 2: "))
p3 = float(input("Enter product price 3: "))
p4 = float(input("Enter product price 4: "))
p5 = float(input("Enter product price 5: "))

if p1 >= 0 and p2 >= 0 and p3 >= 0 and p4 >= 0 and p5 >= 0:

    total = p1 + p2 + p3 + p4 + p5

    Gst = total * 18 / 100

    final_bill = total + Gst

    print("Total Product Price =", total)
    print("GST (18%) =", Gst)
    print("Final Bill =", final_bill)

else:
    print("Invalid product price")    