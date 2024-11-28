'''WAP to print a library system created a class called Bools taht represent a books of library with the help of oop's concept'''

class Book():
    def __init__(self,title,author,isbn,status):
        self.book_title=title
        self.book_author=author
        self.book_ISBN_no=isbn
        self.avl_status=status
    
    def checkout(self):
        if self.avl_status is "available":
            return "Checked-Out Book Successfully..."            
    def return_book(self):
        if self.avl_status is "checked-out":
            return "Return Book Successfully..."            

    def get_book(self):
        return f"""
                Book Title : {self.book_title}
                Book Author : {self.book_author}
                Book ISBN Code : {self.book_ISBN_no}
                Book Status : {self.checkout() or self.return_book()}    """

b1=Book("Marathi Sahitya","Rohit",123456,"available")
print(b1.get_book())