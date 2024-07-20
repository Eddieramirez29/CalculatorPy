import tkinter as tk
import re  # Para usar la función "re.split()"

# Crear una instancia de la ventana principal
root = tk.Tk()
root.title("Ejemplo de Grid en Tkinter")

# Crear un campo de texto
entry = tk.Entry(root, font=("Arial", 24), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)  # Ubicar en la fila 0, columnas 0 a 2 con relleno

# Función para manejar la acción del botón
def on_button_click(text):
    current_text = entry.get()  # Obtener el texto actual del campo de entrada
    if text == "=":
        try:
            partes = re.split(r'(\D)', current_text)  # \D es cualquier carácter que no es un dígito

            if len(partes) >= 3:
                a = partes[0]  # Variable izquierda
                b = partes[1]  # Símbolo
                c = partes[2]  # Variable derecha

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

                entry.delete(0, tk.END)  # Limpiar el campo de entrada
                entry.insert(0, str(resultado))  # Mostrar el resultado
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

# Crear botones usando grid
button7 = tk.Button(root, text="7", command=lambda: on_button_click("7"))  # "7" es el argumento
button7.grid(row=1, column=0, padx=5, pady=5)  # Ubicar en la fila 1, columna 0 con relleno

button8 = tk.Button(root, text="8", command=lambda: on_button_click("8"))  # "8" es el argumento
button8.grid(row=1, column=1, padx=5, pady=5)  # Ubicar en la fila 1, columna 1 con relleno

button9 = tk.Button(root, text="9", command=lambda: on_button_click("9"))  # "9" es el argumento
button9.grid(row=1, column=2, padx=5, pady=5)  # Ubicar en la fila 1, columna 2 con relleno

buttonDel = tk.Button(root, text="DEL", command=lambda: on_button_click("DEL"))  # "DEL" es el argumento
buttonDel.grid(row=1, column=3, padx=5, pady=5)  # Ubicar en la fila 1, columna 3 con relleno

button4 = tk.Button(root, text="4", command=lambda: on_button_click("4"))  # "4" es el argumento
button4.grid(row=2, column=0, padx=5, pady=5)  # Ubicar en la fila 2, columna 0 con relleno

button5 = tk.Button(root, text="5", command=lambda: on_button_click("5"))  # "5" es el argumento
button5.grid(row=2, column=1, padx=5, pady=5)  # Ubicar en la fila 2, columna 1 con relleno

button6 = tk.Button(root, text="6", command=lambda: on_button_click("6"))  # "6" es el argumento
button6.grid(row=2, column=2, padx=5, pady=5)  # Ubicar en la fila 2, columna 2 con relleno

buttonDiv = tk.Button(root, text="/", command=lambda: on_button_click("/"))  # "/" es el argumento
buttonDiv.grid(row=2, column=3, padx=5, pady=5)  # Ubicar en la fila 2, columna 3 con relleno

button1 = tk.Button(root, text="1", command=lambda: on_button_click("1"))  # "1" es el argumento
button1.grid(row=3, column=0, padx=5, pady=5)  # Ubicar en la fila 3, columna 0 con relleno

button2 = tk.Button(root, text="2", command=lambda: on_button_click("2"))  # "2" es el argumento
button2.grid(row=3, column=1, padx=5, pady=5)  # Ubicar en la fila 3, columna 1 con relleno

button3 = tk.Button(root, text="3", command=lambda: on_button_click("3"))  # "3" es el argumento
button3.grid(row=3, column=2, padx=5, pady=5)  # Ubicar en la fila 3, columna 2 con relleno

buttonMult = tk.Button(root, text="*", command=lambda: on_button_click("*"))  # "*" es el argumento
buttonMult.grid(row=3, column=3, padx=5, pady=5)  # Ubicar en la fila 3, columna 3 con relleno

buttonPoint = tk.Button(root, text=".", command=lambda: on_button_click("."))  # "." es el argumento
buttonPoint.grid(row=4, column=0, padx=5, pady=5)  # Ubicar en la fila 4, columna 0 con relleno

buttonZero = tk.Button(root, text="0", command=lambda: on_button_click("0"))  # "0" es el argumento
buttonZero.grid(row=4, column=1, padx=5, pady=5)  # Ubicar en la fila 4, columna 1 con relleno

buttonPlus = tk.Button(root, text="+", command=lambda: on_button_click("+"))  # "+" es el argumento
buttonPlus.grid(row=4, column=2, padx=5, pady=5)  # Ubicar en la fila 4, columna 2 con relleno

buttonMinus = tk.Button(root, text="-", command=lambda: on_button_click("-"))  # "-" es el argumento
buttonMinus.grid(row=4, column=3, padx=5, pady=5)  # Ubicar en la fila 4, columna 3 con relleno

buttonEqual = tk.Button(root, text="=", command=lambda: on_button_click("="))  # "=" es el argumento
buttonEqual.grid(row=5, column=1, columnspan=2, padx=5, pady=5)  # Ubicar en la fila 5, columnas 1 a 2 con relleno

# Ejecutar el bucle principal de la ventana
root.mainloop()
