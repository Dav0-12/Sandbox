"""
File reading practice
Read lines from a file and print the lines that begin with #
"""

filename = input("Please enter a filename to read: ")
file = open(filename, "r")
for line in file:
    if line.strip().startswith("#"):
        print(line.strip())
file.close()
