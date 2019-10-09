#The hangman interface
from tkinter import *
from helperMethods import *
from tkinter import ttk

game = hangmanGame
game.getAnswerPhrase(game)

root = Tk()
root.title("Hangman")
root.resizable(0,0)
#make a grid
# Gets h/w
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()

# Gets screen w/h as relevant to need
positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

# Position window in the center of the page
root.geometry("+{}+{}".format(positionRight, positionDown))

#mainFrame = ttk.Frame(root, padding = "3 3 12 12")
#ttk.Button(mainFrame, text="WHATS UP B").grid()

i = 0
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for each in range(0, 26):
    print(alphabet[i])
    print(i)
    button = Button(root, text = alphabet[i], justify = CENTER, width = 3, padx = 3)
    button.pack(side = LEFT)
    i = i + 1
    #make one button per letter w/ unique key and add to window
    #can probably use the text label on the button to get the letter to search for

root.mainloop()
