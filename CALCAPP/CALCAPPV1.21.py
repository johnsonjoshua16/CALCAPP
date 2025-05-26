print("Welcome to CALCAPP")
import MathMentorAI.MathMentorAI as MathMentorAI # type: ignore
import tkinter as tk
from tkinter import messagebox

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

def perform_calculation():
    choice = calc_var.get()
    if choice == "":
        messagebox.showwarning("No Selection", "Please choose a calculation.")
        return
    try:
        if choice == 'addition':
            import CALCAPP.addCALC as addCALC
        elif choice == 'subtraction':
            import CALCAPP.subtractCALC as subtractCALC
        elif choice == 'multiplication':
            import CALCAPP.multiplyCALC as multiplyCALC
        elif choice == 'division':
            import CALCAPP.divideCALC as divideCALC
        elif choice == 'modulus':
            import CALCAPP.modulusCALC as modulusCALC
        elif choice == 'floor division':
            import CALCAPP.floordivisionCALC as floordivisionCALC
        elif choice == 'square root':
            import CALCAPP.squarerootCALC as squarerootCALC
        elif choice == 'power':
            import CALCAPP.powerCALC as powerCALC
        elif choice == 'logarithm':
            import CALCAPP.logarithmCALC as logarithmCALC
        elif choice == 'sine':
            import CALCAPP.sineCALC as sineCALC
        elif choice == 'cosine':
            import CALCAPP.cosineCALC as cosineCALC
        elif choice == 'tangent':
            import CALCAPP.tangentCALC as tangentCALC
        elif choice == 'mean':
            import CALCAPP.meanCALC as meanCALC
        elif choice == 'mode':
            import CALCAPP.modeCALC as modeCALC
        elif choice == 'median':
            import CALCAPP.medianCALC as medianCALC
        elif choice == 'range':
            import CALCAPP.rangeCALC as rangeCALC
        elif choice == 'hyperbolic sine':
            import CALCAPP.hyperbolicsineCALC as hyperbolicsineCALC
        elif choice == 'hyperbolic cosine':
            import CALCAPP.hyperboliccosineCALC as hyperboliccosineCALC
        elif choice == 'hyperbolic tangent':
            import CALCAPP.hyperbolictangentCALC as hyperbolictangentCALC
        elif choice == 'hyperbolic arcsine':
            import CALCAPP.hyperbolicarcsineCALC as hyperbolicarcsineCALC
        elif choice == 'hyperbolic arccosine':
            import CALCAPP.hyperbolicarccosineCALC as hyperbolicarccosineCALC
        elif choice == 'hyperbolic arctangent':
            import CALCAPP.hyperbolicarctangentCALC as hyperbolicarctangentCALC
        elif choice == 'radian conversion':
            import CALCAPP.radianconversionCALC as radianconversionCALC
        elif choice == 'degree conversion':
            import CALCAPP.degreeconversionCALC as degreeconversionCALC
        else:
            messagebox.showerror("Invalid Choice", "Invalid calculation selected.")
            return
        messagebox.showinfo("Success", f"{choice.title()} module imported and executed!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# --- GUI Design ---
root = tk.Tk()
root.title("CALCAPP V1.18")
root.geometry("500x400")
root.configure(bg="#f4f4f9")

tk.Label(root, text="CALCAPP V1.18", font=("Arial", 20, "bold"), bg="#f4f4f9", fg="#4CAF50").pack(pady=10)
tk.Label(root, text="Choose a calculation:", font=("Arial", 14), bg="#f4f4f9").pack(pady=5)

calc_options = [
    'addition', 'subtraction', 'multiplication', 'division', 'modulus', 'floor division',
    'square root', 'power', 'logarithm', 'sine', 'cosine', 'tangent', 'mean', 'mode',
    'median', 'range', 'hyperbolic sine', 'hyperbolic cosine', 'hyperbolic tangent',
    'hyperbolic arcsine', 'hyperbolic arccosine', 'hyperbolic arctangent',
    'radian conversion', 'degree conversion'
]
calc_var = tk.StringVar(value="")

dropdown = tk.OptionMenu(root, calc_var, *calc_options)
dropdown.config(font=("Arial", 12), width=25)
dropdown.pack(pady=10)

tk.Button(root, text="Perform Calculation", font=("Arial", 14), bg="#4CAF50", fg="white",
          command=perform_calculation).pack(pady=20)

tk.Label(root, text="Thank you for using CALCAPP!\nMake sure to come back next time! Goodbye!\n((Refer a friend))",
         font=("Arial", 10), bg="#f4f4f9", fg="#333").pack(side="bottom", pady=20)

root.mainloop()
