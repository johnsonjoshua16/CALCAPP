import math
# Now This is for tangent---------------------------------------------------------------
def tangent_number(angle):
    return math.tan(math.radians(angle))

# Input from the user
angle = float(input("Enter the angle in degrees: "))

# Calculate the tangent
result = tangent_number(angle)

# Display the result
print(f"The tangent of {angle} degrees is {result}.")