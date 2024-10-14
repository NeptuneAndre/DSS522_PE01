# Part 3
# Step 1: Get user input
user_input = input("Enter at least 10 numbers separated by commas or spaces: ")

# Step 2: Convert input into a list of integers
numbers = list(map(int, user_input.replace(",", " ").split()))

# Step 3: Find all odd numbers
odd_numbers = [num for num in numbers if num % 2 != 0]

# Step 4: Print or save the odd numbers in a new list
print("Odd numbers:", odd_numbers)
