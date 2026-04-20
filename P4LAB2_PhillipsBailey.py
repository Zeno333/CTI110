# Bailey Phillips
# P4LAB2_PhillipsBailey

run_again = "yes"

# while loop to keep program running
while run_again.lower() == "yes":

    num = int(input("Enter an integer: "))

    # check if number is negative
    if num < 0:
        print("This program does not handle negative numbers.")
    else:
        # for loop to print multiplication table
        for i in range(1, 13):
            print(f"{num} * {i} = {num * i}")

    # ask user if they want to run again
    run_again = input("\nWould you like to run the program again? ")

print("Exiting program...")