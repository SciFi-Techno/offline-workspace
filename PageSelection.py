from Data import data_cursor

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

        self.input_space = 0

        self.currentIndexChanged.connect(self.page_selection_change)

    '''
    This function allows PageSelector to access the TextSpace object
    '''
    def set_text_space(self, text_space):
        self.input_space = text_space

    ''' 
    This function retrieves and inserts data for their respective
    pages or it clears the text space when a new page is made
    '''
    def page_selection_change(self, selected_index):

        # Creates a cursor in text space for manipulating the text
        cursor = self.input_space.textCursor()
        self.input_space.setTextCursor(cursor)
        cursor.movePosition(cursor.End)
        cursor.select(cursor.Document)

        # Obtain list of pages made by user
        index_list = data_cursor.execute("SELECT page_index FROM pages_data")
        for indexes in index_list.fetchall():
            if selected_index not in indexes:

                # Remove cursor selected text/Clear the currently written input if a new page is made
                cursor.removeSelectedText()
            else:

                # Replace the currently written input with a selected page's respective data
                data = data_cursor.execute("SELECT data FROM pages_data WHERE page_index = ?", (selected_index,))
                cursor.insertText(data.fetchone()[0])

                # TESTING
                print(data.fetchall())

    '''
    This function retrieves the current page's index
    '''
    def current_page_index(self):
        return self.currentIndex()