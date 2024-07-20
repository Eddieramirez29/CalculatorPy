import tkinter as tk
import re  # To use the "re.split()" function

# Create an instance of the main window
root = tk.Tk()
root.title("Basic Calculator In Tkinter")

# Create a text field
entry = tk.Entry(root, font=("Arial", 24), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)  # Place in row 0, columns 0 to 2 with padding

# Function to handle button click actions
def on_button_click(text):
    current_text = entry.get()  # Get the current text from the input field
    if text == "=":
        try:
            partes = re.split(r'(\D)', current_text)  # \D is any character that is not a digit

            if len(partes) >= 3:
                a = partes[0]  # Left variable
                b = partes[1]  # Operator
                c = partes[2]  # Right variable

                if b == "+":
                    resultado = float(a) + float(c)
                elif b == "-":
                    resultado = float(a) - float(c)
                elif b == "*":
                    resultado = float(a) * float(c)
                elif b == "/":
                    resultado = float(a) / float(c)
                else:
                    resultado = "Error"

                entry.delete(0, tk.END)  # Clear the input field
                entry.insert(0, str(resultado))  # Display the result
            else:
                entry.delete(0, tk.END)
                entry.insert(0, "Error")
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif text == "DEL":
        entry.delete(len(current_text) - 1, tk.END)
    else:
        entry.insert(tk.END, text)

# Create buttons using grid
button7 = tk.Button(root, text="7", command=lambda: on_button_click("7"))  # "7" is the argument
button7.grid(row=1, column=0, padx=5, pady=5)  # Place in row 1, column 0 with padding

button8 = tk.Button(root, text="8", command=lambda: on_button_click("8"))  # "8" is the argument
button8.grid(row=1, column=1, padx=5, pady=5)  # Place in row 1, column 1 with padding

button9 = tk.Button(root, text="9", command=lambda: on_button_click("9"))  # "9" is the argument
button9.grid(row=1, column=2, padx=5, pady=5)  # Place in row 1, column 2 with padding

buttonDel = tk.Button(root, text="DEL", command=lambda: on_button_click("DEL"))  # "DEL" is the argument
buttonDel.grid(row=1, column=3, padx=5, pady=5)  # Place in row 1, column 3 with padding

button4 = tk.Button(root, text="4", command=lambda: on_button_click("4"))  # "4" is the argument
button4.grid(row=2, column=0, padx=5, pady=5)  # Place in row 2, column 0 with padding

button5 = tk.Button(root, text="5", command=lambda: on_button_click("5"))  # "5" is the argument
button5.grid(row=2, column=1, padx=5, pady=5)  # Place in row 2, column 1 with padding

button6 = tk.Button(root, text="6", command=lambda: on_button_click("6"))  # "6" is the argument
button6.grid(row=2, column=2, padx=5, pady=5)  # Place in row 2, column 2 with padding

buttonDiv = tk.Button(root, text="/", command=lambda: on_button_click("/"))  # "/" is the argument
buttonDiv.grid(row=2, column=3, padx=5, pady=5)  # Place in row 2, column 3 with padding

button1 = tk.Button(root, text="1", command=lambda: on_button_click("1"))  # "1" is the argument
button1.grid(row=3, column=0, padx=5, pady=5)  # Place in row 3, column 0 with padding

button2 = tk.Button(root, text="2", command=lambda: on_button_click("2"))  # "2" is the argument
button2.grid(row=3, column=1, padx=5, pady=5)  # Place in row 3, column 1 with padding

button3 = tk.Button(root, text="3", command=lambda: on_button_click("3"))  # "3" is the argument
button3.grid(row=3, column=2, padx=5, pady=5)  # Place in row 3, column 2 with padding

buttonMult = tk.Button(root, text="*", command=lambda: on_button_click("*"))  # "*" is the argument
buttonMult.grid(row=3, column=3, padx=5, pady=5)  # Place in row 3, column 3 with padding

buttonPoint = tk.Button(root, text=".", command=lambda: on_button_click("."))  # "." is the argument
buttonPoint.grid(row=4, column=0, padx=5, pady=5)  # Place in row 4, column 0 with padding

buttonZero = tk.Button(root, text="0", command=lambda: on_button_click("0"))  # "0" is the argument
buttonZero.grid(row=4, column=1, padx=5, pady=5)  # Place in row 4, column 1 with padding

buttonPlus = tk.Button(root, text="+", command=lambda: on_button_click("+"))  # "+" is the argument
buttonPlus.grid(row=4, column=2, padx=5, pady=5)  # Place in row 4, column 2 with padding

buttonMinus = tk.Button(root, text="-", command=lambda: on_button_click("-"))  # "-" is the argument
buttonMinus.grid(row=4, column=3, padx=5, pady=5)  # Place in row 4, column 3 with padding

buttonEqual = tk.Button(root, text="=", command=lambda: on_button_click("="))  # "=" is the argument
buttonEqual.grid(row=5, column=1, columnspan=2, padx=5, pady=5)  # Place in row 5, columns 1 to 2 with padding

# Run the main loop of the window
root.mainloop()