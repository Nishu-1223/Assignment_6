from tkinter import *

window=Tk()
window.geometry("300x400")

#EntryBox
e=Entry(window, width=35, borderwidth=5)
e.place(x=10,y=10)

#Buttons
def click(num):
    result=e.get()
    e.delete(0,END)
    e.insert(0, str(result)+str(num))

button_1=Button(window, text='1', padx=15, pady=10, command=lambda:click(1))
button_1.place(x=10,y=60)

button_2=Button(window, text='2', padx=15, pady=10, command=lambda:click(2))
button_2.place(x=80,y=60)

button_3=Button(window, text='3', padx=15, pady=10, command=lambda:click(3))
button_3.place(x=150,y=60)

button_4=Button(window, text='4', padx=15, pady=10, command=lambda:click(4))
button_4.place(x=10,y=110)

button_5=Button(window, text='5', padx=15, pady=10, command=lambda:click(5))
button_5.place(x=80,y=110)

button_6=Button(window, text='6', padx=15, pady=10, command=lambda:click(6))
button_6.place(x=150,y=110)

button_7=Button(window, text='7', padx=15, pady=10, command=lambda:click(7))
button_7.place(x=10,y=160)

button_8=Button(window, text='8', padx=15, pady=10, command=lambda:click(8))
button_8.place(x=80,y=160)

button_9=Button(window, text='9', padx=15, pady=10, command=lambda:click(9))
button_9.place(x=150,y=160)

button_0=Button(window, text='0', padx=15, pady=10, command=lambda:click(0))
button_0.place(x=10,y=210)

#operators
def add():
    n1=e.get()
    global math
    math= "addition"
    global i
    i=float(n1)
    e.delete(0, END)

button_add=Button(window, text='+', padx=15, pady=10, command=add)
button_add.place(x=80,y=210)

def sub():
    n1=e.get()
    global math
    math = "subtraction"
    global i
    i=float(n1)
    e.delete(0, END)

button_sub=Button(window, text='-', padx=15, pady=10, command=sub)
button_sub.place(x=150,y=210)

def mult():
    n1=e.get()
    global math
    math = "multiplication"
    global i
    i=float(n1)
    e.delete(0, END)

button_mult=Button(window, text='*', padx=15, pady=10, command=mult)
button_mult.place(x=10,y=260)

def div():
    n1=e.get()
    global math
    math = "division"
    global i
    i=float(n1)
    e.delete(0, END)

button_div=Button(window, text='/', padx=15, pady=10, command=div)
button_div.place(x=80,y=260)

def equal():
    n2=e.get()
    e.delete(0, END)
    try:
        if math=="addition":
            e.insert(0, i + float(n2))
        elif math=="subtraction":
            e.insert(0, i - float(n2))
        elif math=="multiplication":
            e.insert(0, i * float(n2))
        elif math=="division":
            if float(n2) == 0:
                e.insert(0, "Error: Division by zero")
            else:
                e.insert(0, i / float(n2))
    except NameError:
        e.insert(0, "Error: No operation selected")
    except ValueError:
        e.insert(0, "Error: Invalid input")

button_equal=Button(window, text='=', padx=15, pady=10, command= equal)
button_equal.place(x=150,y=260)

def clear():
    e.delete(0, END)

button_clear=Button(window, text='clear', padx=15, pady=10, command= clear)
button_clear.place(x=10,y=310)

mainloop()