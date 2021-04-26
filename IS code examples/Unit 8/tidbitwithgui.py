"""
File: tidbitwithgui.py
Project 8.7

GUI for tidbit program.

Inputs: purchase price and annual interest rate.
"""

from breezypythongui import EasyFrame


class TidbitGUI(EasyFrame):

    def __init__(self):
        """Set up the window and widgets."""
        EasyFrame.__init__(self, title="Tidbit Loan Scheduler")
        """Input fields"""
        self.addLabel(text="Purchase Price", row=0, column=0)
        self.priceField = self.addFloatField(value=0.0, row=0, column=1, precision=2)
        self.addLabel(text="Annual Interest Rate", row=1, column=0)
        self.rateField = self.addFloatField(value=0, row=1, column=1)
        """Command button"""
        self.button = self.addButton(text="Compute", row=2, column=0, columnspan=2,
                                     command=self.computeSchedule)
        """Output text box"""
        self.outputArea = self.addTextArea(text="", row=3, column=0, columnspan=2)

    def computeSchedule(self):
        """Event handler for the Compute button."""
        purchasePrice = self.priceField.getNumber()
        rate = float(self.rateField.getNumber() / 100)
        if purchasePrice == 0 or rate == 0:
            return
        output = Tidbit().paySchedule(purchasePrice, rate)
        self.outputArea.setText(output)


class Tidbit:

    def paySchedule(self, purchasePrice, rate):
        downPayment = purchasePrice * 0.1
        purchasePrice = purchasePrice - downPayment
        monthlyPayment = .05 * purchasePrice
        month = 0
        balance = purchasePrice
        output = "Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance\n"


        while True:
            month += 1
            interest = (balance * rate)/12
            principal = monthlyPayment - interest
            remaining = balance - principal
            output += "%2d%15.2f%15.2f%17.2f%17.2f%17.2f\n" % (month, balance, interest, principal, monthlyPayment, remaining)
            balance = remaining
            if monthlyPayment >= balance:
                month += 1
                interest = ((balance*rate)/12)/100
                monthlyPayment = balance + interest
                remaining = 0
                output += "%2d%15.2f%15.2f%17.2f%17.2f%17.2f\n" % (month, balance, interest, principal, monthlyPayment, remaining)
                break
        return output


def main():
    """Instantiate and pop up the window."""
    TidbitGUI().mainloop()


if __name__ == "__main__":
    main()
