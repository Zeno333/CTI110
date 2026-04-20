# Bailey Phillips
# 03/11/2026
# P2HW2
# This program asks the user to enter six module grades, stores them in a list,
# and then displays the lowest grade, highest grade, sum of grades, and average.

# Pseudocode
# 1. Ask the user to enter grades for Module 1 through Module 6
# 2. Store the grades inside a list
# 3. Use Python functions to determine:
#       lowest grade
#       highest grade
#       sum of grades
#       average of grades
# 4. Display the results formatted like the example output

module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

grades = [module1, module2, module3, module4, module5, module6]

lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

print("\n------------Results------------")

print(f"{'Lowest Grade:':<20}{lowest}")
print(f"{'Highest Grade:':<20}{highest}")
print(f"{'Sum of Grades:':<20}{total}")
print(f"{'Average:':<20}{average:.2f}")

print("------------------------------------------")