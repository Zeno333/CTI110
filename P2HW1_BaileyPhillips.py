# Bailey Phillips
# 03/10/2026
# P2HW1
# This program calculates travel expenses and displays them with formatted output.

budget = float(input("Enter Budget: "))
destination = input("\nEnter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
hotel = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

remaining = budget - gas - hotel - food

print("\n------------Travel Expenses------------")

print(f"{'Location:':<20}{destination}")
print(f"{'Initial Budget:':<20}${budget:,.2f}")
print(f"{'Fuel:':<20}${gas:,.2f}")
print(f"{'Accommodation:':<20}${hotel:,.2f}")
print(f"{'Food:':<20}${food:,.2f}")

print("---------------------------------------")

print(f"\nRemaining Balance: ${remaining:,.2f}")