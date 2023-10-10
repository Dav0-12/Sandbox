"""
Dictionary creation.

Write a function that takes a list of strings and returns a dictionary of
string: length of string pairs

"""

def main():
    strings = ["David", "Hunter", "Someone else"]
    string_to_length_of_string = convert_list_to_dictionary(strings)
    print(string_to_length_of_string)


def convert_list_to_dictionary(strings):
    string_to_length_of_string = {}
    for string in strings:
        string_to_length_of_string[string] = len(string)
    return string_to_length_of_string



main()