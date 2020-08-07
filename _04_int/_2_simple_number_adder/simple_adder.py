# Write a Python program that asks the user for two numbers. 
# Then display the sum of the two numbers
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    num1 = simpledialog.askinteger(None, "num1")
    num2 = simpledialog.askinteger(None, "num2")
    messagebox.showinfo(None, num1 + num2)