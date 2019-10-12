from tkinter import *
from hangman import *
#methods parted out into smaller methods for readability and versatility

def doNothing():
    #this method does nothing but replace the window closing protocol
    return 0

def placePhrase(top, phrase, guessedLetters, phraseLabels):
    row = 0
    for e in phrase:
        if (e == " "): ++row
        else:
            letterLabel = Label(top, text=e, justify=CENTER, width=3,padx=3)
            letterLabel.grid(row=0, column=1, padx=1, pady=1)


