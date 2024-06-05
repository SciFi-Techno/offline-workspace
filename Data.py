import sqlite3

# Create the database which will hold all the data
data_storage = sqlite3.connect("workspace_data.db")

# Create the cursor to iterate through the database
data_cursor = data_storage.cursor()

# Create the table that stores the data
data_cursor.execute("CREATE TABLE IF NOT EXISTS pages_data(page_index, data)")