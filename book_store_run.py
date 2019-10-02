from connect_book_database import *

server = 'localhost,1433'
database = 'ebook_store_db'
username = 'SA'
password = 'Passw0rd2018'

book_store = Ebook_Store(server, database, username, password)

book_store.print_all_book_info()

print(book_store.search_book_title("Cloud Atlas"))

book_store.add_book_to_table("Of Mice and Men", "John Steinbeck", "1955/04/01")
book_store.print_all_book_info()

book_store.update_book_in_table('date_published', '1937', 'book_title', 'Of Mice and Men')
book_store.print_all_book_info()

book_store.delete_book_in_table('Of Mice and Men')
book_store.print_all_book_info()

