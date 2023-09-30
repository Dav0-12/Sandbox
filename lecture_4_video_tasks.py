"""
Name display system


def main():
    try:
        names = ["David", "Ryley", "Tracey", "Glen", "Jake"]
        number = int(input(f"Enter a number from 1 to {len(names)}: "))
        print(names[number - 1])
    except ValueError:
        print("This is not a valid integer")
    except IndexError:
        print("This number is not within the defined range")


main()
"""

"""
Nested Lists and Ordering


from operator import itemgetter


def main():
    try:
        score_pairs = [['Derek', 7], ['Carrie', 8], ['Bob', 6]]
        name = input("Name: ")
        score = float(input("Score: "))
        score_pairs.append([name, score])
        score_pairs.sort(key=itemgetter(1), reverse=True)
        print(f"{score_pairs}")
    except ValueError:
        print("Something went wrong")


main()
"""

"""
Display words that are longer than 3 characters
Use list comprehension

text = "This is a sentence"
words = text.split()
words_longer_than_3_chars = [word for word in words if (len(word) > 3)]
print(words_longer_than_3_chars)
"""




