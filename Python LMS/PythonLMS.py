import datetime
import os


# os.getcwd() #it will show the working directory
import self as self

class LMS:
    """ This class is used to keep record of books library.
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

    def add_a_book(self):
         new_book=("Enter the book title")
         if new_book== "":
             return self.add_a_book()
         elif len(new_book) >25:
             print("Book title is too long !!!")
             return self.add_a_book()
         else:
             fhand = open(self.list_of_books, 'a')
             lines = fhand.writelines(new_book)
             new_id= int(max(self.books_dict))+1
             #print(new_id)
             #self.books_dict.update(str({new_id:),{'books_title':"new_book" ,'lender_name':"",'Issue_date':"",'status':"Available"}})
             self.books_dict.update({str(int(max(self.books_dict))+1):{'books_title':"new_book",'lender_name':"",'Issue_date':"",'status':"Available"}})
             print(f"This book{new_book}has been added!!!!")

    def submit_book(self):
            book_id=input("Enter book id")
            if book_id in self.books_dict():
                if self.books_dict[book_id]["status"]=="Available":
                    print("Book is already available. Please check your book id")
                    return self.submit_book()
                elif not self.books_dict[book_id]["status"]=="Available":
                    self.books_dict[book_id]["lender_name"]=""
                    self.books_dict[book_id]["Issue_date"]=""
                    self.books_dict[book_id]["status"]="Available"
                    print("Library updated Successfully")
                else:
                     print("Book Id not found")

try:
    myLMS=LMS("List_of_books.txt","Python's")
    press_key_list={"D":"display","I":"Issues books", "A":"Add books","R":"Return Books","Q": "Quit books"}
    key_press= False
    while not (key_press=='q'):
        print(f"welcome to the {myLMS.library_name}")
        for key,value in press_key_list.items():
            print("Press",key,"To",value)
        key_press=input("press keys:").lower()
        if key_press=="i":
            print("\n current selection: Issued book")
            myLMS.Issue_books()
        elif key_press=="a":
            print("\n current selection: Add a book")
            myLMS.display_books()
        elif key_press=="d":
            print("\n current selection: Display a book")
        elif key_press=='q':
            break
        else:
            continue
except Exception as e:
    print("something went wrong, Please check the input")
    print(e)



lib=(LMS("List_of_books.txt", "Library system"))
print(lib.display_books())
#lib.Issue_books()
#lib.add_a_book()
