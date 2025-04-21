import math

# Now this is for hyperbolic sine---------------------------------------------------------------
def hyperbolic_sine_number(angle):
    return math.sinh(math.radians(angle))

# Input from the user
angle = float(input("Enter the angle in degrees: "))

# Calculate the hyperbolic sine
result = hyperbolic_sine_number(angle)

# Display the result
print(f"The hyperbolic sine of {angle} degrees is {result}.")