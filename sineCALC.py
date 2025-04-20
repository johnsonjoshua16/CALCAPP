import math

def sine_number(angle):
    return math.sin(math.radians(angle))

# Input from the user
angle = float(input("Enter the angle in degrees: "))

# Calculate the sine
result = sine_number(angle)

# Display the result
print(f"The sine of {angle} degrees is {result}.")

## Please let us know where improvements can be made. ##