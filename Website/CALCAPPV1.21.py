print("Hello, Welcome to CALCAPP")
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

def open_math_mentor_ai():
    mentor = tk.Toplevel(root)
    mentor.title("Math Mentor AI")
    mentor.geometry("400x400")
    mentor.configure(bg="#e3f2fd")

    tk.Label(mentor, text="Math Mentor AI", font=("Arial", 18, "bold"), fg="#1976d2", bg="#e3f2fd").pack(pady=10)
    tk.Label(mentor, text="Your personal AI math tutor for CALCAPP", font=("Arial", 12), bg="#e3f2fd").pack(pady=5)

    def show_explanation():
        calc = calc_entry.get().strip().lower()
        explanations = {
            "addition": "Adds two numbers together.",
            "subtraction": "Subtracts the second number from the first.",
            "multiplication": "Multiplies two numbers together.",
            "division": "Divides the first number by the second.",
            "modulus": "Finds the remainder when the first number is divided by the second.",
            "floor division": "Performs division and rounds down to the nearest whole number.",
            "square root": "Finds the square root of a number.",
            "power": "Raises a number to the power of another number.",
            "logarithm": "Finds the logarithm of a number to a specified base.",
            "sine": "Finds the sine of an angle (in degrees).",
            "cosine": "Finds the cosine of an angle (in degrees).",
            "tangent": "Finds the tangent of an angle (in degrees).",
            "mean": "Calculates the average of a list of numbers.",
            "mode": "Finds the most frequently occurring number(s) in a list.",
            "median": "Finds the middle value in a sorted list of numbers.",
            "range": "Calculates the difference between the largest and smallest numbers in a list.",
            "hyperbolic sine": "Finds the hyperbolic sine of an angle (in degrees).",
            "hyperbolic cosine": "Finds the hyperbolic cosine of an angle (in degrees).",
            "hyperbolic tangent": "Finds the hyperbolic tangent of an angle (in degrees).",
            "hyperbolic arcsine": "Finds the inverse hyperbolic sine of a number.",
            "hyperbolic arccosine": "Finds the inverse hyperbolic cosine of a number.",
            "hyperbolic arctangent": "Finds the inverse hyperbolic tangent of a number.",
            "radian conversion": "Converts an angle from degrees to radians.",
            "degree conversion": "Converts an angle from radians to degrees."
        }
        explanation = explanations.get(calc, "Sorry, I don't have an explanation for that calculation.")
        messagebox.showinfo("Explanation", explanation, parent=mentor)

    def show_example():
        calc = calc_entry.get().strip().lower()
        examples = {
            "addition": "Example: 5 + 3 = 8",
            "subtraction": "Example: 10 - 4 = 6",
            "multiplication": "Example: 7 * 2 = 14",
            "division": "Example: 20 / 4 = 5",
            "modulus": "Example: 10 % 3 = 1",
            "floor division": "Example: 10 // 3 = 3",
            "square root": "Example: √16 = 4",
            "power": "Example: 2^3 = 8",
            "logarithm": "Example: log(100, 10) = 2",
            "sine": "Example: sin(30°) = 0.5",
            "cosine": "Example: cos(60°) = 0.5",
            "tangent": "Example: tan(45°) = 1",
            "mean": "Example: Mean of [1, 2, 3] = 2",
            "mode": "Example: Mode of [1, 2, 2, 3] = 2",
            "median": "Example: Median of [1, 3, 2] = 2",
            "range": "Example: Range of [1, 3, 2] = 2 (3 - 1)",
            "hyperbolic sine": "Example: sinh(30°) = 0.547",
            "hyperbolic cosine": "Example: cosh(30°) = 1.140",
            "hyperbolic tangent": "Example: tanh(30°) = 0.462",
            "hyperbolic arcsine": "Example: arcsinh(1) = 0.881",
            "hyperbolic arccosine": "Example: arccosh(2) = 1.317",
            "hyperbolic arctangent": "Example: arctanh(0.5) = 0.549",
            "radian conversion": "Example: 180° = π radians",
            "degree conversion": "Example: π radians = 180°"
        }
        example = examples.get(calc, "Sorry, I don't have an example for that calculation.")
        messagebox.showinfo("Example", example, parent=mentor)

    def show_general_help():
        help_text = (
            "General Math Help:\n"
            "- Use addition, subtraction, multiplication, and division for basic arithmetic.\n"
            "- Use trigonometric functions (sine, cosine, tangent) for angles.\n"
            "- Use logarithms for exponential calculations.\n"
            "- Use mean, median, and mode for statistics.\n"
            "- Use hyperbolic functions for advanced math.\n"
        )
        messagebox.showinfo("General Math Help", help_text, parent=mentor)

    tk.Label(mentor, text="Type a calculation name for help:", font=("Arial", 12), bg="#e3f2fd").pack(pady=10)
    calc_entry = tk.Entry(mentor, font=("Arial", 12), width=25)
    calc_entry.pack(pady=5)

    tk.Button(mentor, text="Explain Calculation", font=("Arial", 12), bg="#1976d2", fg="white",
              command=show_explanation).pack(pady=5)
    tk.Button(mentor, text="Show Example", font=("Arial", 12), bg="#1976d2", fg="white",
              command=show_example).pack(pady=5)
    tk.Button(mentor, text="General Math Help", font=("Arial", 12), bg="#1976d2", fg="white",
              command=show_general_help).pack(pady=5)
    tk.Button(mentor, text="Close", font=("Arial", 12), command=mentor.destroy).pack(pady=15)

# --- GUI Design ---
root = tk.Tk()
root.title("CALCAPP V1.21")
root.geometry("500x400")
root.configure(bg="#f4f4f9")

tk.Label(root, text="CALCAPP V1.21", font=("Arial", 20, "bold"), bg="#f4f4f9", fg="#4CAF50").pack(pady=10)
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

button_frame = tk.Frame(root, bg="#f4f4f9")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Perform Calculation", font=("Arial", 14), bg="#4CAF50", fg="white",
          command=perform_calculation).grid(row=0, column=0, padx=10)

tk.Button(button_frame, text="Math Mentor AI", font=("Arial", 14), bg="#1976d2", fg="white",
          command=open_math_mentor_ai).grid(row=0, column=1, padx=10)

tk.Label(root, text="Thank you for using CALCAPP!\nMake sure to come back next time! Goodbye!\n((Refer a friend))",
         font=("Arial", 10), bg="#f4f4f9", fg="#333").pack(side="bottom", pady=20)

root.mainloop()
