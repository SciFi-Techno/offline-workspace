from PyQt5.QtWidgets import QPushButton, QFileDialog

class ButtonImages(QPushButton):
    def __init__(self):
        super().__init__()

        # Creates a button for inserting images
        self.setText("Insert Image")

        # Set dimensions of the button
        self.setFixedSize(110, 35)

        #self.clicked.connect(self.add_image_dialog())

    def add_image_dialog(self):
        file = QFileDialog.getOpenFileName(self, 'Open Image',
                                           "/Users", "Images files (*.jpg *.gif *.png)",
                                           options=QFileDialog.DontUseNativeDialog)
        if (file):
            print(file)