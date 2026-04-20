# Bailey Phillips
# 04/20/2026
# P5LAB
# This program simulates a self-checkout machine. It generates a random total,
# asks the user for payment, calculates change, and displays the breakdown.

import random

# Function to calculate and display change
def disperse_change(change):
    # Convert to cents to avoid float issues
    change = int(round(change * 100))

    dollars = change // 100
    change %= 100

    quarters = change // 25
    change %= 25

    dimes = change // 10
    change %= 10

    nickels = change // 5
    change %= 5

    pennies = change

    print("\nChange is: ${:.2f}".format((dollars*100 + quarters*25 + dimes*10 + nickels*5 + pennies)/100))

    if dollars > 0:
        print(f"{dollars} Dollars")
    if quarters > 0:
        print(f"{quarters} Quarters")
    if dimes > 0:
        print(f"{dimes} Dimes")
    if nickels > 0:
        print(f"{nickels} Nickels")
    if pennies > 0:
        print(f"{pennies} Pennies")


# Main function
def main():
    # Generate random total owed
    total_owed = round(random.uniform(0.01, 100.00), 2)

    print(f"You owe ${total_owed:.2f}")

    # Get user input
    cash = float(input("How much cash will you put in the self-checkout? "))

    # Validate input
    while cash < total_owed:
        print("Not enough money. Please enter an amount equal to or greater than the total.")
        cash = float(input("Enter amount: "))

    # Calculate change
    change = cash - total_owed

    # Call function
    disperse_change(change)


# Call main function
main()