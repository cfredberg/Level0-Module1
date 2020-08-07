# Write a Python program that asks the user for two numbers.
# Then ask the user if the would like to add, subtract, multiply, or divide.
# Use if-else statements to provide the desired math operation on the numbers and display the result.
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    num1 = simpledialog.askfloat(None, "num1")
    num2 = simpledialog.askfloat(None, "num2")
    thing = simpledialog.askstring(None, "+, -, *, or /")
    if thing == "+":
        messagebox.showinfo(None, num1 + num2)
    elif thing == "-":
        messagebox.showinfo(None, num1 - num2)
    elif thing == "*":
        messagebox.showinfo(None, num1 * num2)
    elif thing == "/":
        messagebox.showinfo(None, num1 / num2)