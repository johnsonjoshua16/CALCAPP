print("Welcome to CALCAPP")
from MathMentorAI import MathMentorAI # type: ignore



## This is still very much under development and is not a finished product. ##


print("The Order of Operations is addition, subtraction, multiplication, division, modulus, floor division, square root, power, logarithm, sine, cosine, tangent, mean, mode, median and range.")
print("hyperbolic sine, hyperbolic cosine, hyperbolic tangent, hyperbolic arcsine, hyperbolic arccosine, hyperbolic arctangent, radian conversion and degree conversion.")
choice = input("Please choose a calculation from the list above: ")

if choice == 'addition':
    import CALCAPP.addCALC as addCALC # type: ignore
    
if choice == 'subtraction':
    import CALCAPP.subtractCALC as subtractCALC # type: ignore
    
if choice == 'multiplication':
    import CALCAPP.multiplyCALC as multiplyCALC # type: ignore
    
if choice == 'division':
    import CALCAPP.divideCALC as divideCALC # type: ignore
    
if choice == 'modulus':
    import CALCAPP.modulusCALC as modulusCALC # type: ignore
    
if choice == 'floor division':
    import CALCAPP.floordivisionCALC as floordivisionCALC # type: ignore
    
if choice == 'square root':
    import CALCAPP.squarerootCALC as squarerootCALC # type: ignore
    
if choice == 'power':
    import CALCAPP.powerCALC as powerCALC # type: ignore
    
if choice == 'logarithm':
    import CALCAPP.logarithmCALC as logarithmCALC # type: ignore
    
if choice == 'sine':
    import CALCAPP.sineCALC as sineCALC # type: ignore
    
if choice == 'cosine':
    import CALCAPP.cosineCALC as cosineCALC # type: ignore
    
if choice == 'tangent':
    import CALCAPP.tangentCALC as tangentCALC # type: ignore
    
if choice == 'mean':
    import CALCAPP.meanCALC as meanCALC # type: ignore
    
if choice == 'mode':
    import CALCAPP.modeCALC as modeCALC # type: ignore

if choice == 'median':
    import CALCAPP.medianCALC as medianCALC # type: ignore
    
if choice == 'range':
    import CALCAPP.rangeCALC as rangeCALC # type: ignore
    
if choice == 'hyperbolic sine':
    import CALCAPP.hyperbolicsineCALC as hyperbolicsineCALC # type: ignore
    
if choice == 'hyperbolic cosine':
    import CALCAPP.hyperboliccosineCALC as hyperboliccosineCALC # type: ignore
    
if choice == 'hyperbolic tangent':
    import CALCAPP.hyperbolictangentCALC as hyperbolictangentCALC # type: ignore
    
if choice == 'hyperbolic arcsine':
    import CALCAPP.hyperbolicarcsineCALC as hyperbolicarcsineCALC # type: ignore
    
if choice == 'hyperbolic arccosine':
    import CALCAPP.hyperbolicarccosineCALC as hyperbolicarccosineCALC # type: ignore
    
if choice == 'hyperbolic arctangent':
    import CALCAPP.hyperbolicarctangentCALC as hyperbolicarctangentCALC # type: ignore
    
if choice == 'radian conversion':
    import CALCAPP.radianconversionCALC as radianconversionCALC # type: ignore
    
if choice == 'degree conversion':
    import CALCAPP.degreeconversionCALC as degreeconversionCALC # type: ignore


while choice not in ['addition', 'subtraction', 'multiplication', 'division', 'modulus', 'floor division', 'square root', 'power', 'logarithm', 'sine', 'cosine', 'tangent', 'mean', 'mode', 'median', 'range', 'hyperbolic sine', 'hyperbolic cosine', 'hyperbolic tangent', 'hyperbolic arcsine', 'hyperbolic arccosine', 'radian conversion', 'degree conversion']:
    print("Invalid choice. Please try again.")
    choice = input("Please choose a calculation from the list above: ")
    print("Error34: Invalid response 560174081764805634856306450")
print("Thank you for using CALCAPP!")

print("Make sure to come back next time! Goodbye!")
print( "((Refer a friend))")

## Please let us know where improvements can be made. ##
    