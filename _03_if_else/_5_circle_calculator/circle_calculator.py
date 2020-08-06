from tkinter import simpledialog, messagebox, Tk, Canvas
import math

# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    radius = simpledialog.askinteger(None, None)
    aoc = simpledialog.askstring(None, "a or c")
    if aoc == "a":
        messagebox.showinfo(None, str(math.pi*radius**2))
    else:
        messagebox.showinfo(None, str(2*math.pi*radius))

#Area = πr^2
#Circumference = 2πr 