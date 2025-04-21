import math

# Now this is for cos inverse---------------------------------------------------------------
def cos_inverse(angle):
    return math.acos(angle)

# Input from the user
angle = float(input("Enter the angle in radians: "))

# Calculate the cos inverse
result = cos_inverse(angle)

#  Display the result
print(f"The cos inverse of {angle} radians is {result}.")