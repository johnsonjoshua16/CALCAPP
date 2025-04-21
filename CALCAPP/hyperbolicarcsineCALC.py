import math

# Now this is for hyperbolic arcsine---------------------------------------------------------------
def hyperbolic_arcsine_number(angle):
    return math.asinh(math.radians(angle))

# Input from the user
angle = float(input("Enter the angle in degrees: "))

# Calculate the hyperbolic arcsine
result = hyperbolic_arcsine_number(angle)

# Display the result
print(f"The hyperbolic arcsine of {angle} degrees is {result}.")