#The hangman interface
from tkinter import *
from helperMethods import *
from tkinter import ttk
from checkForLetter import *
from PIL import Image, ImageTk
import random
######################################################################################################################
game = hangmanGame
alphaButtons = []
phraseLabels = []
stages = []
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

root = Tk()
root.title("Hangman")
root.geometry("500x500")
root.resizable(0, 0)

im_temp = Image.open("tileBackground2.gif")
im_temp = im_temp.resize((500, 500), Image.ANTIALIAS)

backgroundIMG = ImageTk.PhotoImage(Image.open("tileBackground2.gif"), master=root)
backgroundLBL = Label(root, image=backgroundIMG)
backgroundLBL.image = backgroundIMG
backgroundLBL.place(x=0, y=0, relwidth=1, relheight=1)

top = Frame(root)
top.pack(side=TOP)
bottom = Frame(root)
bottom.pack(side = BOTTOM)
subTopCenter = Frame(top)
subTopTop = Frame(top)
subTopCenter.grid(row=1,column=0,padx=1,pady=1)
subTopTop.grid(row=0,column=0,padx=1,pady=1)



stage0 = ImageTk.PhotoImage(Image.open("stages\stage0gif.gif"), master=subTopTop)
stageLBL = Label(subTopTop, image=stage0)
stageLBL.image = stage0
stageLBL.place(x=0, y=0, relwidth=.5, relheight=.5)


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

def letterCheck(index, letter):
    found = checkForLetter(game.getPhrase(game), letter)
    game.addToGuessedLetters(game, letter)
    alphaButtons[index].config(state="disabled")
    if (found): alphaButtons[index].config(bg="green")
    else:
        alphaButtons[index].config(bg="red")
        game.incWrongGuess(game)
    if (game.isOver(game)): print ('GAMEOVER')#call gameOver function

def pickRandom():
    index = random.randint(0,25)
    letter = alphabet[index]
    while (game.checkGuessedLetters(game, letter) == True):
        index = random.randint(0, 25)
        letter = alphabet[index]
    letterCheck(index, letter)

def hoverOn(e, i):
    if alphaButtons[i]['state'] == NORMAL:
        alphaButtons[i].config(bg="yellow")

def hoverOff(e, i):
    if alphaButtons[i]['state'] == NORMAL:
        alphaButtons[i].config(bg="SystemButtonFace")

def hoverOnRandom(e, self):
    self.config(bg="yellow")

def hoverOffRandom(e, self):
        self.config(bg="SystemButtonFace")


i = 0
for each in range(0, 26):
    letter = alphabet[i]
    button = Button(bottom, text = alphabet[i], justify = CENTER, width = 3, padx = 3, command=lambda index = i, letter = alphabet[i] : letterCheck(index, letter))
    button.bind("<Enter>", lambda event, index = i : hoverOn(event, index))
    button.bind("<Leave>", lambda event, index = i : hoverOff(event, index))
    if (i <= 8): button.grid(row = 0, column = i, padx = 0.5, pady= 0.5)
    elif ((i > 8) and (i <= 17)): button.grid(row = 1, column = (i-9), padx = 0.5, pady= 0.5)
    elif (i > 17): button.grid(row = 2, column = (i-18), padx = .5, pady= 0.5)
    alphaButtons.append(button)
    i = i + 1
    #make one button per letter w/ unique key and add to window
    #can probably use the text label on the button to get the letter to search for
pickRandomButton = Button(bottom, text = "??", justify = CENTER, width = 3, padx = 3, command = pickRandom)
pickRandomButton.grid(row = 2, column = 8, padx = .5, pady = .5)
pickRandomButton.bind("<Enter>", lambda event, button = pickRandomButton : hoverOnRandom(event, button))
pickRandomButton.bind("<Leave>", lambda event, button = pickRandomButton : hoverOffRandom(event, button))

game.getAnswerPhrase(game, subTopCenter)

root.mainloop()
