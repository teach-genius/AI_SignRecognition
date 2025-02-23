from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap, QIcon
from templates import Home 
import sys

#version de python utilisée 3.9.11

class Connexion(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        icon_path = "icons/icon_logo.svg"
        self.setFixedSize(1200, 600)
        self.setWindowIcon(QIcon(QPixmap(icon_path)))
        self.set_win_title("SilentVoice")
        self.setCentralWidget(Home(self))

    def setframe(self, fen):
        self.setCentralWidget(fen)
        
    def set_win_title(self, title):
        self.setWindowTitle(title)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Connexion()
    window.show()
    sys.exit(app.exec())
