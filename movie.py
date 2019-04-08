# Created by: Aden Rao
# Created on: April 7, 2019
# This program lets the user enter age and based on that it tells them what movies they can see.

# imports math function
import math

#Input fot the user to enter their age and it tells them to
myAge = int(input("Type your age: "))

# If statment to determine what movies they can see
if myAge >= (17):
		print("You can watch R Rated Movies")
elif myAge >= (13):
		print("You can watch PG-13 Rated Movies")
elif myAge >= (1):
		print("You can watch G Rated Movies")
