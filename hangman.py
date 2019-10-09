#game logic
from tkinter import *
from helperMethods import *

class hangmanGame:
    phrase = ""

    def setAnswerPhrase(self, newPhrase):
        self.phrase = newPhrase

    def getAnswerPhrase(self):

        def submitPhrase():
            phrase = phraseEntry.get()
            self.phrase = phrase
            print("Phrase " + phrase + " assigned.")
            phraseW.destroy()

        def tryToClose():
            return 0

        phraseW = Tk()

        # Gets h/w
        windowWidth = phraseW.winfo_reqwidth()
        windowHeight = phraseW.winfo_reqheight()

        # Gets screen w/h as relevant to need
        positionRight = int(phraseW.winfo_screenwidth() / 2 - windowWidth / 2)
        positionDown = int(phraseW.winfo_screenheight() / 2 - windowHeight / 2)

        # Position window in the center of the page
        phraseW.geometry("+{}+{}".format(positionRight, positionDown))
        phraseW.protocol("WM_DELETE_WINDOW", tryToClose)
        phraseLabel = Label(phraseW, text="Answer Phrase: ")
        phraseLabel.pack(side=LEFT)
        phraseEntry = Entry(phraseW, bd=5, )
        phraseEntry.pack(side=RIGHT)
        phraseSubmit = Button(phraseW, text="Submit", command = submitPhrase)
        phraseSubmit.pack(side=RIGHT)





    def askForPhrase(self):
        phrase = ""
        #get input from GUI
        return phrase

    def resetGame(self):
        self.phrase = ""

    def getPhrase(self):
        return self.phrase

    def __init__(self):
        self.phrase = ""
