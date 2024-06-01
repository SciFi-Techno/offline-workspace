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
        self.page_selector = self.add_page_selector()
        layout_2.addStretch()
        layout_2.addWidget(self.page_selector, Qt.AlignCenter)
        layout_2.addStretch()

        # Nest layout_2 under layout_1
        layout_1.addLayout(layout_2)

        # Placeholder for further widgets
        self.text_space = self.add_text_space()
        layout_1.addWidget(self.text_space)

        # Create the widget that houses all other widgets
        widget = QWidget()
        widget.setLayout(layout_1)
        self.setCentralWidget(widget)

        # Open window as full screen
        self.showMaximized()

    '''
    This function creates and returns the page selection 
    bar at the top of the main window
    '''
    def add_page_selector(self):
        # Initialize the page selection bar
        page_selector = QComboBox()
        page_selector.setFixedWidth(400)
        page_selector.setFixedHeight(35)

        # Allow user to add new pages
        page_selector.setEditable(True)

        # New pages are added to bottom of the pages list
        page_selector.setInsertPolicy(QComboBox.InsertAtBottom)

        # Carry out actions based on changes to page selection bar
        page_selector.currentIndexChanged.connect(self.page_selection_actions)
        return page_selector

    '''
    This function creates and returns the text space
    '''
    def add_text_space(self):
        text_space = QTextEdit()
        return text_space

    '''
    This function carries out some action upon
    selection of a page
    '''
    def page_selection_actions(self, selected_index):
        print(selected_index, self.page_selector.itemText(selected_index))


app = QApplication([])

window = MainWindow()
window.show()

app.exec()