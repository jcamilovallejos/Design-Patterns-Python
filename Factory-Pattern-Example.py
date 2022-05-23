
class Book:
    book_title = ""
    book_author = ""

    def __init__(self,title,author):
        self.book_title = title
        self.book_author = author

    def getNameAndAuthor(self):
        return self.book_title + 'by ' + self.book_author


class BookFactory:
    @staticmethod
    def create(title,author):
        book = Book(title,author)
        return book

book = BookFactory.create("Cien anios de soledad","Gabriel Garcia Marquez")
print("Books info:" + book.getNameAndAuthor())




    
