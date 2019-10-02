# import the class file
from connect_book_database import *

# set up the basic needs to get access to the server with the database info in it
server = 'localhost,1433'
database = 'ebook_store_db'
username = 'SA'
password = 'Passw0rd2018'

# make a class instance for the database
book_store = Ebook_Store(server, database, username, password)

# use a method to print all the book info
book_store.print_all_book_info()

# use a method to look for book with title 'Cloud Atlas'
print(book_store.search_book_title("Cloud Atlas"))

# use a method to add a book to the table 'books' in the database
book_store.add_book_to_table("Of Mice and Men", "John Steinbeck", "1955/04/01")
book_store.print_all_book_info()

# use a method to update the date published in the table in the database
book_store.update_book_in_table('date_published', '1937', 'book_title', 'Of Mice and Men')
book_store.print_all_book_info()

# use a method to delete the book 'Of Mice and Men'
book_store.delete_book_in_table('Of Mice and Men')
book_store.print_all_book_info()

