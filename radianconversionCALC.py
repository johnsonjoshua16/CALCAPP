import math
# Now ths is for radian conversion---------------------------------------------------------------
def radian_conversion(angle):
    return math.radians(angle)

# Input from the user
angle = float(input("Enter the angle in degrees: "))

# Calculate the radian conversion
result = radian_conversion(angle)

# Display the result
print(f"The angle {angle} degrees in radians is {result}.")