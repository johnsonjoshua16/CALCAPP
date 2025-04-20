# Now this is for Range---------------------------------------------------------------
def range_numbers(numbers):
    return max(numbers) - min(numbers)

# Input from the user
numbers = list(map(float, input("Enter the numbers separated by spaces: ").split()))

# Calculate the range
result = range_numbers(numbers)

# Display the result

print(f"The range of the numbers is {result}.")