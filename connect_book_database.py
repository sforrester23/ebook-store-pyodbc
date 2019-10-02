# Import the necessaries
import pyodbc

# Set up a class for the database of books
class Ebook_Store():
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connect_db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
        self.cursor = self.connect_db.cursor()

    # method for encapsulating something that can execute queries, but cannot be accessed outside of this page.
    def __filter_query(self, query):
        return self.cursor.execute(query)

    # method for querying all books from the table 'books' of the database
    def query_all_books(self):
        return self.__filter_query("SELECT * FROM books")

    # method for printing all the books in the database, using a loop and .fetchone() to get each one and end when the last one is done
    def print_all_book_info(self):
        all_book_query = self.query_all_books()
        while True:
            record = all_book_query.fetchone()
            if record is None:
                break
            print(record)

    # method for finding a book based on its book title
    def search_book_title(self, book_title):
        title_query = self.__filter_query("SELECT * FROM books WHERE book_title = '{}'".format(str(book_title)))
        return title_query.fetchone()

    # method for adding a book to a table, telling the user when it is done
    def add_book_to_table(self, book_title, book_author, date_published):
        self.__filter_query("INSERT INTO books VALUES ('{}', '{}', '{}')".format(book_title, book_author, date_published))
        # this .commit() applied to the connection attribute of the database will make sure the changes commit and alters the persistent data
        self.connect_db.commit()
        print('Insertion Complete')

    # method for updating an entry in the table, based on certain critera on what to change and which entries to change. Similarly uses .commit() to change the persistent date
    def update_book_in_table(self, value_to_update, new_value, condition_column, condition_value):
        self.__filter_query("UPDATE books SET {} = '{}' WHERE {} = '{}'".format(value_to_update, new_value, condition_column, condition_value))
        self.connect_db.commit()
        print('Update Complete')

    # method for deleting an entry in a table, based on the book title you'd like to delete. Using .commit() to change persistent date
    def delete_book_in_table(self, book_to_delete):
        self.__filter_query("DELETE FROM books WHERE book_title = '{}'".format(book_to_delete))
        self.connect_db.commit()
        print('Removal complete')

