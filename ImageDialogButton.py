from PyQt5.QtWidgets import QPushButton, QFileDialog
from PyQt5.QtGui import QImage, QPixmap

class ButtonImages(QPushButton):
    def __init__(self, input_text_space):
        super().__init__()

        # Creates a button for inserting images
        self.setText("Insert Image")

        # Set dimensions of the button
        self.setFixedSize(110, 35)

        self.input_space = input_text_space

        self.clicked.connect(self.add_image_dialog)

    def add_image_dialog(self):
        file = QFileDialog.getOpenFileName(self, 'Open Image',
                                           "/Users", "Images files (*.jpg *.gif *.png)",
                                           options=QFileDialog.DontUseNativeDialog)
        image = QImage(file[0])
        self.input_space.setImage(image)