import string
from PySide2.QtGui import QKeyEvent
from PySide2.QtWidgets import (QApplication, QWidget,
                               QPushButton, QTextEdit,
                               QLabel, QMessageBox, QVBoxLayout,
                               QComboBox)

class TextEdit(QTextEdit):
    def __init__(self):
        super().__init__()

    def keyPressEvent(self, e: QKeyEvent) -> None:
        if e.text() in "01234567890 .e":
            self.insertPlainText(e.text())
            return
        
        elif e.text() in string.ascii_letters:
            return
        else:
            super().keyPressEvent(e)

class Main(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.number_field = TextEdit()
        self.number_field.setPlaceholderText("Enter numbers (Split with space)")

        self.operator_selector = QComboBox()
        self.operator_selector.addItems(["Add", "Subtract", "Multiply", "Divide"])

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate)

        self.layout.addWidget(self.number_field)
        self.layout.addWidget(self.operator_selector)
        self.layout.addWidget(self.calculate_button)

    def calculate(self):
        list_of_numbers = []

        for n in self.number_field.toPlainText().split(" "):
            if n in (' ', ''):
                continue

            output = None
            try:
                output = eval(n)

            except Exception:
                print("fatal error")
                quit(1)

            list_of_numbers.append(float(output))
        
        ops = {
            "add": '+',
            "subtract": '-',
            "multiply": '*',
            "divide": '/'
        }
        operator = self.operator_selector.currentText()
        QMessageBox.information(self, "Results", str(sum(list_of_numbers)) if operator == 'Add' else str(self.calc(list_of_numbers, ops.get(operator.lower()))))

    def calc(self, nums, op):
        output = nums[0]

        output = eval(f"output {op} {op.join([str(n) for n in nums[1:]])}")

        return output

app = QApplication([])
main = Main()
main.setWindowTitle("Calculator")
main.resize(800, 400)

main.show()
app.exec_()