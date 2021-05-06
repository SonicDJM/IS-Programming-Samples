"""
File: texteditor.py
Project 8.8
"""

from breezypythongui import EasyFrame
import tkinter.filedialog

class TextEditor(EasyFrame):
    """Demonstrates the use of a file dialog."""
    
    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, "Text Editor")
        # self.outputArea (text area)
        self.outputArea = self.addTextArea(text = "", row = 0, column = 0, columnspan = 3, width = 80, height = 15)
        # self.newButton (new file button)
        self.newButton = self.addButton(text = "New", row = 1, column = 0, command = self.newFile)
        # self.openButton (open file button)
        self.openButton = self.addButton(text = "Open", row = 1, column = 1, command = self.openFile)
        # self.saveButton (save file button)
        self.saveButton = self.addButton(text = "Save", row = 1, column = 2, command = self.saveFile, state = "disabled")

    # Event handling methods.
    def newFile(self):
        """Clears the text area and the title bar."""
        self.outputArea["text"] = ""
        self.__init__["title"] = ""
        pass

    def openFile(self):
        """Pops up an open file dialog, and if a file is
        selected, displays its text in the text area and
        its pathname in the title bar."""
        filename = tkinter.filedialog.askopenfile(parent = self, filetypes = "*.txt")
        print(filename) # DEBUG
        pass

    def saveFile(self):
        """Pops up an open file dialog, and saves
        the contents of the text area to the selected
        file name."""
        pass

def main():
    """Instantiate and pop up the window."""
    TextEditor().mainloop()

if __name__ == "__main__":
 main()
   
