# Bailey Phillips
# 03/05/2026
# P2LAB2
# This program stores vehicle MPG values in a dictionary and calculates
# the gallons of gas needed for a trip.

cars = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

keys = cars.keys()

print(keys)

vehicle = input("Enter a vehicle to see it's mpg: ")

mpg = cars[vehicle]
print(f"\nThe {vehicle} gets {mpg} mpg.")

miles = float(input(f"\nHow many miles will you drive the {vehicle}? "))

gallons = miles / mpg

print(f"\n{gallons:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles} miles.")