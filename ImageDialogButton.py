from PyQt5.QtWidgets import QPushButton, QFileDialog
from PyQt5.QtGui import QImage

class ButtonImages(QPushButton):
    def __init__(self, input_text_space):
        super().__init__()

        # Creates a button for inserting images
        self.setText("Insert Image")

        # Set dimensions and color of the button
        self.setFixedSize(110, 35)
        self.setStyleSheet("""
            background-color: #b6d7a8;
            color: black;""")

        self.input_space = input_text_space

        self.clicked.connect(self.add_image_dialog)

    def add_image_dialog(self):

        # Open the file for showing it on text space specifically
        file = QFileDialog.getOpenFileName(self, 'Open Image',
                                           "/Users", "Images files (*.jpg *.gif *.png)",
                                           options=QFileDialog.DontUseNativeDialog)
        file_bytes = open(file[0], 'rb').read()
        image = QImage(file[0])
        self.input_space.setImage(image, file_bytes)