import math

# Now this is for degree conversion---------------------------------------------------------------
def degree_conversion(angle):
    return math.degrees(angle)

# Input from the user
angle = float(input("Enter the angle in radians: "))

# Calculate the degree conversion
result = degree_conversion(angle)

# Display the result
print(f"The angle {angle} radians in degrees is {result}.")