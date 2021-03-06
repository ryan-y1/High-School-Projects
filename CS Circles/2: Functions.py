# Created 16 Feb 2021
# Last modified 16 Feb 2021
# Code written for the Coding Exercises of 2: Functions
##

# One Road: prints the max weight that can be transported across three bridges
print(min(a,b,c))

# Two Roads: prints the path with the higher weight limit
routeA = min(a,b,c)
routeB = min(d,e)
maxRoute = max(routeA,routeB)
print(maxRoute)

# Growth Debugging: calculates the population growth over 3 years, when population grows by 10% each year
populationIn2012 = 1000
populationIn2013 = populationIn2012 * 1.1
populationIn2014 = populationIn2013 * 1.1
populationIn2015 = populationIn2014 * 1.1

# Complication: prints the lower value between variables A and B without using the min function
print(max(-A, -B) * -1)

# Payment Calculator: prints the minimum payment of a bank account
minimumPayment = max(10, balance * 0.021)
print(min(balance, minimumPayment))
