from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    for i in range(4):
        name = simpledialog.askstring(None, "Name")
        if name.lower() == "dave":
            messagebox.showinfo(None, "Dave is an instructor for the League and knows a lot about coding")
        elif name.lower() == "charlie":
            messagebox.showinfo(None, "Charlie programmed this game")
        elif name.lower() == "lucas":
            messagebox.showinfo(None, "Doesn't care what goes here")
        elif name.lower() == "zach":
            messagebox.showinfo(None, "Python doesn't work for him")
