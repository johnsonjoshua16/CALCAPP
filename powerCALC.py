# Now This is for power---------------------------------------------------------------
def power_number(num, exp):
    return num ** exp

# Input from the user
number = float(input("Enter the number: "))
exponent = float(input("Enter the exponent: "))

# Calculate the power
result = power_number(number, exponent)

# Display the result
print(f"The power of {number} raised to {exponent} is {result}.")