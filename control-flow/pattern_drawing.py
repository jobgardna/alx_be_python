# pattern_drawing.py

# Prompt user to enter pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop using while for rows
while row < size:
    # Inner loop using for to print '*' in one row
    for col in range(size):
        print("*", end="")  # print without newline
    print()  # move to the next line after one row is printed
    row += 1  # increment row
