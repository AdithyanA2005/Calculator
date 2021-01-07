from PyQt5 import QtWidgets
from calculator.gui import Ui_MainWindow

class CalculatorWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def initialise (self):
        self.btn0.clicked.connect(self.digit_pressed)
        self.btn1.clicked.connect(self.digit_pressed)
        self.btn2.clicked.connect(self.digit_pressed)
        self.btn3.clicked.connect(self.digit_pressed)
        self.btn4.clicked.connect(self.digit_pressed)
        self.btn5.clicked.connect(self.digit_pressed)
        self.btn6.clicked.connect(self.digit_pressed)
        self.btn7.clicked.connect(self.digit_pressed)
        self.btn8.clicked.connect(self.digit_pressed)
        self.btn9.clicked.connect(self.digit_pressed)
        self.btnDot.clicked.connect(self.digit_pressed)
        self.btnPlus.clicked.connect(self.operand_pressed)
        self.btnDiv.clicked.connect(self.operand_pressed)
        self.btnMinus.clicked.connect(self.operand_pressed)
        self.btnMult.clicked.connect(self.operand_pressed)
        self.btnEqual.clicked.connect(self.equal_pressed)
        self.btnSquare.clicked.connect(self.square_pressed)
        self.btnPercent.clicked.connect(self.percent_pressed)
        self.btnClearAll.clicked.connect(self.clear_all)
        self.btnBack.clicked.connect(self.back_spacee)


    def digit_pressed(self):
        clickedButton = self.sender()
        digitValue = (clickedButton.text()) 
        display_text = self.calcDisplay.text() + str(digitValue)
        display_text = display_text.replace("ENTER NUMBERS", "")
        self.calcDisplay.setText(display_text)
        print(f"\nDigit pressed: {clickedButton}")
        print(f"Button pressed is {digitValue}")


    def clear_all(self):
        clickedButton = self.sender()
        print(f"\nButton pressed: {clickedButton}")
        print(f"Button pressed is clear_all")
        self.calcDisplay.setText("")
        self.calcDisplay.setText("ENTER NUMBERS")


    def back_spacee(self):
        clickedButton = self.sender()
        print(f"\nButton pressed: {clickedButton}")
        print(f"Button pressed is back_spacee")
        text = self.calcDisplay.text()
        text = text[:-1]
        self.calcDisplay.setText(text)
        print("One digit deleted")


    def operand_pressed(self):
        clickedButton = self.sender()
        btnValue = str(clickedButton.text()) 
        text = self.calcDisplay.text()
        print(f"\nButton pressed: {clickedButton}")
        print(f"Operation {btnValue}")   

        if btnValue == "+":
            text = text + " + "

        elif btnValue == "-":
            text = text + " - "

        elif btnValue == "÷":
            text = text + " / "

        elif btnValue == "×":
            text = text + " * "

        elif btnValue == "%":
            text = text + " % "

        else:
            print(f"You have a unrecognised Operation '{btnValue}'")

        self.calcDisplay.setText(text)


    def equal_pressed(self):

        try:
            text = self.calcDisplay.text()
            text.replace(" + ", "+")
            text.replace(" - ", "-")
            text.replace(" * ", "*")
            text.replace(" / ", "/")
            text.replace(" % ", "%")
            result = eval(text)
            result = str(result)
            self.calcDisplay.setText(result)

        except Exception as e:
            print(e)
            self.calcDisplay.setText("")

        
    def square_pressed(self):
        text = self.calcDisplay.text()
        result = eval(text)
        result = float(result)
        result = result ** 2
        result = str(result)
        self.calcDisplay.setText(result)


    def percent_pressed(self):
        text = self.calcDisplay.text()
        result = eval(text)
        result = float(result)
        result = result * 100
        result = str(result)
        self.calcDisplay.setText(result)
