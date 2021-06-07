# Written by Ryan Y.
# Created 19 Feb 2021
# Last Modified 19 Feb 2021
# This program calculates the grade of a test.
##

score = int(input("What score did you get on your test? "))
total = int(input("How many marks was the test out of? "))

if total <= 0:
    print("Your test cannot be scored out of zero!")
else:
    grade = score / total

    if grade > 1:
        print("Does your teacher give you bonus questions? If not, you entered the values incorrectly.")
    elif grade >= 0.86:
        print("Congrats on getting an A on your test!")
    elif grade >= 0.73:
        print("Nice, you got a B on your test!")
    elif grade >= 0.67:
        print("You got a C+ on your test, not bad.")
    elif grade >= 0.60:
        print("You got a C on your test, not terrible.")
    elif grade >= 0.50:
        print("I suppose C- is not the worst...")
    elif grade >= 0:
        print("It's ok, study even harder for next time!")
    else:
        print("The numbers were entered incorrectly.")
