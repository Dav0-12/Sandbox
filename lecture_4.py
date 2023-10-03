"""Number formatter"""


def main():
    numbers = get_numbers()
    squared_numbers = square_numbers(numbers)
    display_numbers(squared_numbers)


def get_numbers():
    strings = input("Enter numbers seperated by commas: ").split(',')
    numbers = [float(string.strip()) for string in strings]
    return numbers


def square_numbers(numbers):
    squared_numbers = sorted([(number ** 2) for number in numbers])
    return squared_numbers


def display_numbers(numbers):
    number_string = "..".join([str(number) for number in numbers])
    print(number_string)


main()