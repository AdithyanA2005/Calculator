from calculator.gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from calculator.calculator import CalculatorWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    calculator = CalculatorWindow()
    ui = CalculatorWindow()
    ui.setupUi(calculator)
    ui.initialise()
    calculator.show()
    sys.exit(app.exec_())
    