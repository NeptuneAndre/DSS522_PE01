# Part 2
# Generate a list of the first 50 integers
integers = list(range(1, 51))

# Print the list of integers
print("List of the first 50 integers:")
print(integers)

# Find and print the even numbers from the list
even_numbers = [num for num in integers if num % 2 == 0]

print("\nList of even numbers:")
print(even_numbers)
