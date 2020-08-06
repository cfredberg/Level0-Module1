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
    score = 0
    riddle1 = simpledialog.askstring(None, "What has six faces, but does not wear makeup, has twenty-one eyes, but cannot see? What is it?")
    riddle2 = simpledialog.askstring(None, "David's father has three sons: Snap, Crackle, and _____?")
    riddle3 = simpledialog.askstring(None, "What is more useful when it is broken?")

    if riddle1 == "a die":
        score+=1
    if riddle2 == "david":
        score+=1
    if riddle3 == "an egg":
        score+=1
    messagebox.showinfo(None, score)