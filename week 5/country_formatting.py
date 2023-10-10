"""Country formatting"""

import csv

FILE_NAME = "countries.csv"


def main():
    country_to_data = load_data()
    display_data(country_to_data)


def load_data():
    country_to_data = {}
    with open(FILE_NAME, 'r') as in_file:
        reader = csv.reader(in_file)
        next(reader)
        for record in reader:
            record[2] = int(record[2].replace(',', ''))
            record[3] = float(record[3][:-1])
            print(record)
            country_to_data[record[0]] = record[1:-1]
    return country_to_data


def display_data(country_to_data):




main()