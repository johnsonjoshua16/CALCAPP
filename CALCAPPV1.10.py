print("Welcome to CALCAPP")


print("The Order of Operations is addition, subtraction, multiplication, division, modulus, floor division, square root, power, logarithm, sine, cosine and tangent.")
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

while choice not in ['addition', 'subtraction', 'multiplication', 'division', 'modulus', 'floor division', 'square root', 'power', 'logarithm', 'sine', 'cosine', 'tangent']:
    print("Invalid choice. Please try again.")
    choice = input("Please choose a calculation from the list above: ")
print("Thank you for using CALCAPP!")

print("Make sure to come back next time! Goodbye!")
    