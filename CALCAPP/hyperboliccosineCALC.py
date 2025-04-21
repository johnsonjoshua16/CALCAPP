import math


# Now this is for hyperbolic cosine---------------------------------------------------------------
def hyperbolic_cosine_number(angle):
    return math.cosh(math.radians(angle))

# Input from the user
angle = float(input("Enter the angle in degrees: "))

# Calculate the hyperbolic cosine
result = hyperbolic_cosine_number(angle)

#   Display the result
print(f"The hyperbolic cosine of {angle} degrees is {result}.")
