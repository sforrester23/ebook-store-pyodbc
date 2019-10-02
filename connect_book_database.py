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

    def add

