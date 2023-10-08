"""Age and Name matching"""


def main():
    names = ["David", "Tracey", "Glen", "Ryley", "Jake"]
    ages = [19, 46, 56, 17, 10]
    print(find_oldest_person(names, ages))


def find_oldest_person(names, ages):
    oldest_index = ages.index(max(ages))
    oldest_person = names[oldest_index]
    return oldest_person


main()
