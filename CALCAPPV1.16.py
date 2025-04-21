print("Welcome to CALCAPP")

## This is still very much under development and is not a finished product. ##


print("The Order of Operations is addition, subtraction, multiplication, division, modulus, floor division, square root, power, logarithm, sine, cosine, tangent, mean, mode, median and range.")
print("hyperbolic sine, hyperbolic cosine, hyperbolic tangent, hyperbolic arcsine, hyperbolic arccosine, hyperbolic arctangent, sin inverse, cos inverse, tan inverse, radian conversion and degree conversion.")
choice = input("Please choose a calculation from the list above: ")

if choice == 'addition':
    import addCALC # type: ignore
    
if choice == 'subtraction':
    import subtractCALC # type: ignore
    
if choice == 'multiplication':
    import multiplyCALC # type: ignore
    
if choice == 'division':
    import divideCALC # type: ignore
    
if choice == 'modulus':
    import modulusCALC # type: ignore
    
if choice == 'floor division':
    import floordivisionCALC # type: ignore
    
if choice == 'square root':
    import squarerootCALC # type: ignore
    
if choice == 'power':
    import powerCALC # type: ignore
    
if choice == 'logarithm':
    import logarithmCALC # type: ignore
    
if choice == 'sine':
    import sineCALC # type: ignore
    
if choice == 'cosine':
    import cosineCALC # type: ignore
    
if choice == 'tangent':
    import tangentCALC # type: ignore
    
if choice == 'mean':
    import meanCALC # type: ignore
    
if choice == 'mode':
    import modeCALC # type: ignore

if choice == 'median':
    import medianCALC # type: ignore
    
if choice == 'range':
    import rangeCALC # type: ignore
    
if choice == 'hyperbolic sine':
    import hyperbolicsineCALC # type: ignore
    
if choice == 'hyperbolic cosine':
    import hyperboliccosineCALC # type: ignore
    
if choice == 'hyperbolic tangent':
    import hyperbolictangentCALC # type: ignore
    
if choice == 'hyperbolic arcsine':
    import hyperbolicarcsineCALC # type: ignore
    
if choice == 'hyperbolic arccosine':
    import hyperbolicarccosineCALC # type: ignore
    
if choice == 'hyperbolic arctangent':
    import hyperbolicarctangentCALC # type: ignore
    


while choice not in ['addition', 'subtraction', 'multiplication', 'division', 'modulus', 'floor division', 'square root', 'power', 'logarithm', 'sine', 'cosine', 'tangent', 'mean', 'mode', 'median', 'range', 'hyperbolic sine', 'hyperbolic cosine', 'hyperbolic tangent', 'hyperbolic arcsine', 'hyperbolic arccosine', 'hyperbolic arctangent', 'sin inverse', 'cos inverse', 'tan inverse', 'radian conversion', 'degree conversion']:
    print("Invalid choice. Please try again.")
    choice = input("Please choose a calculation from the list above: ")
    print("Error34: Invalid response 560174081764805634856306450")
print("Thank you for using CALCAPP!")

print("Make sure to come back next time! Goodbye! ((Refer a friend))")

## Please let us know where improvements can be made. ##
    