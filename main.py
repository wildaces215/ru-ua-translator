

from argostranslate import package, translate
from PyQt5.QtWidgets import QApplication, QWidget
import sys
#Local Imports
#from translate import RuTranslate

class MainScreen(QWidget):
    def __init__(self):
         super().__init__()
         self.initUI()
    def GUI(self):
        
        self = QWidget()
        
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Simple')
        self.show()
        
    def initUI(self):
    
        self.setGeometry(300, 300, 300, 220)
        
        self.show()



def main():
    
    app = QApplication(sys.argv)
    ex = MainScreen()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()