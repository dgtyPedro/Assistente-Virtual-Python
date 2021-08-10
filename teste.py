from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from assistentepython import Ui_Dialog



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
            
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    
    sys.exit(app.exec())
