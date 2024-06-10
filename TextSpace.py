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

        self.textChanged.connect(self.setText)

    '''
    This function obtains and saves the user written text into
    a database
    '''
    def setText(self):

        # Obtain the current page's index
        index = self.page_selection_bar.current_page_index()

        # Updates the respective page data in the database
        data_cursor.execute("UPDATE pages_data SET data = ? WHERE page_index = ?",
                            (self.toPlainText().encode(), index))
        data_storage.commit()

    '''
    This function receives an image as QImage and as bytes
    which is then stored in the database and displayed on 
    text space
    '''
    def setImage(self, image, image_bytes):
        cursor = self.textCursor()

        # Obtain the current page's index
        index = self.page_selection_bar.current_page_index()

        # Updates the respective page data in the database
        data_cursor.execute("UPDATE pages_data SET data = ? WHERE page_index = ?",
                            (image_bytes, index))
        data_storage.commit()

        # Output image in the text space
        cursor.insertImage(image)