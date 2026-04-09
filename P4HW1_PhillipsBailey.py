# Bailey Phillips
# 04/09/2026
# P4HW1_PhillipsBailey
# This program asks the user for a number of scores, checks that each score
# is valid, stores the scores in a list, drops the lowest score, calculates
# the average, and displays the letter grade.

"""
Pseudocode / Algorithm

1. Create an empty list to store scores.
2. Ask the user how many scores they want to enter.
3. Use a loop to collect that many scores.
4. For each score:
      a. Ask the user to enter the score.
      b. While the score is less than 0 or greater than 100:
            - Display an error message.
            - Ask the user to enter the score again.
      c. Add the valid score to the list.
5. Find the lowest score in the list.
6. Remove the lowest score from the list.
7. Find the average of the modified list.
8. Determine the letter grade using the average:
      A = 90-100
      B = 80-89
      C = 70-79
      D = 60-69
      F = below 60
9. Display:
      - Lowest score
      - Modified score list
      - Scores average
      - Grade
"""

# Create empty list
score_list = []

# Ask user for number of scores
num_scores = int(input("How many scores do you want to enter? "))

# Loop to collect scores
for score_num in range(1, num_scores + 1):
    score = float(input(f"\nEnter score #{score_num}: "))

    while score < 0 or score > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{score_num} again: "))

    score_list.append(score)

# Find and remove lowest score
lowest_score = min(score_list)
score_list.remove(lowest_score)

# Calculate average
average_score = sum(score_list) / len(score_list)

# Determine letter grade
if average_score >= 90:
    letter_grade = "A"
elif average_score >= 80:
    letter_grade = "B"
elif average_score >= 70:
    letter_grade = "C"
elif average_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display results
print("\n")
print("--------------Results--------------")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {score_list}")
print(f"Scores Average: {average_score:.2f}")
print(f"Grade         : {letter_grade}")
print("-----------------------------------")