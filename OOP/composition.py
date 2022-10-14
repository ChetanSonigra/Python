#  use of one or more classes inside one class.

class Book:
    def __init__(self,title,price,author = None):
        self.title = title
        self.price = price
        self.author = author
        self.chapters = []
    
    def addchapters(self, chapter):
        self.chapters.append(chapter)

    def getbookpagecount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pagecount
        return result

class Chapter:
    def __init__(self,name, pagecount):
        self.name = name
        self.pagecount = pagecount

class Author:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    
auth = Author('leo', 'tolstoy')
b1 = Book('war and peace', 39.0, auth)
b1.addchapters(Chapter('1',123))
b1.addchapters(Chapter('2', 55))
print(b1.author)
print(b1.title, b1.getbookpagecount())
