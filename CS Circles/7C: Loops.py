# Created 19 Feb 2021
# Last modified 20 Feb 2021
# Code written for the Coding Exercises of 7C: Loops
##

# Countup: counts from 1 to 10, prints Blastoff! when counter reaches 10
counter = 0
while counter < 10:
   counter = counter + 1
   print(counter)
print("Blastoff!")

# One Triangle: prints a triangle using 1s
n=int(input())
for i in range(0, n):
   X = 0
   for j in range(0, n-i):
      X = (X*10) + 1
   print(X)

# Square Census: prints all whole square numbers that are less than n
import math
n=int(input())
counter = int(math.sqrt(n))
x = float(math.sqrt(n))
if counter != x:
   while counter * counter <= n + 1:
      for i in range(1, counter + 1):
         print(i * i)
      counter = counter + 1
else:
   while counter * counter <= n + 1:
      for i in range(1, counter):
         print(i * i)
      counter = counter + 1
      
# Skipping: counts lines that do not contain SKIP or END and prints them
counter = 0
while True:
   lineIn = input()
   if lineIn=='SKIP':
      continue
   if lineIn=='END':
      break
   counter = counter+1
   print('line', counter, '=', lineIn)

# Finding Factors: prints all factorizations of n
n = int(input())
for i in range(1, n):
   if n * i == n:
      x = int(n // i)
      print(str(i) + " times " + str(x) + " equals " + str(n))
   else:
      x = int(n // i)
      if i * x == n:
         print(str(i) + " times " + str(x) + " equals " + str(n))
print(str(n) + " times 1 equals " + str(n))
