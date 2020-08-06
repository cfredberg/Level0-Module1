from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    birthday = simpledialog.askstring(None, "Give me your birthday(mm/dd)")
    date = "08/06"
    if date == birthday:
        messagebox.showinfo(None, "Happy Birthday")
    else:
        messagebox.showinfo(None, "Happy UnBirthday")