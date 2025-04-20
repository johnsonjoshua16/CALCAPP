# Now this is for Mode---------------------------------------------------------------
def mode_numbers(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    max_frequency = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_frequency]
    return modes

# Input from the user
numbers = list(map(float, input("Enter the numbers separated by spaces: ").split()))

# Calculate the mode
result = mode_numbers(numbers)

# Display the result
print(f"The mode of the numbers is {result}.")