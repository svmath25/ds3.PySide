import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Настройте графический интерфейс приложения."""
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle("Начало")
        self.setUpMainWindow()

    def setUpMainWindow(self):
        """Создайте QLabel для отображения в главном окне."""
        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Приветственная надпись
        hello_label = QLabel("Добро пожаловать!", central_widget)
        hello_label.setFont(QFont("Arial", 15))
        hello_label.move(175, 15)

        # Загрузка и отображение изображения
        image_path = r"assets\pht1.jpg"
        try:
            if os.path.exists(image_path):
                world_label = QLabel(central_widget)
                pixmap = QPixmap(image_path)
                # Масштабируем изображение
                scaled_pixmap = pixmap.scaled(490, 500, Qt.AspectRatioMode.KeepAspectRatio,
                                              Qt.TransformationMode.SmoothTransformation)
                world_label.setPixmap(scaled_pixmap)
                world_label.move(0, 40)
                world_label.resize(scaled_pixmap.size())
            else:
                print(f"Image not found: {image_path}")
        except Exception as error:
            print(f"Error loading image: {error}")


class SecondWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Настройте графический интерфейс для второго окна."""
        self.setGeometry(550, 100, 400, 700)
        self.setWindowTitle("Профиль пользователя")
        self.setUpMainWindow()

    def createImageLabels(self):
        """Открывает файлы изображений и создаёт метки изображений."""
        images = [r"assets\photo.jpg"]

        for image_path in images:
            try:
                if os.path.exists(image_path):
                    label = QLabel(self.centralWidget())
                    pixmap = QPixmap(image_path)
                    # Масштабируем изображение
                    scaled_pixmap = pixmap.scaled(410, 410, Qt.AspectRatioMode.KeepAspectRatio,
                                                  Qt.TransformationMode.SmoothTransformation)
                    label.setPixmap(scaled_pixmap)
                    label.move(0, 0)
                    label.resize(scaled_pixmap.size())
                else:
                    print(f"Файл {image_path} не найден")
            except Exception as e:
                print(f"Ошибка при загрузке изображения {image_path}: {e}")

    def setUpMainWindow(self):
        """Создайте метки, которые будут отображаться в окне."""
        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.createImageLabels()

        # Информация о пользователе
        bio_label = QLabel("Биография: Калганова Софья, 19 лет.", central_widget)
        bio_label.setFont(QFont("Arial", 15))
        bio_label.move(15, 410)
        bio_label.resize(390, 30)

        teach_label = QLabel("Обучение: МАИ , 2 курс , 317 кафедра - Инноватика", central_widget)
        teach_label.setFont(QFont("Arial", 17))
        teach_label.setWordWrap(True)
        teach_label.move(15, 450)
        teach_label.resize(370, 50)

        experience_label = QLabel("Опыт работы: отсутствует, в процессе", central_widget)
        experience_label.setFont(QFont("Arial", 16))
        experience_label.move(15, 520)
        experience_label.resize(370, 30)

        developer_label = QLabel("Фраза - чего то, то добиться надо", central_widget)
        developer_label.setFont(QFont("Arial", 16))
        developer_label.move(15, 550)
        developer_label.resize(370, 50)


# Запуск приложения
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window1 = SecondWindow()

    window.show()
    window1.show()

    sys.exit(app.exec())