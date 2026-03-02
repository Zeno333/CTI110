# Bailey Phillips
# 03/01/2026
# P1HW1
# This program calculates exponents and performs addition and subtraction
# using user input.

print("-----Calculating Exponents-----")

base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

result = base ** exponent

print(f"\n{base} raised to the power of {exponent} is {result} !!\n")

print("-----Addition and Subtraction-----")

start_num = int(input("Enter a starting integer: "))
add_num = int(input("Enter an integer to add: "))
subtract_num = int(input("Enter an integer to subtract: "))

total = start_num + add_num - subtract_num

print(f"\n{start_num} + {add_num} - {subtract_num} is equal to {total}")