import math
# Now This is for cosine---------------------------------------------------------------
def cosine_number(angle):
    return math.cos(math.radians(angle))

# Input from the user
angle = float(input("Enter the angle in degrees: "))

# Calculate the cosine
result = cosine_number(angle)

# Display the result
print(f"The cosine of {angle} degrees is {result}.")