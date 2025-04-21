import math

#Now this is for sin inverse---------------------------------------------------------------
def sin_inverse(angle):
    return math.asin(angle)

# Input from the user
angle = float(input("Enter the angle in radians: "))

# Calculate the sin inverse
result = sin_inverse(angle)

# Display the result
print(f"The sin inverse of {angle} radians is {result}.")