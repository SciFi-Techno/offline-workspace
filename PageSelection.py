from Data import data_storage, data_cursor

from PyQt5.QtWidgets import QComboBox
import numpy as np

class PageSelector(QComboBox):

    """
    This function creates the page selection bar at the top
    of the main window and sets the signal for whenever the
    person changes the page
    """
    def __init__(self):
        super().__init__()

        # Set fixed width and height of the bar
        self.setFixedWidth(250)
        self.setFixedHeight(35)

        # Allow user to make new pages by editing directly from bar
        self.setEditable(True)

        # New pages added to bottom of pages list
        self.setInsertPolicy(QComboBox.InsertAtBottom)

        # Placeholder variable for holding the TextSpace object
        self.input_space = None

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

        # The following code adds, updates, and retrieves pages and their data from the database
        index_list_1 = data_cursor.execute("SELECT page_index FROM pages_data")

        # Check if there are any pages in the database
        if len(index_list_1.fetchall()) == 0:

            # If there are no pages, add a page to the database when a user creates a new page
            data_cursor.execute("""
                        INSERT INTO pages_data VALUES
                            (?, '')""", (selected_index, ))
            data_storage.commit()
        else:

            # Obtain all page indexes in the database and convert to a numpy array
            index_list_2 = data_cursor.execute("SELECT page_index FROM pages_data")
            indexes = np.array(index_list_2.fetchall())

            # If the current user-selected page exists in the database, retrieve its data from database
            if selected_index in indexes:
                data = data_cursor.execute("SELECT data FROM pages_data WHERE page_index = ?", (selected_index,))
                cursor.insertText(data.fetchone()[0].decode(errors="ignore"))

            # Add a new user-made page into the database
            else:
                cursor.removeSelectedText()
                data_cursor.execute("""
                            INSERT INTO pages_data VALUES
                                (?, '')""", (selected_index, ))
                data_storage.commit()

    '''
    This function retrieves the current page's index
    '''
    def current_page_index(self):
        return self.currentIndex()