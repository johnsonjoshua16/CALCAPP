import math
# Now this is for tan inverse---------------------------------------------------------------
def tan_inverse(angle):
    return math.atan(angle)

# Input from the user
angle = float(input("Enter the angle in radians: "))

# Calculate the tan inverse
result = tan_inverse(angle)

# Display the result
print(f"The tan inverse of {angle} radians is {result}.")