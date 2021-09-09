"""
File: temperatureconverter.py
Project 8.3
Temperature conversion between Fahrenheit and Celsius.
Illustrates the use of numeric data fields.
"""

from breezypythongui import EasyFrame

class TemperatureConverter(EasyFrame):
    """A termperature conversion program."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title = "Temperature Converter")

        # self.addLabel (Label for Celsius)
        self.addLabel(text = "Celsius", row = 0, column = 1, sticky = "NSEW")
        # self.celsiusField (Celsius field)
        self.celsiusField = self.addFloatField(value = 0.0, row = 1, column = 1, precision = 1)
        # self.addLabel (Label for Fahrenheit)
        self.addLabel(text = "Fahrenheit", row = 0, column = 2, sticky = "NSEW")
        # self.fahrField (Fahrenheit field)
        self.fahrField = self.addFloatField(value = 32.0, row = 1, column = 2, precision = 1)
        # self.addButton (Celsius button)
        self.addButton(text = ">>>>", row = 2, column = 1, command = self.computeFahr)
        # self.addButton (Fahrenheit button)
        self.addButton(text = "<<<<", row = 2, column = 2, command = self.computeCelsius)

    # The controller methods
    def computeFahr(self):
        """Inputs the Celsius degrees
        and outputs the Fahrenheit degrees."""
        initTemp = self.celsiusField.getNumber()
        finalTemp = (initTemp * 1.8) + 32
        self.fahrField.setNumber(finalTemp)
      

    def computeCelsius(self):
        """Inputs the Fahrenheit degrees
        and outputs the Celsius degrees."""
        initTemp = self.fahrField.getNumber()
        finalTemp = (initTemp - 32) * .5556
        self.celsiusField.setNumber(finalTemp)
        
        
def main():
    """Instantiate and pop up the window."""
    TemperatureConverter().mainloop()

if __name__ == "__main__":
    main()

