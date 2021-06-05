# Created 20 Feb 2021
# Last modified 20 Feb 2021
# Code for the Coding Exercises of 7B: Math
##

# Eggsactly: prints the number of dozens and remainder
eggs = int(input())
cartons = eggs // 12
remainder = eggs % 12
print(cartons)
print(remainder)

# Divisibility: takes two integers and determines if the two are divisible with no remainder
a = int(input())
b = int(input())
ans = a % b
if ans == 0:
   print("divisible")
else:
   print("not divisible")

# Pizza Circles: use the math module to calculate and print the area of a pizza
import math
r = float(input())
a = math.pi * (r ** 2)
print(a)

# Geometric Mean: calculates the geometric mean of two integers
import math
a = float(input())
b = float(input())
ans = math.sqrt(a * b)
print(ans)

# Skill-Testing Question: multiplies the sum of integers A and B by C and prints the value
a = int(input())
b = int(input())
c = int(input())
ans = (a + b) * c
print(ans)

# A Feat with Feet: converts height measured in feet to centimetres
heightFt = float(input())
heightCm = heightFt * 30.48
print(heightCm)

# Gravity: calculates the time it takes for a parcel to reach the ground when dropped from 11000 metres
import math
v = float(input())
timeReq = (v - math.sqrt(v ** 2 - 4 * -4.9 * 11000)) / (2 * -4.9)
print(timeReq)
