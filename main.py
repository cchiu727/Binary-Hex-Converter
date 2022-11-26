import sys

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel,
    QVBoxLayout, QComboBox, QLineEdit
)
from PyQt5.QtCore import Qt, QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Decimal Binary Hex Converter")
        
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

        # answer label
        outputLabel = QLabel("???")
        outputLabel.setAlignment(Qt.AlignHCenter)
        layout.addWidget(outputLabel)



    # for prompt combo box
    def combo_index_changed(self, i):
        print(i)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()