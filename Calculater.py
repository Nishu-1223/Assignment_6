import tkinter as tk
from tkinter import ttk

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

root = tk.Tk()
root.title("Simple Calculator")

display = ttk.Entry(root, width=20, font=("Arial", 16), justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Row 1
button_7 = ttk.Button(root, text="7", command=lambda: button_click(7))
button_7.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
button_8 = ttk.Button(root, text="8", command=lambda: button_click(8))
button_8.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
button_9 = ttk.Button(root, text="9", command=lambda: button_click(9))
button_9.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
button_divide = ttk.Button(root, text="/", command=lambda: button_click("/"))
button_divide.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")

# Row 2
button_4 = ttk.Button(root, text="4", command=lambda: button_click(4))
button_4.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
button_5 = ttk.Button(root, text="5", command=lambda: button_click(5))
button_5.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
button_6 = ttk.Button(root, text="6", command=lambda: button_click(6))
button_6.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
button_multiply = ttk.Button(root, text="*", command=lambda: button_click("*"))
button_multiply.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

# Row 3
button_1 = ttk.Button(root, text="1", command=lambda: button_click(1))
button_1.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
button_2 = ttk.Button(root, text="2", command=lambda: button_click(2))
button_2.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
button_3 = ttk.Button(root, text="3", command=lambda: button_click(3))
button_3.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
button_subtract = ttk.Button(root, text="-", command=lambda: button_click("-"))
button_subtract.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")

# Row 4
button_0 = ttk.Button(root, text="0", command=lambda: button_click(0))
button_0.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
button_decimal = ttk.Button(root, text=".", command=lambda: button_click("."))
button_decimal.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
button_add = ttk.Button(root, text="+", command=lambda: button_click("+"))
button_add.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

# Row 5
button_equal_sign = ttk.Button(root, text="=", command=button_equal)
button_equal_sign.grid(row=5, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")
button_clear_entry = ttk.Button(root, text="C", command=button_clear)
button_clear_entry.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

root.mainloop()