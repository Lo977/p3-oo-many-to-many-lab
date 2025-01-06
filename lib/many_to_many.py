class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])
    
    def __repr__(self):
        return f"Author(name={self.name})"


class Book:
    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        print(f'self from book contracts{self}')
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]
    
    def __repr__(self):
        return self.title



class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError
        
        if not isinstance(book, Book):
            raise TypeError
        
        if not isinstance(date, str):
            raise TypeError
        
        if not isinstance(royalties, int):
            raise TypeError
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
        print(f"self_author is {self.author.name} and self_book is {self.book.title}")
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
    
    def __repr__(self):
        return f"Contract(author={self.author.name}, book={self.book.title}, date={self.date}, royalties={self.royalties})"

#Create Authors
author1 = Author("Alice")
author2 = Author("Bob")

#Create books
book1 = Book("Python 101")
book2 = Book("Advanced Python")

# Sign Contracts
contract1 = author1.sign_contract(book1,"01-01-2025", 1000)
contract2 = author1.sign_contract(book2,"02-02-2025",1500)
contract3 = author2.sign_contract(book1,"03-03-2025",1200)

# view authors and their books
# print(author1.books())
print(f" {author1.name} has signed contracts for books: {author1.books()}")
print(f"{author2.name} has signed contracts for books: {author2.books()}")

# Total Royalties
print(f" {author1.name}'s total royalties is :{author1.total_royalties()}")

# View contracts by dates:
print(f" Contracts signed on 01-01-2025: {Contract.contracts_by_date('01-01-2025')}")
print(f"author contracts:{author1.contracts()} and Author name :{contract1.author}")