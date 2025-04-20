import math
# Now This is for logarithm---------------------------------------------------------------
def logarithm_number(num, base):
    return math.log(num, base)

# Input from the user
number = float(input("Enter the number: "))
base = float(input("Enter the base: "))

# Calculate the logarithm
result = logarithm_number(number, base)

# Display the result
print(f"The logarithm of {number} to the base {base} is {result}.")

## Please let us know where improvements can be made. ##