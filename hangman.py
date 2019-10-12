#game logic
from tkinter import *
from helperMethods import *

class hangmanGame:
    phrase = ""
    wrongGuessCounter = 0
    maxWrongGuesses = 5
    guessedLetters = []

    def setAnswerPhrase(self, newPhrase):
        self.phrase = newPhrase

    def getAnswerPhrase(self, top):

        def submitPhrase():
            phrase = phraseEntry.get()
            self.phrase = phrase
            print("Phrase " + phrase + " assigned.")
            phraseW.destroy()
            row = 0
            i = 0
            for e in phrase:
                if (e == " "):
                    print('space found')
                    row = row + 1
                    print(row)
                    i = 0
                else:
                    letterLabel = Label(top, text=e, justify=RIGHT, width=1, padx=1, font=('bold', 18))
                    letterLabel.grid(row=row, column=1+i, padx=1, pady=1)
                    i = i + 1

        def tryToClose():
            #empty method to override windows "x" close
            return 0

        phraseW = Tk()
        phraseW.title("Enter an an answer phrase:")

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
        self.wrongGuessCounter = 0

    def getPhrase(self):
        return self.phrase

    def incWrongGuess(self):
        self.wrongGuessCounter += 1

    def getWrongGuessCount(self):
        return self.wrongGuessCounter

    def addToGuessedLetters(self, letter):
        self.guessedLetters.append(letter)

    def resetGuessedLetters(self):
        self.guessedLetters = []

    def checkGuessedLetters(self, letter):
        if letter in self.guessedLetters: return True
        else: return False

    def isOver(self):
        if (self.wrongGuessCounter == self.maxWrongGuesses): return True
        else: return False

    def __init__(self):
        self.phrase = ""
