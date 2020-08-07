from tkinter import *

windowWidth = 800
windowHeight = 800
root = Tk()

canvas = Canvas(root, width=windowWidth, height=windowHeight, borderwidth=0, highlightthickness=0, bg="#000050")
canvas.grid()
    
# this code runs whenever the mouse is clicked on the window
def mouse_pressed(event):
    # draws a dark blue background
    canvas.create_rectangle(0, 0, windowWidth, windowHeight, fill="#000050")
    # x and y will be equal to the mouse pointer's x and y location
    x = event.x
    y = event.y
    #x is 170
    #y is 220
    # this defines the x and y coordinated of all three points
    # of a triangle
    points = [x-70, y-160, x-20, y-70, x-120, y-70]
    canvas.create_oval(x-140, y-100, x, y, fill="red")
    canvas.create_oval(x-130, y-100, x-10, y-10, fill="orange")
    canvas.create_oval(x-120, y-100, x-20, y-20, fill="yellow")

    canvas.create_polygon(points, fill='gray', width=2) #draws triangle

    
    #1. Add details to your rocket to make it look better. You can look at rocket.png for inspiration.
    
    #2. Modify the locations of the shapes above so the rocket will be drawn where the mouse is clicked
    

canvas.bind("<Button-1>", mouse_pressed)

root.mainloop()