import MainWindowUI

from PyQt5.QtWidgets import QTextEdit

class TextSpace(QTextEdit):

    """
    This function creates the text space and sets the signal
    for retrieving user written text
    """
    def __init__(self):
        super().__init__()
        self.textChanged.connect(self.getText)

        self.__data_dict = {}

    '''
    This function obtains the user written text
    '''
    def getText(self):
        index = MainWindowUI.window.page_selector.current_page_index()
        self.__data_dict[index] = self.toPlainText()
        print(self.__data_dict)

    def check_key_in_dict(self, page_index):
        if page_index in self.__data_dict:
            return True
        else:
            return False
