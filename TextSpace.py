from Data import data_storage, data_cursor

from PyQt5.QtWidgets import QTextEdit

class InputTextSpace(QTextEdit):

    """
    This function creates the text space and sets the signal
    for retrieving user written text
    """
    def __init__(self, page_selector):
        super().__init__()

        # Access to PageSelection object
        self.page_selection_bar = page_selector
        self.page_selection_bar.set_text_space(self)

        self.textChanged.connect(self.getText)

    '''
    This function obtains and saves the user written text into
    a database
    '''
    def getText(self):

        # Obtain the current page's index
        index = self.page_selection_bar.current_page_index()

        # Check if there is any data on the current page
        if len(self.toPlainText()) == 0:

            # Add the current page's data and index to the database storage
            data_cursor.execute("""
                        INSERT INTO pages_data VALUES
                            (?, ?)""", (index, self.toPlainText()))
        else:

            # If there already is data, update the entry in database
            data_cursor.execute("UPDATE pages_data SET data = ? WHERE page_index = ?",
                                (self.toPlainText(), index))

        data_storage.commit()

        # TESTING
        res = data_cursor.execute("SELECT * FROM pages_data")
        print(res.fetchall())