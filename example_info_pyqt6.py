import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

class ProfileWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        """Настройки графического интерфейса приложения."""
        self.setGeometry(100, 100, 700, 1000)
        self.setWindowTitle("example_profile")
        self.setUpMainWindow()
    
    def setUpMainWindow(self):
        """Создание и настройка виджетов для профиля."""
        # Главный layout
        main_layout = QVBoxLayout()
        
        # Верхняя часть с изображением
        image_label = QLabel()
        pixmap = QPixmap("profile.png")
        
        # Масштабируем изображение если нужно
        if not pixmap.isNull():
            pixmap = pixmap.scaled(513, 534, Qt.AspectRatioMode.KeepAspectRatio)
            image_label.setPixmap(pixmap)
        else:
            image_label.setText("Изображение не найдено")
        
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(image_label)
        
        # Имя пользователя
        name_label = QLabel("Таланян Артур")
        name_label.setFont(QFont("Verdana", 30))
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(name_label)
        
        # Биография
        bio_label = QLabel("Биография:")
        bio_label.setFont(QFont("Verdana", 20))
        bio_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        main_layout.addWidget(bio_label)
        
        bio_info_label = QLabel("Студент 2-го курса в МАИ, Инноватика, М3О-236БВ-24")
        bio_info_label.setFont(QFont("Verdana", 14))
        bio_info_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        main_layout.addWidget(bio_info_label)
        
        # Добавляем отступ
        main_layout.addSpacing(20)
        
        # Умения
        skills_label = QLabel("Умения:")
        skills_label.setFont(QFont("Verdana", 20))
        skills_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        main_layout.addWidget(skills_label)
        
        skills_info_label = QLabel("Базовый Python, SQL")
        skills_info_label.setFont(QFont("Verdana", 14))
        skills_info_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        main_layout.addWidget(skills_info_label)
        
        # Добавляем отступ
        main_layout.addSpacing(20)
        
        # Опыт
        exp_label = QLabel("Опыт:")
        exp_label.setFont(QFont("Verdana", 20))
        exp_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        main_layout.addWidget(exp_label)
        
        exp_info_label = QLabel("Отсутствует")
        exp_info_label.setFont(QFont("Verdana", 14))
        exp_info_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        main_layout.addWidget(exp_info_label)
        
        # Добавляем растягивающийся элемент в конце
        main_layout.addStretch()
        
        self.setLayout(main_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProfileWindow()
    window.show()
    sys.exit(app.exec())