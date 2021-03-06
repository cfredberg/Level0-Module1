from tkinter import simpledialog, messagebox, Tk, Canvas

windowWidth = 600
windowHeight = 600

root = Tk()

canvas = Canvas(root, width=windowWidth, height=windowHeight, bg="#DDDDDD")
canvas.grid()

#1. Ask the user what color tomato they would like and save their response   
#   You can give them up to three choices 
tomato = simpledialog.askstring(None, "Red, Green, or Blue")

#2. use if-else statements to draw the tomato in the color that they chose
#   you can modify the code below or draw your own tomato
if tomato.lower() == "red":
    canvas.create_oval(75, 200, 400, 450, fill="red", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="red", outline="")


    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
elif tomato.lower() == "green":
    canvas.create_oval(75, 200, 400, 450, fill="green", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="green", outline="")

    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
else:
    canvas.create_oval(75, 200, 400, 450, fill="blue", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="blue", outline="")

    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
    




root.mainloop()
