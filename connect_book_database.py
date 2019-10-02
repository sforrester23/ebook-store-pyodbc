import pyodbc

class Ebook_Store():
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connect_db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
        self.cursor = self.connect_db.cursor()

    def __filter_query(self, query):
        return self.cursor.execute(query)

    def query_all_books(self):
        return self.__filter_query("SELECT * FROM books")

    def print_all_book_info(self):
        all_book_query = self.query_all_books()
        while True:
            record = all_book_query.fetchone()
            if record is None:
                break
            print(record)

    def search_book_title(self, book_title):
        title_query = self.__filter_query("SELECT * FROM books WHERE book_title = '{}'".format(str(book_title)))
        return title_query.fetchone()

    def add_book_to_table(self, book_title, book_author, date_published):
        self.__filter_query("INSERT INTO books VALUES ('{}', '{}', '{}')".format(book_title, book_author, date_published))
        self.connect_db.commit()

    def update_book_in_table(self, value_to_update, new_value, condition_column, condition_value):
        self.__filter_query("UPDATE books SET {} = '{}' WHERE {} = '{}'".format(value_to_update, new_value, condition_column, condition_value))
        self.connect_db.commit()

