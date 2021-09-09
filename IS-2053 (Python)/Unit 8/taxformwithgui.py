"""
File: taxformwithgui.py
Project 8.1
A GUI-based tax calculator.

Computes and prints the total tax, given the income and
number of dependents (inputs), and a standard deduction of
$10,000, an exemption amount of $3,000, and a flat tax rate
of 20%.
"""

from breezypythongui import EasyFrame

class TaxCalculator(EasyFrame):
    """Application window for the tax calculator."""

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = "Tax Calculator")

        # Label and field for the income
        self.addLabel(text = "Gross Income", row = 0, column = 0, sticky = "NSEW")
        self.incomeField = self.addFloatField(value = 0.0, row = 0, column = 1)

        # Label and field for the number of dependents
        self.addLabel(text = "Dependence", row = 1, column = 0, sticky = "NSEW")
        self.depField = self.addIntegerField(value = 0, row = 1, column = 1)

        # The command button
        self.addButton(text = "Calculate", row = 3, column = 1, state = "normal", command = self.computeTax)

        # Label and field for the tax
        self.addLabel(text = "Total tax", row = 4, column = 0, sticky = "NSEW")
        self.taxField = self.addFloatField(value = 0, row = 4, column = 1, precision = 2, state = "readonly")

    # The event handler method for the button
    def computeTax(self):
        """Obtains the data from the input field and uses
        them to compute the tax, which is sent to the
        output field."""
        # Initialize the constants
        TAX_RATE = 0.20
        STANDARD_DEDUCTION = 10000.0
        DEPENDENT_DEDUCTION = 3000.0
        grossIncome = self.incomeField.getNumber()
        numDependents = self.depField.getNumber()
        # Compute the income tax
        taxableIncome = grossIncome - STANDARD_DEDUCTION - \
                    DEPENDENT_DEDUCTION * numDependents
        incomeTax = taxableIncome * TAX_RATE
        self.taxField.setNumber(incomeTax)
        pass
        
        
def main():
    TaxCalculator().mainloop()

if __name__ == "__main__":
    main()

