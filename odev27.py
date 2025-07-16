import sys
import pytesseract
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QFileDialog
from PyQt5.QtGui import QPixmap
from PIL import Image

# Eğer Windows kullanıyorsan aşağıdaki satırın yorumunu kaldır ve doğru yolu belirt
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class OCRApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OCR Reader")
        self.setGeometry(100, 100, 600, 400)

        self.label = QLabel("Select an image to read text.", self)
        self.label.setWordWrap(True)

        self.image_label = QLabel(self)
        self.image_label.setFixedSize(400, 250)

        self.button = QPushButton("Select Image", self)
        self.button.clicked.connect(self.select_image)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def select_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if file_name:
            pixmap = QPixmap(file_name)
            self.image_label.setPixmap(pixmap.scaled(self.image_label.size()))
            text = pytesseract.image_to_string(Image.open(file_name))
            self.label.setText(f"OCR Result:\n{text.strip()}" if text.strip() else "No text found.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OCRApp()
    window.show()
    sys.exit(app.exec_())

