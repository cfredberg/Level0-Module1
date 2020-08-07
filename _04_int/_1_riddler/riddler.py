from tkinter import messagebox, simpledialog, Tk

'''
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got correct
'''

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    score = 0
    riddle1 = simpledialog.askstring(None, "How do you spell COW in thirteen letters?")
    riddle2 = simpledialog.askstring(None, "David's father has three sons: Snap, Crackle, and _____?")
    riddle3 = simpledialog.askstring(None, "What is more useful when it is broken?")

    if riddle1.lower() == "see o double you":
        score+=1
    else:
        messagebox.showinfo(None, "The correct answer is 'see o double you'")
    if riddle2.lower() == "david":
        score+=1
    else:
        messagebox.showinfo(None, "The correct answer is 'david'")
    if 'egg' in riddle3.lower():
        score+=1
    else:
        messagebox.showinfo(None, "The correct answer is 'an egg'")
    messagebox.showinfo(None, score)