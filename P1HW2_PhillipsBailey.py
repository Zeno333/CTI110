# Bailey Phillips
# 03/01/2026
# P1HW2
# This program calculates and displays travel expenses and remaining budget.

"""
PSEUDOCODE (Program Logic)
1. Display program intro message
2. Ask user for budget (number)
3. Ask user for travel destination (text)
4. Ask user for gas cost (number)
5. Ask user for hotel/accommodation cost (number)
6. Ask user for food cost (number)
7. Add gas + hotel + food to get total expenses
8. Subtract total expenses from budget to get remaining balance
9. Display formatted travel expense report and remaining balance
"""

# Intro
print("This program calculates and displays travel expenses\n")

# Inputs
budget = float(input("Enter Budget: "))
destination = input("\nEnter your travel destination: ")
gas = float(input("\nHow much do you think you will spend on gas? "))
hotel = float(input("\nApproximately, how much will you need for accomodation/hotel? "))
food = float(input("\nLast, how much do you need for food? "))

# Calculations
expenses = gas + hotel + food
remaining = budget - expenses

# Output
print("\n------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget:.0f}\n")
print(f"Fuel: {gas:.0f}")
print(f"Accomodation: {hotel:.0f}")
print(f"Food: {food:.0f}\n")
print(f"Remaining Balance: {remaining:.0f}")