import math

# Now this is for hyperbolic arctangent---------------------------------------------------------------
def hyperbolic_arctangent_number(angle):
    return math.atanh(math.radians(angle))

# Input from the user
angle = float(input("Enter the angle in degrees: "))

# Calculate the hyperbolic arctangent
result = hyperbolic_arctangent_number(angle)

# Display the result
print(f"The hyperbolic arctangent of {angle} degrees is {result}.")