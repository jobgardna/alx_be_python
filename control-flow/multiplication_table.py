# multiplication_table.py

# Prompt user for the number
number = int(input("Enter a number to see its multiplication table: "))

# Use a for loop to iterate from 1 to 10
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
