from PyQt5.QtWidgets import QWidget, QApplication
import sys

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__()

root = QApplication(sys.argv)
app = Window()
app.show()
sys.exit(root.exec_())