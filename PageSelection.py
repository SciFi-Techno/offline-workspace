from PyQt5.QtWidgets import QComboBox

class PageSelector(QComboBox):

    """
    This function creates the page selection bar at the top
    of the main window and sets the signal for whenever the
    person changes the page
    """
    def __init__(self):
        super().__init__()

        # Set fixed width and height of the bar
        self.setFixedWidth(400)
        self.setFixedHeight(35)

        # Allow user to make new pages by editing directly from bar
        self.setEditable(True)

        # New pages added to bottom of pages list
        self.setInsertPolicy(QComboBox.InsertAtBottom)

        self.currentIndexChanged.connect(self.page_selection_actions)

    '''
    This function carries out some action upon selection of a 
    page
    '''
    def page_selection_actions(self, selected_index):
        print(selected_index, self.itemText(selected_index))

    def current_page_index(self):
        return self.currentIndex()