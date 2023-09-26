"""
What is the output of the following?

s = "\tPython, Monty  \n"
print(s[1], ".", sep="")
print(s.strip(), ".", sep="")
s.replace(' ', '*')
print(s.lstrip(), ".", sep="")
print(s.strip().split(','))

"""

"""
name = input("Name: ")
with open("name.txt", "w") as out_file:
    print(name, file=out_file)
"""

"""
strings = ["Steve", "Bob", "Ben", "David", "Hunter"]
# Can also use enumerate function to create an index counter. Syntax: for i, string in enumerate(strings, 1)
# i will then start at 1 and count up for each iteration
for string in strings:  
    index_of_name = (strings.index(string) + 1)
    outfile = open(f"{string}.txt", 'w')
    print(f"The name {string} is in position {index_of_name}", file=outfile)
    outfile.close()
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is: ", result)  # no danger of undefined variable
