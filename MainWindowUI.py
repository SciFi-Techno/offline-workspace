import PageSelection, TextSpace, ImageDialogButton

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):

    """
    This function creates the main UI of the application
    """
    def __init__(self):
        super(MainWindow, self).__init__()

        # Set the title of the window
        self.setWindowTitle("Testing")

        # Create the layouts within the main window
        layout_1 = QVBoxLayout()
        layout_2 = QHBoxLayout()

        # Create page selection bar, a text space, and a button and add the first two components to layout_2
        self.page_selector = PageSelection.PageSelector()
        self.text_space = TextSpace.InputTextSpace(self.page_selector)
        self.image_button = ImageDialogButton.ButtonImages(self.text_space)
        layout_2.addWidget(self.page_selector, Qt.AlignCenter)
        layout_2.addWidget(self.image_button, Qt.AlignRight)
        layout_2.addStretch()

        # Nest layout_2 under layout_1 and add the button to layer 1
        layout_1.addLayout(layout_2)
        layout_1.addWidget(self.text_space)

        # Create the widget that houses all other widgets
        widget = QWidget()
        widget.setLayout(layout_1)

        # Set the colors of the widget
        widget.setStyleSheet("""
            background-color: #d9ead3;
            color: grey;
            """)

        self.setCentralWidget(widget)

        # Open window as full screen
        self.showMaximized()

# This is the start of the application
app = QApplication([])
window = MainWindow()
window.show()
app.exec()