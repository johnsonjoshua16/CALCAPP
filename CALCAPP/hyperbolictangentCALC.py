import math


# Now this is for hyperbolic tangent---------------------------------------------------------------
def hyperbolic_tangent_number(angle):
    return math.tanh(math.radians(angle))

# Input from the user
angle = float(input("Enter the angle in degrees: "))

# Calculate the hyperbolic tangent
result = hyperbolic_tangent_number(angle)

# Display the result
print(f"The hyperbolic tangent of {angle} degrees is {result}.")