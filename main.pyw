import sys
from View import MainWindow as mw
from PyQt6.QtWidgets import QApplication

def main():
    print("test")
    app = QApplication( sys.argv )
    
    main_window = mw.MainWindow()

    app.exec()

if __name__ == '__main__':
    sys.exit(  main() )