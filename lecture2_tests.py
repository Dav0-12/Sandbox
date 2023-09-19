"""Good Function Names"""

# 1. determine a subject grade based on a given total score
# def determine_subject_grade

# 2. convert currency to USB to AUD
# convert_USD_to_AUD

# 3. print a report
# print_report

# 4. calculate the average of a list of numbers
# calculate_average

# 5. determine is a number is even
# is_even

# 6. get a user's age, making sure that it is not negative
# get_valid_age

"""Smiley face system"""

import random


def main():
    low_number = get_number("Low Number: ")
    high_number = get_number("High Number: ")
    while high_number <= low_number:
        print(f"Enter a number higher than {low_number}")
        high_number = get_number("High Number: ")
    n = random.randint(low_number, high_number)
    print_smiley_faces(n)


def get_number(prompt):
    number = int(input(prompt))
    return number


def print_smiley_faces(number_of_smily):
    print("😁" * number_of_smily)


main()
