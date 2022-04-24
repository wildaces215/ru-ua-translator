

from argostranslate import package, translate
from PyQt5.QtWidgets import QApplication,QSystemTrayIcon, QWidget,QLabel,QGridLayout,QTextEdit,QPushButton,QComboBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon




import sys

#Local Imports
from translate import Translator

class MainScreen(QWidget):
    def __init__(self):
         super().__init__()
         self.GUI()
    def GUI(self):
        
        
        self.setWindowIcon(QIcon('icon.png'))        
        

        grid = QGridLayout()
        
        self.setLayout(grid)

        self.setGeometry(600, 400, 600, 400)
        
        self.setWindowTitle("English Translator")

        self.selectedLangauge = QComboBox()

        self.selectLangauge.addItems(["Ukranian","Russian"])
        
        self.leftTextBox = QTextEdit(self)
        self.rightTextBox = QTextEdit(self) 
        
        self.translateButton = QPushButton("Translate")
        
        self.createDBButton = QPushButton("Create Database")
        self.addToDatabase = QPushButton("Add Entry to Database")
        self.exportDatabase = QPushButton("Export Database")

        grid.addWidget(self.leftTextBox,0,0)
        grid.addWidget(self.translateButton,0,1)
        grid.addWidget(self.rightTextBox,0,2)

       
        #grid.addWidget(self.addToDatabase,1,0)
        #grid.addWidget(self.exportDatabase,1,1)

        #Actions
        self.translateButton.clicked.connect(self.translate_action)
        self.addToDatabase.clicked.connect(self.add_to_db)
        
        self.show()
   
    @pyqtSlot()
    def translate_action(self):
        original_text = self.leftTextBox.toPlainText()
        if original_text == None:
            pass
        
        translator = Translator()
        translated_text=translator.translateRussianText(original_text)
        self.rightTextBox.clear()
        self.rightTextBox.append(translated_text)
        
    @pyqtSlot()
    def add_to_db(self):
        print("The add to db button was called.")
    
    @pyqtSlot()
    def export_db(self):
        print("The export to db was called!")


def main():
    
    app = QApplication(sys.argv)

    ex = MainScreen()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()