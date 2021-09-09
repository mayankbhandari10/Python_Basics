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
         #print(line)
         self.books_dict.update({str(id):{"Book_title":line.replace("\n"," "),
         "lender_name":"","Issue_date":"","status":"Available"}})
         id=id+1

    def display_books(self):
        print("-----------------------------List of Books-----------------------------------")
        print("Books ID", "\t", "Title")
        print("------------------------------------------------------------------------------")
        #loop over book dic
        for key,value in self.books_dict.items():
            print(key,"\t\t",value.get("Book_title"),"-[",value.get("status"),"]")

    def Issue_books(self):
       books_id=input("Enter the book Id")
       current_time=datetime.datetime.now().strftime("%Y-%m_%d %H:%M:%S")
       if books_id in self.books_dict.keys():
           if not self.books_dict[books_id]["status"] ==["Available"]:
               print(f"This books is already issued to {self.books_dict[books_id]['lender_name']} \
               on {self.books_dict[books_id]['Issue_date']}")
           return self.books_dict()
       elif self.books_dict[books_id]["status"] ==["Available"]:
           your_name= input("Enter your name")
           self.books_dict[books_id]['lender_name']=your_name
           self.books_dict[books_id]['Issue_date']=current_time
           self.books_dict[books_id]['status']='Already issued'
           print(f"Books issued to {your_name}")
       else:
           print("BookId not found !!!!")
           return self.books_dict()
lib=(LMS("List_of_books.txt", "Library system"))
print(lib.display_books())