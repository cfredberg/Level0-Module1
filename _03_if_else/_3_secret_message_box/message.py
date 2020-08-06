from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    message = simpledialog.askstring(None, "Enter a secret message")
    guess = simpledialog.askstring(None, "Guess the password")
    password = "GuessMeIfYouCan"

    if guess == password:
        messagebox.showinfo(None, message)
    else:
        messagebox.showinfo(None, "WRONG!")