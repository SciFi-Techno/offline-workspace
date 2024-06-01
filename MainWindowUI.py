from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Set the title of the window
        self.setWindowTitle("Testing")

        # Create the layouts within the main window
        layout_1 = QVBoxLayout()
        layout_2 = QHBoxLayout()

        # Create page selection bar and add it to layout_2
        page_selector = self.add_page_selector()
        layout_2.addStretch()
        layout_2.addWidget(page_selector, Qt.AlignCenter)
        layout_2.addStretch()

        # Nest layout_2 under layout_1
        layout_1.addLayout(layout_2)

        # Placeholder for further widgets
        #layout_1.addWidget()

        # Create the widget that houses all other widgets
        widget = QWidget()
        widget.setLayout(layout_1)
        self.setCentralWidget(widget)

        # Open window as full screen
        self.showMaximized()

    '''
    This function creates and adds the page selection 
    bar at the top of the main window
    '''
    def add_page_selector(self):
        page_selector = QComboBox()
        page_selector.setFixedWidth(400)
        page_selector.setFixedHeight(35)
        page_selector.setEditable(True)
        page_selector.setInsertPolicy(QComboBox.InsertAlphabetically)
        page_selector.currentIndexChanged.connect(self.selection_change)
        return page_selector

    '''
    This function carries out some action upon 
    selection of a page
    '''
    def selection_change(self, selected):
        print(selected)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()