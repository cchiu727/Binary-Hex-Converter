import sys

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel,
    QVBoxLayout, QComboBox, QLineEdit, QPushButton
)
from PyQt5.QtCore import Qt, QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Decimal Binary Hex Converter")

        # keeps track of input and output choices
        self.inputChoice = 0
        self.outputChoice = 0
        self.outputVal = 0
        
        # layout
        layout = QVBoxLayout()
        layoutWidget = QWidget()
        layoutWidget.setLayout(layout)
        self.setCentralWidget(layoutWidget)

        # prompt combo boxfor user to choose input type
        promptCombo = QComboBox()
        promptCombo.addItems(["Decimal", "Binary", "Hexadecimal"])
        promptCombo.setEditable(False)
        layout.addWidget(promptCombo)

        # text field for user to input value
        inputLine = QLineEdit()
        inputLine.setMaxLength(16)
        inputLine.setPlaceholderText("Enter your value:")
        layout.addWidget(inputLine)

        # answer combo box for user to choose output type
        outputCombo = QComboBox()
        outputCombo.addItems(["Decimal", "Binary", "Hexadecmial"])
        outputCombo.setEditable(False)
        layout.addWidget(outputCombo)
        
        # button to show answer
        outputButton = QPushButton("Convert")
        outputButton.clicked.connect(self.convert)
        layout.addWidget(outputButton)

        # answer label
        outputLabel = QLabel("???")
        outputLabel.setAlignment(Qt.AlignHCenter)
        layout.addWidget(outputLabel)

    


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()