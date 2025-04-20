# Now this is for Mean---------------------------------------------------------------
def mean_numbers(numbers):
    return sum(numbers) / len(numbers)

# Input from the user
numbers = list(map(float, input("Enter the numbers separated by spaces: ").split()))

# Calculate the mean
result = mean_numbers(numbers)

#   Display the result
print(f"The mean of the numbers is {result}.")