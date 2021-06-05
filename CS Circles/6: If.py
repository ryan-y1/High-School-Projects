# Created 17 Feb 2021
# Last modified 17 Feb 2021
# Code written for the Coding Exercises of 6: If
##

# IHOPython: depending on the input value, prints either Yum! or Still hungry!
pancakes = int(input())
x = pancakes
if x > 3:
   print("Yum!")
if x <= 3:
   print("Still hungry!")

# What's Your Sign?: prints the sign of an integer value from input
x=int(input())
if x > 0:
   print("Positive")
if x < 0:
   print("Negative")
if x == 0:
   print("Zero")
   
# Age Checker: reads integer input and prints whether or not a person of this age can vote
age = int(input())
if age >= 0:
   if age <= 17:
      print("Too young to vote")
   if age > 17:
      print("You can vote")
if age < 0:
   print("You are a time traveller")
