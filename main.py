from calculator.gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from calculator.calculator import CalculatorWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    calculator = CalculatorWindow()
    calculator.show()
    # MainWa]indow = QtWidgets.QMainWindow()
    # ui = CalculatorWindow()
    # ui.setupUi(calculator)
    # calculator.show()
    sys.exit(app.exec_())
	# MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()