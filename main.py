import sys
from PyQt5.QtWidgets import QApplication
from ui import PDFMergerWindow 

def main():
    app = QApplication(sys.argv)
    window = PDFMergerWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
