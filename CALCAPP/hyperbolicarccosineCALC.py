import math

# Now this is for hyperbolic arccosine---------------------------------------------------------------
def hyperbolic_arccosine_number(angle):
    return math.acosh(math.radians(angle))

# Input from the user
angle = float(input("Enter the angle in degrees: "))

# Calculate the hyperbolic arccosine
result = hyperbolic_arccosine_number(angle)

# Display the result
print(f"The hyperbolic arccosine of {angle} degrees is {result}.")