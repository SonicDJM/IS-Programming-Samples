"""
File: crapsgui.py
Project 9.7
Pops up a window that allows the user to play the game of craps.
"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
from craps import Player
from die import Die

class CrapsGUI(EasyFrame):
   
    def __init__(self):
        """Creates the player, and sets up the Images and labels for the two dice to be displayed, the text area for the game state, and the two command buttons."""
        EasyFrame.__init__(self, title = "Craps Game")
        self.setSize(220, 320)
        """Instantiate the model and initial values of the dice"""
        self.die1 = Die()
        self.die2 = Die()
        self.rolls = []
        """Add labels and buttons to the view"""
        self.dieLabel1 = self.addLabel("", row = 0, column = 0, sticky = "NSEW")
        self.dieLabel2 = self.addLabel("", row = 0, column = 1, sticky = "NSEW")
        self.stateArea = self.addTextArea("", row = 1, column = 0, columnspan = 1)
        self.rollButton = self.addButton(text = "Roll", row = 2, column = 0, command = self.nextRoll)
        self.gameButton = self.addButton(text = "New game", row = 2, column = 1, command = self.newGame)
        self.refreshImages()

    def __str__(self):
        for (v1, v2) in self.rolls:
            result = result + str((v1, v2)) + " " + str(v1 + v2) + "\n"
        return result

    def nextRoll(self):
        """Rolls the dice and updates the view with
        the results."""
        self.die1.roll()
        self.die2.roll()
        (v1, v2) = (self.die1.getValue(), self.die2.getValue())
        self.rolls.append((v1, v2))

            
    def newGame(self):
        """Create a new craps game and updates the view."""
        self.die1 = Die()
        self.die2 = Die()
        self.rolls = []
        self.stateArea.setText("")
        self.rollButton["state"] = "normal"
        self.refreshImages()
        
    def refreshImages(self):
        """Updates the images in the window."""
        file1 = "DICE/" + str(self.die1) + ".gif"
        file2 = "DICE/" + str(self.die2) + ".gif"
        self.image1 = PhotoImage(file=file1)
        self.dieLabel1["image"] = self.image1
        self.image2 = PhotoImage(file=file2)
        self.dieLabel2["image"] = self.image2

def main():
    CrapsGUI().mainloop()

if __name__ == "__main__":
    main()
