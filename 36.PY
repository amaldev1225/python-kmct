
class Publisher:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Publisher:", self.name)


class Book(Publisher):

    def __init__(self, name, title, author):
        Publisher.__init__(self, name)
        self.title = title
        self.author = author


class Python(Book):

    def __init__(self, name, title, author, price, no_of_pages):
        Book.__init__(self, name, title, author)
        self.price = price
        self.no_of_pages = no_of_pages

    def display(self):
        print("Publisher:", self.name)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Number of pages:", self.no_of_pages)


p = Python("ABC", "Python Basics", "John", 500, 200)

p.display()
