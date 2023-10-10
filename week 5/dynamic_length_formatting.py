"""
import operator

data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
# data.sort(key=operator.itemgetter(1), reverse=True)

max_name_length = max(len(name[0]) for name in data)
max_number_length = max(len(str(name[1])) for name in data)
for pair in sorted(data, key=operator.itemgetter(1), reverse=True):
    print(f"{pair[0]: <{max_name_length}} = {pair[1]: >{max_number_length}}")
"""
import operator

name_to_number = {'Derek': 7, 'Xavier': 80, 'Bob': 612, 'Chantanelle': 9}

max_name_length = max(len(name) for name in name_to_number.keys())
max_number_length = max(len(str(number)) for number in name_to_number.values())

for name, number in sorted(name_to_number.items(), key=operator.itemgetter(1), reverse=True):
    print(f"{name: <{max_name_length}} = {number: >{max_number_length}}")
