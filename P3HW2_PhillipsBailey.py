# Bailey Phillips
# 03/26/2026
# P3HW2_Salary_PhillipsBailey
# This program calculates an employee's regular pay, overtime pay,
# and gross pay based on hours worked and pay rate.

# Pseudocode / detail algorithm:
# 1. Ask user to enter employee name.
# 2. Ask user to enter number of hours worked.
# 3. Ask user to enter employee pay rate.
# 4. Check if hours worked is greater than 40.
# 5. If hours worked is greater than 40:
#       overtime hours = hours worked - 40
#       regular hours = 40
#    Else:
#       overtime hours = 0
#       regular hours = hours worked
# 6. Calculate overtime pay = overtime hours * pay rate * 1.5
# 7. Calculate regular pay = regular hours * pay rate
# 8. Calculate gross pay = regular pay + overtime pay
# 9. Display employee name
# 10. Display hours worked, pay rate, overtime hours, overtime pay,
#     regular pay, and gross pay in a formatted table.

# User input
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Calculations
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours_worked

overtime_pay = overtime_hours * pay_rate * 1.5
regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay

# Output
print()
print(f"Employee name:   {employee_name}")
print()
print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime':<12}{'OverTime Pay':<18}{'RegHour Pay':<18}{'Gross Pay':<12}")
print("--------------------------------------------------------------------------------")
print(f"{hours_worked:<15.1f}{pay_rate:<12.1f}{overtime_hours:<12.1f}${overtime_pay:<17.2f}${regular_pay:<17.2f}${gross_pay:<.2f}")