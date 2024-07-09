class Book:
    def __init__(self,isbn,name,athour,pages,price):
        self.isbn=isbn
        self.name=name
        self.athour=athour
        self.pages=pages
        self.price=price
    def __str__(self):
        return (f"The book is {self.isbn} {self.name}")
    def __repr__(self):
        print(f"{self.pages},{self.price}")
book1=Book(1001,"Python","Ali",150,150000)
print(book1)
book1.__repr__()