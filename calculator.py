import tkinter as tk
from tkinter import messagebox
import math

# -----------------------------
# Window
# -----------------------------
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("500x700")
root.resizable(False, False)
root.configure(bg="#1E1E1E")

expression = ""
memory = 0

# -----------------------------
# Display
# -----------------------------
display = tk.Entry(
    root,
    font=("Arial", 24),
    bd=8,
    relief="sunken",
    justify="right",
    bg="white"
)
display.pack(fill="both", padx=10, pady=10, ipady=15)


# -----------------------------
# Functions
# -----------------------------
def update(value):
    global expression
    expression += str(value)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)


def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)


def backspace():
    global expression
    expression = expression[:-1]
    display.delete(0, tk.END)
    display.insert(0, expression)


def equal():
    global expression
    try:
        result = str(eval(expression))
        display.delete(0, tk.END)
        display.insert(0, result)
        expression = result
    except:
        messagebox.showerror("Error", "Invalid Expression")
        clear()


# -----------------------------
# Scientific Functions
# -----------------------------
def sqrt():
    global expression
    try:
        result = math.sqrt(float(display.get()))
        clear()
        update(result)
    except:
        messagebox.showerror("Error", "Invalid Input")


def square():
    global expression
    try:
        result = float(display.get()) ** 2
        clear()
        update(result)
    except:
        messagebox.showerror("Error", "Invalid Input")


def cube():
    global expression
    try:
        result = float(display.get()) ** 3
        clear()
        update(result)
    except:
        messagebox.showerror("Error", "Invalid Input")


def reciprocal():
    global expression
    try:
        result = 1 / float(display.get())
        clear()
        update(result)
    except:
        messagebox.showerror("Error", "Cannot Divide by Zero")


def factorial():
    global expression
    try:
        result = math.factorial(int(float(display.get())))
        clear()
        update(result)
    except:
        messagebox.showerror("Error", "Invalid Input")


def percent():
    global expression
    try:
        result = float(display.get()) / 100
        clear()
        update(result)
    except:
        messagebox.showerror("Error", "Invalid Input")


def pi():
    clear()
    update(math.pi)


def e():
    clear()
    update(math.e)


def sin():
    clear()
    update(math.sin(math.radians(float(display.get()))))


def cos():
    clear()
    update(math.cos(math.radians(float(display.get()))))


def tan():
    clear()
    update(math.tan(math.radians(float(display.get()))))


def log():
    clear()
    update(math.log10(float(display.get())))


def ln():
    clear()
    update(math.log(float(display.get())))


# -----------------------------
# Memory Functions
# -----------------------------
def ms():
    global memory
    memory = float(display.get())


def mr():
    clear()
    update(memory)


def mc():
    global memory
    memory = 0


def mplus():
    global memory
    memory += float(display.get())


def mminus():
    global memory
    memory -= float(display.get())


# -----------------------------
# Buttons
# -----------------------------
frame = tk.Frame(root, bg="#1E1E1E")
frame.pack()

buttons = [

["MC","MR","MS","M+","M-"],

["√","x²","x³","1/x","%"],

["sin","cos","tan","log","ln"],

["7","8","9","/","C"],

["4","5","6","*","←"],

["1","2","3","-","("],

["0",".","=","+",")"],

["π","e","!","",""]

]

# -----------------------------
# Button Commands
# -----------------------------
for r,row in enumerate(buttons):
    for c,text in enumerate(row):

        if text=="":
            continue

        cmd=None

        if text=="=":
            cmd=equal

        elif text=="C":
            cmd=clear

        elif text=="←":
            cmd=backspace

        elif text=="√":
            cmd=sqrt

        elif text=="x²":
            cmd=square

        elif text=="x³":
            cmd=cube

        elif text=="1/x":
            cmd=reciprocal

        elif text=="%":
            cmd=percent

        elif text=="π":
            cmd=pi

        elif text=="e":
            cmd=e

        elif text=="sin":
            cmd=sin

        elif text=="cos":
            cmd=cos

        elif text=="tan":
            cmd=tan

        elif text=="log":
            cmd=log

        elif text=="ln":
            cmd=ln

        elif text=="!":
            cmd=factorial

        elif text=="MC":
            cmd=mc

        elif text=="MR":
            cmd=mr

        elif text=="MS":
            cmd=ms

        elif text=="M+":
            cmd=mplus

        elif text=="M-":
            cmd=mminus

        else:
            cmd=lambda t=text:update(t)

        tk.Button(
            frame,
            text=text,
            command=cmd,
            width=8,
            height=3,
            font=("Arial",14),
            bg="#333333",
            fg="white",
            activebackground="#555555"
        ).grid(row=r,column=c,padx=3,pady=3)

root.mainloop()