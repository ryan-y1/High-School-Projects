# Created 18 Feb 2021
# Last modified 18 Feb 2021
# Code written for the Coding Exercises of 7A: Strings
##

# String Shaving: prints the input string but without the first and last character
myString = input()
print(myString[1:len(myString)-1])

# Heads and Tails: prints the input string but the first and last characters switch places
myString = input()
front = myString[0:1]
body = myString[1:len(myString)-1]
end = myString[len(myString)-1:len(myString)-0]
final = (end + body + front)
print(final)

# Next Letter: prints the character that comes after the input character in the alphabet
charInitial = ord(input())
if charInitial >= 90:
   charInitial = (90 - 26)
charNext = charInitial + 1
charFinal = chr(charNext)
print(charFinal)

# Pig Latin: translates a word into pig latin and prints it out
word = input()
pigLatin = word[1:len(word)-0] + word[0:1] + "ay"
print(pigLatin)

# The Name Game: takes a name as string input and inserts it when printing out the Name Game
name = input()
print((name + ", ") * 2 + "bo-b" + name[1:len(name)-0])
print("banana-fana fo-f" + name[1:len(name)-0])
print("fee-fi-mo-m" + name[1:len(name)-0])
print(name + "!")
