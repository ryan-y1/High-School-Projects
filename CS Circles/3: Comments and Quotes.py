# Created 17 Feb 2021
# Last modified 17 Feb 2021
# Code written for the Coding Exercises of 3: Comments and Quotes
##

# Second Guessing: prints the num of seconds in a week
# goal: print out the number of seconds in a week 
secondsPerMinute = 60
secondsPerHour = secondsPerMinute * 60 # todo: check this!
secondsPerDay = secondsPerHour * 24
daysPerWeek = 7
# daysPerWeek = daysPerWeek + 2 # weekends are disabled!?
print(secondsPerDay * daysPerWeek)

# The Great Escape: prints a string with escape sequences
# 1st method
print("A double-quote\'s escaped using a backslash, e.g. \\\"")
# 2nd method
print('A double-quote\'s escaped using a backslash, e.g. \\"')
# 3rd method
print("A double-quote" + "'" + "s escaped using a backslash, e.g." + " \\" + '"')
