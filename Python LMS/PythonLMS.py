import datetime
import os


# os.getcwd() #it will show the working directory
import self as self


class LMS:
    """ This class is uded to keep record of books library.
    It has total four module: "Display books","Issue books","Return books","Add books", """

    # creating constructor
    def __init__(self, list_of_books, library_name):
        self.list_of_books = "List_of_books.txt"
        self.library_name = library_name
        self.books_dict = {}  # it will have all the books info like name, title, issue date
        id = 101
        # read notepad file

        fhand = open('list_of_books.txt','r')
        lines=fhand.readlines()
        for line in lines:
         print(line)
         self.books_dict.update()
print(LMS("List_of_books.txt", "Library system"))
