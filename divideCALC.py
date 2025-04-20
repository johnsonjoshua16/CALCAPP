# Now This is for divide---------------------------------------------------------------
def divide_numbers(num1, num2):
    if num2 == 0:
        return "Error! Division by zero."
    else:
        return num1 / num2
    
# Input from the user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Calculate the quotient
result = divide_numbers(number1, number2)

# Display the result
print(f"The quotient of {number1} and {number2} is {result}.")