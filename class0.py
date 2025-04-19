# class Book:
#     #This is a class to represent a book in a library system. (Lushao method)

#     def __init__(self, t1, a1):
#         self.title = t1
#         self.author = a1
#         self.available = True
    
#     def __str__(self):
#         return f"Title: {self.title}, Author: {self.author}, Available: {self.available}"

#     def borrow(self):
#         if self.available:
#             self.available = False
#             return True
#         else:
#             return f"Book '{self.title}' is not available for borrowing."
        
#     def return_book(self): 
#         self.available = True
#         return True
    
#     def get_info(self):
#         if self.available:
#             return f"Title: {self.title}, Author: {self.author}, Available"
#         else:
#             return f"Title: {self.title}, Author: {self.author}, Not Available"
        
    
# book1 = Book("1984", "George Orwell")
# print(book1.get_info())

# book1.borrow()
# print(book1.get_info())

# print(book1.borrow())


# io=book1.return_book()
# print(io)
# print(book1.get_info())


class Book:
    # Real solution
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True  # Default: book is available

    def borrow_book(self):
        if self.available:
            self.available = False
            print(f"You have borrowed '{self.title}'.")
        else:
            print("Sorry, the book is already borrowed.")

    def return_book(self):
        self.available = True
        print(f"You have returned '{self.title}'.")

    def get_info(self):
        status = "Available" if self.available else "Not Available"
        return f"{self.title} by {self.author} - {status}"


# **Testing the class**
book1 = Book("1984", "George Orwell")
print(book1.get_info())  # Output: 1984 by George Orwell - Available

book1.borrow_book()
print(book1.get_info())  # Output: 1984 by George Orwell - Not Available

book1.borrow_book()  # Output: Sorry, the book is already borrowed.

book1.return_book()
print(book1.get_info())  # Output: 1984 by George Orwell - Available