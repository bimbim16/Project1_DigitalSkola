from modules.library_item import LibraryItem

class Book(LibraryItem):
    def __init__(self, title, subject, upc, issbn, authors, dss_number):
        LibraryItem.__init__(self, title, upc, subject)
        self.issbn = issbn
        self.authors = authors
        self.dss_number = dss_number
        