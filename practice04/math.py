#1 task 
import math

# We write the degree that we want to convert into radians. 
n=int(input("Input degree:"))
radian=round((n*(math.pi/180)),6) # Convert degrees to radians and round to 6 decimal places

print("Output radian:",radian )

#2 task
# Function to calculate the area of a trapezoid
def trapezoid(he,va1,va2):
    area = 0.5 * (va1 + va2) * he
    return area

# Ask the user to enter height and two base values
h=int(input("Height:"))
v1=int(input("Base, first value:"))
v2=int(input("Base, second value:"))

area=trapezoid(h,v1,v2)
print("Expected area", area)

#3 task
def area(p, apo): #define a function that calculates polygon area using perimeter and apothem
    return (p*apo)/2
n=int(input("Input number of sides:"))
w=int(input("Input the length of a side:"))
p=n*w #First, we calculate perimetr for formula
apothem=w/(2*(math.tan(math.pi/n))) #calculate the apothem using the formula
total=area(p,apothem)
print("The area of the polygon is:",round(total,2))

#4 task
n=int(input("Length of base:"))
h=int(input("Height of parallelogram:"))
print(n*h)