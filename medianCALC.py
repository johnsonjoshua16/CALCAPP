# Now this is for Median---------------------------------------------------------------
def median_numbers(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]
    
# Input from the user
numbers = list(map(float, input("Enter the numbers separated by spaces: ").split()))

# Calculate the median
result = median_numbers(numbers)

# Display the result
print(f"The median of the numbers is {result}.")