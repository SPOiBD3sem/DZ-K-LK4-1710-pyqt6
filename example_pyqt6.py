import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        self.setGeometry(1000, 1000, 900, 800)
        self.setWindowTitle("Пример QLabel")
        self.setUpMainWindow()
        self.show()
    
    def setUpMainWindow(self):
        label = QLabel("Hello, World!", self)
        label.move(500, 50)
        
        image_label = QLabel(self)
        pixmap = QPixmap("globe.png")  # Укажите путь к вашему изображению
        image_label.setPixmap(pixmap)
        image_label.move(30, 80)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())