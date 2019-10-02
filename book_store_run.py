from connect_book_database import *

server = 'localhost,1433'
database = 'ebook_store_db'
username = 'SA'
password = 'Passw0rd2018'

book_store = Ebook_Store(server, database, username, password)

book_store.print_all_book_info()

print(book_store.search_book_title("Cloud Atlas"))