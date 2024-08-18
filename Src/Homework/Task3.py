# WAP to calculate are if circle
import math

radius=float(input("Enter the radius of the circle "))
pi=math.pi
area=pi*pow(radius,2)
area2=3.14*(radius**2)
print("Area of circle with radius -", radius ,"is", area)
print(f"Formatted area {area:2f}")
print(f"Formatted area {area2:2f}")

"""
* -> Multiplication
** -> power
"""
#one Liner

print(3.14*(float(input("Enter radius \n"))**2))