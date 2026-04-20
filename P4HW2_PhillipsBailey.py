# Bailey Phillips
# 04/09/2026
# P4HW2_PhillipsBailey
# This program calculates pay for multiple employees, including overtime pay,
# regular pay, gross pay, and totals for all employees entered.

"""
Pseudocode / Algorithm

1. Set total overtime pay, total regular pay, total gross pay, and employee count to 0.
2. Ask the user to enter an employee name or "Done" to stop.
3. Use a while loop that continues until the user enters "Done".
4. Inside the loop:
      a. Ask for number of hours worked.
      b. Ask for employee pay rate.
      c. If hours worked is greater than 40:
            - Overtime hours = hours worked - 40
            - Regular hours = 40
         Else:
            - Overtime hours = 0
            - Regular hours = hours worked
      d. Calculate overtime pay.
      e. Calculate regular pay.
      f. Calculate gross pay.
      g. Display the employee's pay information.
      h. Add overtime pay, regular pay, and gross pay to running totals.
      i. Add 1 to employee count.
      j. Ask for the next employee name or "Done" to terminate.
5. After loop ends, display:
      - Total number of employees entered
      - Total amount paid for overtime
      - Total amount paid for regular hours
      - Total amount paid in gross
"""

# Initialize totals
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

# Ask for first employee name
employee_name = input('Enter employee\'s name or "Done" to terminate: ')

# Loop until user enters Done
while employee_name != "Done":
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    # Calculate overtime and regular hours
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours_worked

    # Calculate pays
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = regular_hours * pay_rate
    gross_pay = overtime_pay + regular_pay

    # Display employee info
    print()
    print(f"Employee name:   {employee_name}")
    print()
    print("Hours Worked   Pay Rate    OverTime    OverTime Pay       RegHour Pay        Gross Pay")
    print("----------------------------------------------------------------------------------------")
    print(f"{hours_worked:<15.1f}{pay_rate:<12.2f}{overtime_hours:<12.1f}{overtime_pay:<19.2f}${regular_pay:<18.2f}${gross_pay:.2f}")
    print()

    # Update totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    # Ask for next employee
    employee_name = input('Enter employee\'s name or "Done" to terminate: ')

# Display totals
print()
print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")